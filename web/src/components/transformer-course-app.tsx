'use client'

import {
  Beaker,
  BookOpen,
  CheckCircle2,
  Code2,
  GitBranch,
  Layers,
  LockKeyhole,
  MapIcon,
  Network,
  Route,
  ShieldCheck,
  Sigma,
  X,
} from 'lucide-react'
import { useMemo, useState } from 'react'

import { MathMarkdown } from '@/components/math-markdown'
import {
  buildLearnerState,
  course,
  gradeDiagnostic,
  nextRecommendedNode,
  nodeById,
  stageLabel,
} from '@/lib/course/course-engine'
import type { CourseNode, CourseStage, DiagnosticAnswers, DiagnosticResult, PracticeItem } from '@/lib/course/types'

type PanelMode = 'lesson' | 'practice' | 'diagnostic' | 'lab' | 'project'

const panelModes: { id: PanelMode; label: string; icon: typeof BookOpen }[] = [
  { id: 'lesson', label: 'Lesson', icon: BookOpen },
  { id: 'practice', label: 'Practice', icon: Sigma },
  { id: 'diagnostic', label: 'Diagnostic', icon: Route },
  { id: 'lab', label: 'Lab', icon: Beaker },
  { id: 'project', label: 'Project', icon: Code2 },
]

const stages: CourseStage[] = [
  'problem-framing',
  'text-pipeline',
  'attention-mechanics',
  'transformer-layer',
  'model-architectures',
  'scale-and-variants',
  'capstone',
]

const trackClassByTrack = {
  architecture: 'trackArchitecture',
  attention: 'trackAttention',
  coding: 'trackCoding',
  math: 'trackMath',
  nlp: 'trackNlp',
  probability: 'trackProbability',
  project: 'trackProject',
  systems: 'trackSystems',
  training: 'trackTraining',
  vision: 'trackVision',
}

const completedNodesStorageKey = 'torchbloom.transformer.completedNodes'
const passedPracticeStorageKey = 'torchbloom.transformer.passedPractice'

function readStoredList(key: string) {
  if (typeof window === 'undefined') return []

  try {
    const stored = window.localStorage.getItem(key)
    const parsed = stored ? JSON.parse(stored) : []
    return Array.isArray(parsed) ? parsed.filter((value): value is string => typeof value === 'string') : []
  } catch {
    return []
  }
}

function writeStoredList(key: string, values: string[]) {
  if (typeof window === 'undefined') return
  window.localStorage.setItem(key, JSON.stringify(values))
}

function selectedDiagnosticAnswers(): DiagnosticAnswers {
  return Object.fromEntries(course.diagnosticQuestions.map((question) => [question.id, question.correctAnswer]))
}

function readinessLabel(result: DiagnosticResult) {
  return result.readiness === 'ready_for_attention_core' ? 'Ready for attention core' : 'Repair first'
}

function project(matrix: number[][], vector: number[]) {
  return matrix.map((row) => row.reduce((sum, value, index) => sum + value * (vector[index] ?? 0), 0))
}

function dot(left: number[], right: number[]) {
  return left.reduce((sum, value, index) => sum + value * (right[index] ?? 0), 0)
}

function softmax(values: number[]) {
  const max = Math.max(...values)
  const expValues = values.map((value) => Math.exp(value - max))
  const total = expValues.reduce((sum, value) => sum + value, 0)
  return expValues.map((value) => value / total)
}

function addUnique(values: string[], value: string) {
  return values.includes(value) ? values : [...values, value]
}

