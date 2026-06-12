import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TransformerCourseApp } from '@/components/transformer-course-app'

describe('TransformerCourseApp', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('renders a lesson-centered course with the graph available as an on-demand map', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)

    expect(screen.getByRole('heading', { name: /transformer mastery course/i })).toBeInTheDocument()
    expect(screen.queryByLabelText(/transformer course knowledge graph/i)).not.toBeInTheDocument()
    expect(screen.getByText(/42 graph nodes/i)).toBeInTheDocument()
    expect(screen.getByText(/What This Output Is For/i)).toBeInTheDocument()
    expect(screen.getAllByText(/Source Anchors/i).length).toBeGreaterThan(0)

    await user.click(screen.getByRole('button', { name: /open map/i }))
    expect(screen.getByLabelText(/transformer course knowledge graph/i)).toBeInTheDocument()
    await user.click(screen.getByRole('button', { name: /close map/i }))
    expect(screen.queryByLabelText(/transformer course knowledge graph/i)).not.toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: /^diagnostic$/i }))
    await user.click(screen.getByRole('button', { name: /fill experienced path/i }))
    await user.click(screen.getByRole('button', { name: /score diagnostic/i }))

    expect(screen.getByText(/ready for attention core/i)).toBeInTheDocument()

    await user.click(screen.getByRole('button', { name: /^lab$/i }))
    const lab = screen.getByTestId('attention-lab')

    expect(within(lab).getByLabelText(/query token/i)).toBeInTheDocument()
    await user.click(within(lab).getByRole('button', { name: /reveal row/i }))
    expect(within(lab).getAllByText(/mixed output/i).length).toBeGreaterThan(0)
    expect(within(lab).getByText(/Weighted-sum ledger/i)).toBeInTheDocument()
  })

  it('persists mastered graph nodes locally', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)
    await user.click(screen.getByRole('button', { name: /^practice$/i }))
    await user.click(screen.getByRole('button', { name: /\[6\.2,7\.2\]/i }))
    await user.click(screen.getByRole('button', { name: /mark mastered/i }))

    expect(JSON.parse(window.localStorage.getItem('torchbloom.transformer.completedNodes') ?? '[]')).toContain(
      'attention.weighted-sum-output',
    )
  })

  it('teaches attention output with concrete token context and numeric computation', () => {
    const { container } = render(<TransformerCourseApp />)

    expect(screen.queryByText(/Little-style move/i)).not.toBeInTheDocument()
    expect(screen.getByText(/A token is one item in a sequence/i)).toBeInTheDocument()
    expect(screen.getByText(/We are computing a new vector for the first token/i)).toBeInTheDocument()
    expect(screen.getByText(/The output is \[6\.2, 7\.2\]/i)).toBeInTheDocument()
    expect(screen.getByText(/Because each value vector has length 2/i)).toBeInTheDocument()
    expect(container.querySelector('.equationBox .katex-display')).not.toBeNull()
  })

  it('uses authored practice that requires computing the attention mixture', async () => {
    const user = userEvent.setup()
    const { container } = render(<TransformerCourseApp />)

    await user.click(screen.getByRole('button', { name: /^practice$/i }))

    expect(screen.queryByText(/Which statement best shows mastery/i)).not.toBeInTheDocument()
    expect(screen.getByText(/Compute the new vector for token 1/i)).toBeInTheDocument()
    expect(container.querySelector('.practiceItem .katex')).not.toBeNull()
    await user.click(screen.getByRole('button', { name: /\[6\.2,7\.2\]/i }))

    expect(screen.getByText(/The attention row is not the output/i)).toBeInTheDocument()
  })

  it('presents the project as a staged plain-code build with checks', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)
    await user.click(screen.getByRole('button', { name: /^project$/i }))

    expect(screen.getByText(/Project Contract/i)).toBeInTheDocument()
    expect(screen.getByText(/Build `dot\(a, b\)`/i)).toBeInTheDocument()
    expect(screen.getAllByText(/Masking happens before softmax/i).length).toBeGreaterThan(0)
    expect(screen.getByText(/def dot\(a, b\):/i)).toBeInTheDocument()
  })

  it('renders inline math inside practice choices with KaTeX instead of literal dollar markers', async () => {
    const user = userEvent.setup()
    const { container } = render(<TransformerCourseApp />)

    await user.click(screen.getByRole('button', { name: /open map/i }))
    await user.click(screen.getByRole('button', { name: /why text breaks fully connected nets/i }))
    await user.click(screen.getByRole('button', { name: /^practice$/i }))

    expect(screen.queryByText(/Compute sequence input size as \$ND\$\./i)).not.toBeInTheDocument()
    expect(container.querySelector('.choice .katex')).not.toBeNull()
  })
})
