import { course } from './course-data'
import type {
  Course,
  CourseNode,
  CourseStage,
  DiagnosticAnswers,
  DiagnosticResult,
  LearnerState,
  PracticeItem,
  PracticeResult,
} from './types'

export { course }

const stageOrder: CourseStage[] = [
  'foundations',
  'attention-core',
  'transformer-block',
  'decoder-project',
  'extensions',
]

export function gradeDiagnostic(answers: DiagnosticAnswers): DiagnosticResult {
  const missedRepairNodes = course.diagnosticQuestions
    .filter((question) => answers[question.id] !== question.correctAnswer)
    .map((question) => question.repairNodeId)

  const repairNodeIds = [...new Set(missedRepairNodes)]
  const score = course.diagnosticQuestions.length - missedRepairNodes.length

  return {
    readiness: repairNodeIds.length === 0 ? 'ready_for_attention_core' : 'repair_first',
    score,
    total: course.diagnosticQuestions.length,
    repairNodeIds,
  }
}

export function buildLearnerState(result: DiagnosticResult): LearnerState {
  if (result.readiness === 'ready_for_attention_core') {
    return {
      masteredNodeIds: ['math.weighted-average', 'math.dot-product', 'prob.softmax-normalization', 'code.list-indexing'],
      repairNodeIds: [],
    }
  }

  return {
    masteredNodeIds: [],
    repairNodeIds: result.repairNodeIds,
  }
}

export function nextRecommendedNode(activeCourse: Course, state: LearnerState): CourseNode | undefined {
  const mastered = new Set(state.masteredNodeIds)
  const repairNode = state.repairNodeIds
    .map((nodeId) => activeCourse.nodes.find((node) => node.id === nodeId))
    .find((node): node is CourseNode => node !== undefined && !mastered.has(node.id))

  if (repairNode) return repairNode

  return activeCourse.nodes
    .slice()
    .sort((left, right) => stageOrder.indexOf(left.stage) - stageOrder.indexOf(right.stage))
    .find((node) => !mastered.has(node.id))
}

export function visibleGraphNodes(activeCourse: Course, stage: CourseStage): CourseNode[] {
  return activeCourse.nodes.filter((node) => node.stage === stage)
}

export function answerPracticeItem(item: PracticeItem, answerText: string): PracticeResult {
  const normalized = answerText.trim().toLowerCase()
  const selected =
    item.choices.find((choice) => choice.text.trim().toLowerCase() === normalized) ??
    item.choices.find((choice) => choice.id.trim().toLowerCase() === normalized)

  if (!selected) {
    return {
      correct: false,
      feedback: 'This answer is not one of the current choices. Try the closest precise statement.',
    }
  }

  return {
    correct: selected.correct,
    feedback: selected.feedback,
  }
}

export function nodeById(activeCourse: Course, nodeId: string): CourseNode {
  const node = activeCourse.nodes.find((candidate) => candidate.id === nodeId)
  if (!node) throw new Error(`Unknown course node: ${nodeId}`)
  return node
}

export function stageLabel(stage: CourseStage): string {
  switch (stage) {
    case 'foundations':
      return 'Foundations'
    case 'attention-core':
      return 'Attention Core'
    case 'transformer-block':
      return 'Transformer Block'
    case 'decoder-project':
      return 'Decoder Project'
    case 'extensions':
      return 'Extensions'
  }
}