function GraphCanvas({
  completedNodeIds,
  onSelectNode,
  selectedNodeId,
}: {
  completedNodeIds: string[]
  onSelectNode: (nodeId: string) => void
  selectedNodeId: string
}) {
  const completed = new Set(completedNodeIds)
  const selectedNode = nodeById(course, selectedNodeId)
  const nodeMap = new Map(course.nodes.map((courseNode) => [courseNode.id, courseNode]))

  return (
    <section className="graphCanvas" aria-label="Transformer course knowledge graph">
      <div className="stageRail" aria-hidden>
        {stages.map((stage) => (
          <span key={stage}>{stageLabel(stage)}</span>
        ))}
      </div>

      <svg className="edgeLayer" viewBox="0 0 100 100" preserveAspectRatio="none" aria-hidden>
        {course.nodes.flatMap((targetNode) =>
          targetNode.prerequisites.map((sourceNodeId) => {
            const sourceNode = nodeMap.get(sourceNodeId)
            if (!sourceNode) return null
            const selectedEdge = sourceNode.id === selectedNode.id || targetNode.id === selectedNode.id
            const midX = (sourceNode.graph.x + targetNode.graph.x) / 2

            return (
              <path
                className={selectedEdge ? 'graphEdge active' : 'graphEdge'}
                d={`M ${sourceNode.graph.x} ${sourceNode.graph.y} C ${midX} ${sourceNode.graph.y}, ${midX} ${targetNode.graph.y}, ${targetNode.graph.x} ${targetNode.graph.y}`}
                key={`${sourceNode.id}-${targetNode.id}`}
              />
            )
          }),
        )}
      </svg>

      {course.nodes.map((courseNode) => {
        const isSelected = courseNode.id === selectedNodeId
        const isMastered = completed.has(courseNode.id)
        const isReady = courseNode.prerequisites.every((nodeId) => completed.has(nodeId))
        const Icon = isMastered ? CheckCircle2 : isReady ? GitBranch : LockKeyhole

        return (
          <button
            className={`graphNode ${trackClassByTrack[courseNode.track]} ${isSelected ? 'selected' : ''} ${
              isMastered ? 'mastered' : ''
            } ${isReady ? 'ready' : 'blocked'}`}
            key={courseNode.id}
            onClick={() => onSelectNode(courseNode.id)}
            style={{ left: `${courseNode.graph.x}%`, top: `${courseNode.graph.y}%` }}
            type="button"
          >
            <Icon aria-hidden />
            <strong>{courseNode.title}</strong>
            <small>{courseNode.track}</small>
          </button>
        )
      })}
    </section>
  )
}

function EquationBlock({ equation }: { equation?: string }) {
  if (!equation) return null
  return (
    <div className="equationBox">
      <span>Equation</span>
      <MathMarkdown>{`$$\n${equation}\n$$`}</MathMarkdown>
    </div>
  )
}

function SourceAnchors({ node }: { node: CourseNode }) {
  return (
    <div className="sourceList">
      <span>Source Anchors</span>
      {node.sourceAnchors.map((sourceAnchor) => (
        <code key={sourceAnchor}>{sourceAnchor}</code>
      ))}
    </div>
  )
}

function LessonPanel({ node }: { node: CourseNode }) {
  return (
    <div className="lessonStack">
      <p className="nodeSummary">{node.summary}</p>
      <EquationBlock equation={node.equation} />

      {node.lesson.map((section, index) => (
        <article className="lessonFrame" key={`${node.id}-${section.title}`}>
          <span>Frame {index + 1}</span>
          <h3>{section.title}</h3>
          <MathMarkdown>{section.body}</MathMarkdown>
        </article>
      ))}

      <div className="evidenceGrid">
        <div>
          <h3>Mastery Evidence</h3>
          <ul className="compactList">
            {node.masteryEvidence.map((item) => (
              <li key={item}>
                <MathMarkdown>{item}</MathMarkdown>
              </li>
            ))}
          </ul>
        </div>
        <div>
          <h3>Misconceptions</h3>
          <ul className="compactList">
            {node.commonMisconceptions.map((item) => (
              <li key={item}>
                <MathMarkdown>{item}</MathMarkdown>
              </li>
            ))}
          </ul>
        </div>
      </div>

      <SourceAnchors node={node} />
    </div>
  )
}

