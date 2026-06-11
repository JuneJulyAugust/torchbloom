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
      shape: '37888',
      dotProduct: '11',
      softmax: 'positive-shares',
      tokenIndexing: 'learn',
      embeddingLookup: 'embedding-column',
      position: 'order-not-visible',
      scaledAttention: 'before-softmax',
      masking: 'negative-infinity',
      crossAttention: 'encoder',
    })

    expect(result.readiness).toBe('ready_for_attention_core')
    expect(result.repairNodeIds).toEqual([])
    expect(result.score).toBe(9)
  })

  it('routes prerequisite gaps to repair nodes before the target transformer path', () => {
    const result = gradeDiagnostic({
      shape: '1061',
      dotProduct: '14',
      softmax: 'raw-division',
      tokenIndexing: 'we',
      embeddingLookup: 'all-embeddings-average',
      position: 'reduce-vocab',
      scaledAttention: 'after-softmax',
      masking: 'double-them',
      crossAttention: 'decoder-future',
    })
    const state = buildLearnerState(result)

    expect(result.readiness).toBe('repair_first')
    expect(result.repairNodeIds).toContain('problem.variable-length-text')
    expect(result.repairNodeIds).toContain('prob.softmax-normalization')
    expect(nextRecommendedNode(course, state)?.id).toBe('problem.variable-length-text')
  })

  it('grades practice items with targeted feedback and keeps graph nodes visible by stage', () => {
    const item = course.practiceItems.find((practice) => practice.id === 'practice.prob.softmax-normalization')

    expect(item).toBeDefined()
    expect(answerPracticeItem(item!, item!.choices[0].text).correct).toBe(true)
    expect(answerPracticeItem(item!, item!.choices[1].text).correct).toBe(false)
    expect(visibleGraphNodes(course, 'attention-mechanics').map((node) => node.id)).toContain(
      'attention.weighted-sum-output',
    )
  })
})
