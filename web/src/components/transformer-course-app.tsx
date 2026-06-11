'use client'

import {
  BookOpen,
  CheckCircle2,
  FlaskConical,
  GitBranch,
  Network,
  RotateCcw,
  Sigma,
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
import type { CourseNode, CourseStage, DiagnosticAnswers, DiagnosticResult } from '@/lib/course/types'

type TabId = 'graph' | 'diagnostic' | 'lesson' | 'practice' | 'attention-lab' | 'project'

const tabs: { id: TabId; label: string }[] = [
  { id: 'graph', label: 'Graph' },
  { id: 'diagnostic', label: 'Diagnostic' },
  { id: 'lesson', label: 'Lesson' },
  { id: 'practice', label: 'Practice' },
  { id: 'attention-lab', label: 'Attention Lab' },
  { id: 'project', label: 'Project' },
]

const stageColumns: CourseStage[] = [
  'foundations',
  'attention-core',
  'transformer-block',
  'decoder-project',
  'extensions',
]

const trackClassByTrack = {
  math: 'trackMath',
  probability: 'trackProbability',
  coding: 'trackCoding',
  transformers: 'trackTransformer',
  project: 'trackProject',
}

const completedNodesStorageKey = 'torchbloom.transformer.completedNodes'

function readCompletedNodeIds() {
  if (typeof window === 'undefined') return []

  try {
    const stored = window.localStorage.getItem(completedNodesStorageKey)
    const parsed = stored ? JSON.parse(stored) : []
    return Array.isArray(parsed) ? parsed.filter((value): value is string => typeof value === 'string') : []
  } catch {
    return []
  }
}

function writeCompletedNodeIds(nodeIds: string[]) {
  if (typeof window === 'undefined') return
  window.localStorage.setItem(completedNodesStorageKey, JSON.stringify(nodeIds))
}

function readinessLabel(result: DiagnosticResult) {
  return result.readiness === 'ready_for_attention_core' ? 'Ready for attention core' : 'Repair first'
}

function selectedDiagnosticAnswers(): DiagnosticAnswers {
  return Object.fromEntries(course.diagnosticQuestions.map((question) => [question.id, question.correctAnswer]))
}

function tokenFeatures(token: string) {
  const features: Record<string, number[]> = {
    animal: [1.0, 0.2, 0.1],
    slept: [0.4, 0.6, 0.9],
    because: [0.1, 0.8, 0.2],
    tired: [0.2, 0.7, 1.0],
  }

  return features[token] ?? [0.3, 0.3, 0.3]
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

function GraphPanel({
  completedNodeIds,
  onSelectNode,
  selectedNodeId,
}: {
  completedNodeIds: string[]
  onSelectNode: (nodeId: string) => void
  selectedNodeId: string
}) {
  const completed = new Set(completedNodeIds)

  return (
    <section className="workspaceGrid">
      <div className="graphSurface" aria-label="Transformer course knowledge graph">
        {stageColumns.map((stage) => (
          <div className="graphColumn" key={stage}>
            <div className="stageHeader">{stageLabel(stage)}</div>
            <div className="nodeStack">
              {course.nodes
                .filter((node) => node.stage === stage)
                .map((node) => (
                  <button
                    className={`graphNode ${trackClassByTrack[node.track]} ${
                      selectedNodeId === node.id ? 'selected' : ''
                    }`}
                    key={node.id}
                    onClick={() => onSelectNode(node.id)}
                    type="button"
                  >
                    <span>{completed.has(node.id) ? <CheckCircle2 aria-hidden /> : <GitBranch aria-hidden />}</span>
                    <strong>{node.title}</strong>
                    <small>{node.track}</small>
                  </button>
                ))}
            </div>
          </div>
        ))}
      </div>

      <NodeDetail node={nodeById(course, selectedNodeId)} />
    </section>
  )
}

function NodeDetail({ node }: { node: CourseNode }) {
  return (
    <aside className="nodeDetail">
      <div className="panelTitleRow">
        <Network aria-hidden />
        <div>
          <h2>{node.title}</h2>
          <p>{stageLabel(node.stage)} - {node.track}</p>
        </div>
      </div>
      <p>{node.summary}</p>
      {node.equation ? (
        <div className="equationBox">
          <span>Equation</span>
          <code>{node.equation}</code>
        </div>
      ) : null}
      <div>
        <h3>Strategic Path</h3>
        <ol className="pathList">
          {node.littlePath.map((step) => (
            <li key={step}>{step}</li>
          ))}
        </ol>
      </div>
      <div>
        <h3>Mastery Evidence</h3>
        <ul className="compactList">
          {node.masteryEvidence.map((item) => (
            <li key={item}>{item}</li>
          ))}
        </ul>
      </div>
    </aside>
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
    <section className="twoColumn">
      <div className="taskPanel">
        <div className="panelTitleRow">
          <Sigma aria-hidden />
          <div>
            <h2>Placement Diagnostic</h2>
            <p>Five checks decide whether to start at attention core or repair prerequisites first.</p>
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
      </div>

      <aside className="resultPanel">
        <h2>Recommendation</h2>
        {result ? (
          <>
            <p className={result.readiness === 'ready_for_attention_core' ? 'statusReady' : 'statusRepair'}>
              {readinessLabel(result)}
            </p>
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
              <p>Start with values, queries, keys, and one full attention row.</p>
            )}
          </>
        ) : (
          <p>Answer the checks to get a route through the graph.</p>
        )}
      </aside>
    </section>
  )
}