function PracticePanel({
  items,
  onPassed,
  passedPracticeIds,
}: {
  items: PracticeItem[]
  onPassed: (practiceId: string) => void
  passedPracticeIds: string[]
}) {
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({})

  if (!items.length) {
    return (
      <div className="emptyState">
        <h2>No practice yet</h2>
        <p>This node needs an authored check before it can become mastery-gated.</p>
      </div>
    )
  }

  return (
    <div className="practiceStack">
      {items.map((item) => {
        const selected = item.choices.find((choice) => choice.id === selectedAnswers[item.id])
        const passed = passedPracticeIds.includes(item.id)

        return (
          <article className="practiceItem" key={item.id}>
            <span className="practiceKind">{passed ? 'passed' : item.kind}</span>
            <div className="practicePrompt">
              <MathMarkdown>{item.prompt}</MathMarkdown>
            </div>
            <div className="choiceStack">
              {item.choices.map((choice) => (
                <button
                  aria-label={choice.text.replaceAll('$', '')}
                  className={selectedAnswers[item.id] === choice.id ? 'choice selected' : 'choice'}
                  key={choice.id}
                  onClick={() => {
                    setSelectedAnswers((current) => ({ ...current, [item.id]: choice.id }))
                    if (choice.correct) onPassed(item.id)
                  }}
                  type="button"
                >
                  <MathMarkdown>{choice.text}</MathMarkdown>
                </button>
              ))}
            </div>
            {selected ? (
              <div className={selected.correct ? 'feedbackCorrect' : 'feedbackWrong'}>
                <MathMarkdown>{selected.feedback}</MathMarkdown>
              </div>
            ) : null}
          </article>
        )
      })}
    </div>
  )
}

function DiagnosticPanel({
  answers,
  onAnswer,
  onScore,
  result,
}: {
  answers: DiagnosticAnswers
  onAnswer: (questionId: string, answer: string) => void
  onScore: () => void
  result: DiagnosticResult | null
}) {
  return (
    <div className="diagnosticPanel">
      <div className="panelTitleRow">
        <Route aria-hidden />
        <div>
          <h2>Placement Diagnostic</h2>
          <p>Fast checks identify the first repair node before the attention route.</p>
        </div>
      </div>

      <div className="diagnosticList">
        {course.diagnosticQuestions.map((question) => (
          <fieldset className="diagnosticItem" key={question.id}>
            <legend>{question.prompt}</legend>
            {question.options.map((option) => (
              <label key={option.value}>
                <input
                  checked={answers[question.id] === option.value}
                  name={question.id}
                  onChange={() => onAnswer(question.id, option.value)}
                  type="radio"
                />
                <span>{option.label}</span>
              </label>
            ))}
          </fieldset>
        ))}
      </div>

      <div className="actionRow">
        <button className="primaryAction" onClick={onScore} type="button">
          Score Diagnostic
        </button>
        <button
          className="secondaryAction"
          onClick={() => {
            for (const [questionId, value] of Object.entries(selectedDiagnosticAnswers())) {
              onAnswer(questionId, value)
            }
          }}
          type="button"
        >
          Fill Experienced Path
        </button>
      </div>

      {result ? (
        <div className="resultPanel">
          <strong className={result.readiness === 'ready_for_attention_core' ? 'statusReady' : 'statusRepair'}>
            {readinessLabel(result)}
          </strong>
          <p>
            Score: {result.score}/{result.total}
          </p>
          {result.repairNodeIds.length ? (
            <ul className="compactList">
              {result.repairNodeIds.map((nodeId) => (
                <li key={nodeId}>{nodeById(course, nodeId).title}</li>
              ))}
            </ul>
          ) : (
            <p>The foundation checks are strong enough to start the main route.</p>
          )}
        </div>
      ) : null}
    </div>
  )
}

