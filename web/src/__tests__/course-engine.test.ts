import {
  answerPracticeItem,
  buildLearnerState,
  course,
  gradeDiagnostic,
  nextRecommendedNode,
  visibleGraphNodes,
} from '@/lib/course/course-engine'

describe('Transformer course engine', () => {
  it('places an experienced learner directly into the attention core when prerequisites are strong', () => {
    const result = gradeDiagnostic({
      weightedAverage: '0.8',
      dotProduct: '11',
      softmax: 'largest-score-gets-largest-share',
      pythonIndexing: 'second-token',
      masking: 'future-tokens-zero-share',
    })

    expect(result.readiness).toBe('ready_for_attention_core')
    expect(result.repairNodeIds).toEqual([])
    expect(result.score).toBe(5)
  })

  it('routes prerequisite gaps to repair nodes before the target transformer path', () => {
    const result = gradeDiagnostic({
      weightedAverage: '0.4',
      dotProduct: '14',
      softmax: 'divide-raw-scores',
      pythonIndexing: 'first-token',
      masking: 'delete-all-old-tokens',
    })
    const state = buildLearnerState(result)

    expect(result.readiness).toBe('repair_first')
    expect(result.repairNodeIds).toContain('math.weighted-average')
    expect(result.repairNodeIds).toContain('prob.softmax-normalization')
    expect(nextRecommendedNode(course, state)?.id).toBe('math.weighted-average')
  })

  it('grades practice items with targeted feedback and keeps graph nodes visible by stage', () => {
    const item = course.practiceItems.find((practice) => practice.id === 'practice.softmax-contrast')

    expect(item).toBeDefined()
    expect(answerPracticeItem(item!, 'raw scores can be negative, so normalize positive exponentials').correct).toBe(true)
    expect(answerPracticeItem(item!, 'divide raw scores by their sum').correct).toBe(false)
    expect(visibleGraphNodes(course, 'attention-core').map((node) => node.id)).toContain('transformer.self-attention')
  })
})