function LessonPanel({ node }: { node: CourseNode }) {
  const markdown = `
### ${node.title}

${node.summary}

**Current equation:** \`${node.equation ?? 'concept route'}\`

The learning move here is to make the operation visible before compressing it into notation. For this node, the strategic path is:

${node.littlePath.map((step, index) => `${index + 1}. ${step}`).join('\n')}

The Transformer chapter uses this idea as part of:

\`\`\`text
A = softmax(QK^T / sqrt(d_k))V
\`\`\`
`

  return (
    <section className="lessonSurface">
      <div className="panelTitleRow">
        <BookOpen aria-hidden />
        <div>
          <h2>Lesson Frame</h2>
          <p>A compact Little-style walkthrough for the selected graph node.</p>
        </div>
      </div>
      <MathMarkdown>{markdown}</MathMarkdown>
    </section>
  )
}

function PracticePanel({ selectedNodeId }: { selectedNodeId: string }) {
  const [selectedAnswers, setSelectedAnswers] = useState<Record<string, string>>({})
  const items = course.practiceItems.filter((item) => item.nodeId === selectedNodeId)

  if (!items.length) {
    return (
      <section className="taskPanel">
        <h2>Practice</h2>
        <p>Select another graph node to practice, or continue to the project route.</p>
      </section>
    )
  }

  return (
    <section className="practiceGrid">
      {items.map((item) => {
        const selected = item.choices.find((choice) => choice.id === selectedAnswers[item.id])

        return (
          <article className="practiceItem" key={item.id}>
            <span className="practiceKind">{item.kind}</span>
            <h2>{item.prompt}</h2>
            <div className="choiceStack">
              {item.choices.map((choice) => (
                <button
                  className={selectedAnswers[item.id] === choice.id ? 'choice selected' : 'choice'}
                  key={choice.id}
                  onClick={() => setSelectedAnswers((current) => ({ ...current, [item.id]: choice.id }))}
                  type="button"
                >
                  {choice.text}
                </button>
              ))}
            </div>
            {selected ? (
              <p className={selected.correct ? 'feedbackCorrect' : 'feedbackWrong'}>{selected.feedback}</p>
            ) : null}
          </article>
        )
      })}
    </section>
  )
}

function AttentionLab() {
  const tokens = ['animal', 'slept', 'because', 'tired']
  const [queryToken, setQueryToken] = useState('slept')
  const [maskFuture, setMaskFuture] = useState(false)
  const queryIndex = tokens.indexOf(queryToken)
  const query = tokenFeatures(queryToken)
  const rawScores = tokens.map((token, index) => {
    if (maskFuture && index > queryIndex) return Number.NEGATIVE_INFINITY
    return dot(query, tokenFeatures(token))
  })
  const safeScores = rawScores.map((score) => (Number.isFinite(score) ? score : -1000))
  const shares = softmax(safeScores)

  return (
    <section className="twoColumn" data-testid="attention-lab">
      <div className="taskPanel">
        <div className="panelTitleRow">
          <FlaskConical aria-hidden />
          <div>
            <h2>Attention Lab</h2>
            <p>Inspect one query row. Toggle masking to see why decoders cannot look ahead.</p>
          </div>
        </div>

        <label className="controlLabel">
          Query token
          <select onChange={(event) => setQueryToken(event.target.value)} value={queryToken}>
            {tokens.map((token) => (
              <option key={token} value={token}>
                {token}
              </option>
            ))}
          </select>
        </label>

        <label className="toggleRow">
          <input checked={maskFuture} onChange={(event) => setMaskFuture(event.target.checked)} type="checkbox" />
          <span>Mask future tokens</span>
        </label>

        <div className="equationBox">
          <span>Attention row</span>
          <code>A = softmax(QK^T / sqrt(d_k))V</code>
        </div>
      </div>

      <div className="matrixPanel">
        <h2>Attention Shares</h2>
        <div className="attentionTable" role="table" aria-label="Attention shares">
          <div className="tableRow header" role="row">
            <span role="columnheader">Token</span>
            <span role="columnheader">Score</span>
            <span role="columnheader">Share</span>
          </div>
          {tokens.map((token, index) => (
            <div className="tableRow" key={token} role="row">
              <span role="cell">{token}</span>
              <span role="cell">{Number.isFinite(rawScores[index]) ? rawScores[index].toFixed(2) : 'masked'}</span>
              <span role="cell">
                <span className="shareBar" style={{ width: `${Math.max(8, shares[index] * 100)}%` }} />
                {shares[index].toFixed(2)}
              </span>
            </div>
          ))}
        </div>
      </div>
    </section>
  )
}