function AttentionLab() {
  const tokens = ['animal', 'slept', 'because', 'tired']
  const tokenVectors: Record<string, number[]> = {
    animal: [1.0, 0.2, 0.1],
    slept: [0.4, 0.6, 0.9],
    because: [0.1, 0.8, 0.2],
    tired: [0.2, 0.7, 1.0],
  }
  const wq = [
    [0.8, 0.1, 0.2],
    [0.0, 0.7, 0.4],
  ]
  const wk = [
    [0.6, 0.3, 0.1],
    [0.2, 0.4, 0.8],
  ]
  const wv = [
    [0.5, 0.2, 0.1],
    [0.1, 0.3, 0.7],
  ]
  const [queryToken, setQueryToken] = useState('slept')
  const [maskFuture, setMaskFuture] = useState(false)
  const [prediction, setPrediction] = useState('animal')
  const [revealed, setRevealed] = useState(false)
  const queryIndex = tokens.indexOf(queryToken)
  const query = project(wq, tokenVectors[queryToken])
  const keys = tokens.map((token) => project(wk, tokenVectors[token]))
  const values = tokens.map((token) => project(wv, tokenVectors[token]))
  const rawScores = keys.map((key, index) => {
    if (maskFuture && index > queryIndex) return Number.NEGATIVE_INFINITY
    return dot(key, query) / Math.sqrt(query.length)
  })
  const shares = softmax(rawScores.map((score) => (Number.isFinite(score) ? score : -1000)))
  const output = values[0].map((_, featureIndex) =>
    shares.reduce((sum, share, tokenIndex) => sum + share * values[tokenIndex][featureIndex], 0),
  )
  const weightedContributions = values.map((valueVector, tokenIndex) =>
    valueVector.map((value) => shares[tokenIndex] * value),
  )
  const maxShareIndex = shares.reduce((bestIndex, share, index) => (share > shares[bestIndex] ? index : bestIndex), 0)

  return (
    <div className="labPanel" data-testid="attention-lab">
      <div className="panelTitleRow">
        <Beaker aria-hidden />
        <div>
          <h2>Attention Lab</h2>
          <p>Predict one attention row, then reveal Q/K/V scores, shares, and the mixed value output.</p>
        </div>
      </div>

      <EquationBlock equation={'\\mathbf{y}_n=\\sum_m \\mathrm{softmax}_m(\\mathbf{k}_m^T\\mathbf{q}_n/\\sqrt{D_q})\\mathbf{v}_m'} />

      <div className="conceptPanel">
        <span>Lab Goal</span>
        <h3>Follow one token from input vector to mixed output.</h3>
        <p>
          A token starts as an input vector <strong>x</strong>. The lab builds an asking vector <strong>q</strong>,
          matching vectors <strong>k</strong>, and value vectors <strong>v</strong>. Scores become shares, and shares
          mix the values into the output vector.
        </p>
      </div>

      <div className="controlGrid">
        <label className="controlLabel">
          Query token
          <select
            onChange={(event) => {
              setQueryToken(event.target.value)
              setRevealed(false)
            }}
            value={queryToken}
          >
            {tokens.map((token) => (
              <option key={token} value={token}>
                {token}
              </option>
            ))}
          </select>
        </label>
        <label className="controlLabel">
          Predict largest share
          <select
            onChange={(event) => {
              setPrediction(event.target.value)
              setRevealed(false)
            }}
            value={prediction}
          >
            {tokens.map((token) => (
              <option key={token} value={token}>
                {token}
              </option>
            ))}
          </select>
        </label>
      </div>

      <label className="toggleRow">
        <input
          checked={maskFuture}
          onChange={(event) => {
            setMaskFuture(event.target.checked)
            setRevealed(false)
          }}
          type="checkbox"
        />
        <span>Mask future tokens</span>
      </label>

      <button className="primaryAction" onClick={() => setRevealed(true)} type="button">
        Reveal Row
      </button>

      {revealed ? (
        <>
          <p className={tokens[maxShareIndex] === prediction ? 'feedbackCorrect' : 'feedbackWrong'}>
            Largest share: {tokens[maxShareIndex]}. Your prediction: {prediction}.
          </p>
          <div className="attentionTable" role="table" aria-label="Attention shares">
            <div className="tableRow header" role="row">
              <span role="columnheader">Token</span>
              <span role="columnheader">Score</span>
              <span role="columnheader">Share</span>
              <span role="columnheader">Value</span>
            </div>
            {tokens.map((token, index) => (
              <div className="tableRow" key={token} role="row">
                <span role="cell">{token}</span>
                <span role="cell">{Number.isFinite(rawScores[index]) ? rawScores[index].toFixed(2) : 'masked'}</span>
                <span role="cell">
                  <span className="shareBar" style={{ width: `${Math.max(8, shares[index] * 100)}%` }} />
                  {shares[index].toFixed(2)}
                </span>
                <span role="cell">[{values[index].map((value) => value.toFixed(2)).join(', ')}]</span>
              </div>
            ))}
          </div>
          <div className="calculationLedger">
            <span>Weighted-sum ledger</span>
            <h3>Every row contributes to the output vector.</h3>
            {tokens.map((token, index) => (
              <p key={token}>
                {token}: {shares[index].toFixed(3)} x [{values[index].map((value) => value.toFixed(2)).join(', ')}] =
                [{weightedContributions[index].map((value) => value.toFixed(3)).join(', ')}]
              </p>
            ))}
            <strong>sum = [{output.map((value) => value.toFixed(3)).join(', ')}]</strong>
          </div>
          <div className="outputVector">
            <span>Mixed output</span>
            <strong>[{output.map((value) => value.toFixed(3)).join(', ')}]</strong>
          </div>
        </>
      ) : (
        <p className="labPrompt">Choose the query token, make a prediction, then reveal the row.</p>
      )}
    </div>
  )
}

