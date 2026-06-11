export type CourseStage =
  | 'problem-framing'
  | 'text-pipeline'
  | 'attention-mechanics'
  | 'transformer-layer'
  | 'model-architectures'
  | 'scale-and-variants'
  | 'capstone'

export type CourseTrack =
  | 'math'
  | 'probability'
  | 'coding'
  | 'nlp'
  | 'attention'
  | 'architecture'
  | 'training'
  | 'systems'
  | 'vision'
  | 'project'

export type LessonSection = {
  title: string
  body: string
}

export type CourseNode = {
  id: string
  title: string
  track: CourseTrack
  stage: CourseStage
  summary: string
  sourceAnchors: string[]
  prerequisites: string[]
  equation?: string
  graph: {
    x: number
    y: number
  }
  lesson: LessonSection[]
  littlePath: string[]
  masteryEvidence: string[]
  commonMisconceptions: string[]
  practiceIds: string[]
}

export type DiagnosticQuestion = {
  id: string
  prompt: string
  correctAnswer: string
  repairNodeId: string
  options: {
    value: string
    label: string
  }[]
}

export type DiagnosticAnswers = Record<string, string>

export type DiagnosticResult = {
  readiness: 'ready_for_attention_core' | 'repair_first'
  score: number
  total: number
  repairNodeIds: string[]
}

export type PracticeItem = {
  id: string
  nodeId: string
  kind: 'compute' | 'shape' | 'explain' | 'debug' | 'transfer'
  prompt: string
  choices: {
    id: string
    text: string
    correct: boolean
    feedback: string
  }[]
}

export type PracticeResult = {
  correct: boolean
  feedback: string
}

export type LearnerState = {
  masteredNodeIds: string[]
  repairNodeIds: string[]
}

export type Course = {
  id: string
  title: string
  subtitle: string
  target: string
  nodes: CourseNode[]
  diagnosticQuestions: DiagnosticQuestion[]
  practiceItems: PracticeItem[]
}