function ProjectPanel() {
  return (
    <section className="projectSurface">
      <div className="panelTitleRow">
        <RotateCcw aria-hidden />
        <div>
          <h2>Tiny Attention Router</h2>
          <p>The MVP project turns the graph into a from-scratch implementation route.</p>
        </div>
      </div>
      <div className="projectSteps">
        {[
          'Tokenize a tiny sentence.',
          'Write token vectors as short Python lists.',
          'Compute Q, K, and V with small fixed matrices.',
          'Compute one attention row by hand, then in code.',
          'Add the decoder mask before softmax.',
          'Explain one generated next-token choice.',
        ].map((step, index) => (
          <div className="projectStep" key={step}>
            <span>{index + 1}</span>
            <p>{step}</p>
          </div>
        ))}
      </div>
    </section>
  )
}

export function TransformerCourseApp() {
  const [activeTab, setActiveTab] = useState<TabId>('graph')
  const [selectedNodeId, setSelectedNodeId] = useState('transformer.self-attention')
  const [answers, setAnswers] = useState<DiagnosticAnswers>({})
  const [diagnosticResult, setDiagnosticResult] = useState<DiagnosticResult | null>(null)
  const [completedNodeIds, setCompletedNodeIds] = useState<string[]>(readCompletedNodeIds)

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
    if (result.readiness === 'ready_for_attention_core') {
      setSelectedNodeId('transformer.qkv')
    }
  }

  return (
    <main className="courseShell">
      <header className="courseHeader">
        <div>
          <p className="eyebrow">TorchBloom MVP - UDL Chapter 12</p>
          <h1>Transformer Mastery Course</h1>
          <p>{course.subtitle}</p>
        </div>
        <div className="targetPanel">
          <span>Target</span>
          <strong>{course.target}</strong>
        </div>
      </header>

      <section className="routeBar" aria-label="Current learning route">
        <div>
          <span>Selected node</span>
          <strong>{selectedNode.title}</strong>
        </div>
        <div>
          <span>Recommended next</span>
          <strong>{recommendation?.title ?? 'Take diagnostic'}</strong>
        </div>
        <button
          className="secondaryAction"
          onClick={() =>
            setCompletedNodeIds((current) => {
              const next = current.includes(selectedNodeId) ? current : [...current, selectedNodeId]
              writeCompletedNodeIds(next)
              return next
            })
          }
          type="button"
        >
          Mark Mastered
        </button>
      </section>

      <nav className="tabBar" aria-label="Course sections">
        {tabs.map((tab) => (
          <button
            aria-selected={activeTab === tab.id}
            className={activeTab === tab.id ? 'active' : ''}
            key={tab.id}
            onClick={() => setActiveTab(tab.id)}
            role="tab"
            type="button"
          >
            {tab.label}
          </button>
        ))}
      </nav>

      {activeTab === 'graph' ? (
        <GraphPanel completedNodeIds={completedNodeIds} onSelectNode={setSelectedNodeId} selectedNodeId={selectedNodeId} />
      ) : null}
      {activeTab === 'diagnostic' ? (
        <DiagnosticPanel answers={answers} onAnswer={handleAnswer} onScore={handleScore} result={diagnosticResult} />
      ) : null}
      {activeTab === 'lesson' ? <LessonPanel node={selectedNode} /> : null}
      {activeTab === 'practice' ? <PracticePanel selectedNodeId={selectedNodeId} /> : null}
      {activeTab === 'attention-lab' ? <AttentionLab /> : null}
      {activeTab === 'project' ? <ProjectPanel /> : null}
    </main>
  )
}