function ProjectPanel({ node }: { node: CourseNode }) {
  const projectSteps = [
    'Build `dot(a, b)` and check it on two short lists.',
    'Build `matvec(W, x)` so each token can create query, key, and value vectors.',
    'Build `softmax(scores)` and confirm the returned shares sum to 1.',
    'Build `apply_causal_mask(scores, position)` so future scores are blocked before softmax.',
    'Build `mix(shares, values)` and print the weighted-sum ledger for one output token.',
    'Run the four-token example, then explain one attention row in plain language.',
  ]

  return (
    <div className="projectPanel">
      <div className="panelTitleRow">
        <Code2 aria-hidden />
        <div>
          <h2>Tiny Masked Decoder</h2>
          <p>Capstone route from arrays to a next-token distribution.</p>
        </div>
      </div>
      <EquationBlock equation={node.equation} />

      <div className="conceptPanel">
        <span>Project Contract</span>
        <h3>Build a tiny attention router with plain Python lists.</h3>
        <p>
          The project artifact is a script that prints scores, masked scores, shares, value vectors, and mixed outputs.
          It should prove that masking happens before softmax and that attention shares mix values rather than replacing
          them.
        </p>
      </div>

      <div className="projectSteps">
        {projectSteps.map((step, index) => (
          <div className="projectStep" key={step}>
            <span>{index + 1}</span>
            <p>{step}</p>
          </div>
        ))}
      </div>

      <div className="resultPanel">
        <strong>Checks</strong>
        <ul className="compactList">
          <li>Masking happens before softmax, so future tokens get share 0.</li>
          <li>Every attention row sums to 1 after softmax.</li>
          <li>The mixed output has the same length as each value vector.</li>
          <li>The learner can explain scores versus shares versus values for one row.</li>
        </ul>
      </div>

      <pre className="codeBlock">{`tokens = ["animal", "slept", "because", "tired"]

def dot(a, b):
    return sum(left * right for left, right in zip(a, b))

def matvec(W, x):
    return [dot(row, x) for row in W]

def mix(shares, values):
    width = len(values[0])
    return [
        sum(shares[token_index] * values[token_index][feature] for token_index in range(len(values)))
        for feature in range(width)
    ]

# Next: add softmax(scores), apply_causal_mask(scores, position),
# then print the ledger for one query token before computing every row.`}</pre>
      <SourceAnchors node={node} />
    </div>
  )
}

function LearningWorkspace({
  activeMode,
  answers,
  completedNodeIds,
  diagnosticResult,
  onAnswer,
  onMarkMastered,
  onModeChange,
  onPassedPractice,
  onScore,
  passedPracticeIds,
  selectedNode,
}: {
  activeMode: PanelMode
  answers: DiagnosticAnswers
  completedNodeIds: string[]
  diagnosticResult: DiagnosticResult | null
  onAnswer: (questionId: string, answer: string) => void
  onMarkMastered: () => void
  onModeChange: (mode: PanelMode) => void
  onPassedPractice: (practiceId: string) => void
  onScore: () => void
  passedPracticeIds: string[]
  selectedNode: CourseNode
}) {
  const selectedPractice = course.practiceItems.filter((item) => selectedNode.practiceIds.includes(item.id))
  const selectedPracticePassed =
    selectedPractice.length > 0 && selectedPractice.every((item) => passedPracticeIds.includes(item.id))
  const mastered = completedNodeIds.includes(selectedNode.id)
  const ActiveIcon = panelModes.find((mode) => mode.id === activeMode)?.icon ?? BookOpen

  return (
    <section className="learningSurface">
      <div className="learningHeader">
        <div className="panelTitleRow">
          <ActiveIcon aria-hidden />
          <div>
            <h2>{selectedNode.title}</h2>
            <p>{stageLabel(selectedNode.stage)} - {selectedNode.track}</p>
          </div>
        </div>
        <button
          className={mastered ? 'masteredAction' : 'secondaryAction'}
          disabled={!selectedPracticePassed && !mastered}
          onClick={onMarkMastered}
          type="button"
        >
          {mastered ? 'Mastered' : selectedPracticePassed ? 'Mark Mastered' : 'Pass Practice First'}
        </button>
      </div>

      <nav className="modeTabs" aria-label="Learning modes">
        {panelModes.map((mode) => {
          const Icon = mode.icon
          return (
            <button
              aria-pressed={activeMode === mode.id}
              className={activeMode === mode.id ? 'active' : ''}
              key={mode.id}
              onClick={() => onModeChange(mode.id)}
              type="button"
            >
              <Icon aria-hidden />
              <span>{mode.label}</span>
            </button>
          )
        })}
      </nav>

      {activeMode === 'lesson' ? <LessonPanel node={selectedNode} /> : null}
      {activeMode === 'practice' ? (
        <PracticePanel items={selectedPractice} onPassed={onPassedPractice} passedPracticeIds={passedPracticeIds} />
      ) : null}
      {activeMode === 'diagnostic' ? (
        <DiagnosticPanel answers={answers} onAnswer={onAnswer} onScore={onScore} result={diagnosticResult} />
      ) : null}
      {activeMode === 'lab' ? <AttentionLab /> : null}
      {activeMode === 'project' ? <ProjectPanel node={nodeById(course, 'project.tiny-masked-decoder')} /> : null}
    </section>
  )
}

export function TransformerCourseApp() {
  const [activeMode, setActiveMode] = useState<PanelMode>('lesson')
  const [selectedNodeId, setSelectedNodeId] = useState('attention.weighted-sum-output')
  const [mapOpen, setMapOpen] = useState(false)
  const [answers, setAnswers] = useState<DiagnosticAnswers>({})
  const [diagnosticResult, setDiagnosticResult] = useState<DiagnosticResult | null>(null)
  const [completedNodeIds, setCompletedNodeIds] = useState<string[]>(() => readStoredList(completedNodesStorageKey))
  const [passedPracticeIds, setPassedPracticeIds] = useState<string[]>(() => readStoredList(passedPracticeStorageKey))

  const selectedNode = nodeById(course, selectedNodeId)
  const recommendation = useMemo(() => {
    if (!diagnosticResult) return null
    return nextRecommendedNode(course, buildLearnerState(diagnosticResult))
  }, [diagnosticResult])

  function handleAnswer(questionId: string, answer: string) {
    setAnswers((current) => ({ ...current, [questionId]: answer }))
  }

  function handleScore() {
    const result = gradeDiagnostic(answers)
    setDiagnosticResult(result)
    const nextNode = nextRecommendedNode(course, buildLearnerState(result))
    if (nextNode) {
      setSelectedNodeId(nextNode.id)
    }
  }

  function handlePassedPractice(practiceId: string) {
    setPassedPracticeIds((current) => {
      const next = addUnique(current, practiceId)
      writeStoredList(passedPracticeStorageKey, next)
      return next
    })
  }

  function handleMarkMastered() {
    setCompletedNodeIds((current) => {
      const next = addUnique(current, selectedNodeId)
      writeStoredList(completedNodesStorageKey, next)
      return next
    })
  }

  return (
    <main className="courseShell">
      <header className="appBar">
        <div>
          <p className="eyebrow">TorchBloom - UDL Chapter 12</p>
          <h1>{course.title}</h1>
          <p>{course.subtitle}</p>
        </div>
        <div className="targetStrip">
          <Network aria-hidden />
          <span>{course.nodes.length} graph nodes</span>
          <Layers aria-hidden />
          <span>{course.practiceItems.length} checks</span>
          <ShieldCheck aria-hidden />
          <span>{completedNodeIds.length} mastered</span>
        </div>
      </header>

      <section className="missionBar" aria-label="Current learning route">
        <div>
          <span>Target</span>
          <strong>{course.target}</strong>
        </div>
        <button
          className="recommendationButton"
          onClick={() => {
            if (recommendation) {
              setSelectedNodeId(recommendation.id)
              setActiveMode('lesson')
            } else {
              setActiveMode('diagnostic')
            }
          }}
          type="button"
        >
          <Route aria-hidden />
          {recommendation ? `Go to ${recommendation.title}` : 'Take diagnostic for route'}
        </button>
        <button className="secondaryAction" onClick={() => setMapOpen(true)} type="button">
          <MapIcon aria-hidden />
          Open Map
        </button>
      </section>

      <section className="learningStudio">
        <LearningWorkspace
          activeMode={activeMode}
          answers={answers}
          completedNodeIds={completedNodeIds}
          diagnosticResult={diagnosticResult}
          onAnswer={handleAnswer}
          onMarkMastered={handleMarkMastered}
          onModeChange={setActiveMode}
          onPassedPractice={handlePassedPractice}
          onScore={handleScore}
          passedPracticeIds={passedPracticeIds}
          selectedNode={selectedNode}
        />
      </section>

      {mapOpen ? (
        <div className="mapOverlay" role="dialog" aria-modal="true" aria-label="Course dependency map">
          <div className="mapHeader">
            <div>
              <span>Dependency Map</span>
              <h2>{selectedNode.title}</h2>
            </div>
            <button className="secondaryAction" onClick={() => setMapOpen(false)} type="button">
              <X aria-hidden />
              Close Map
            </button>
          </div>
          <GraphCanvas
            completedNodeIds={completedNodeIds}
            onSelectNode={(nodeId) => {
              setSelectedNodeId(nodeId)
              setActiveMode('lesson')
              setMapOpen(false)
            }}
            selectedNodeId={selectedNodeId}
          />
        </div>
      ) : null}
    </main>
  )
}
