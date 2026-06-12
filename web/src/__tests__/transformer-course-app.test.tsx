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
    expect(screen.getByText(/Ask Before Naming/i)).toBeInTheDocument()
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
    expect(within(lab).getByText(/mixed output/i)).toBeInTheDocument()
  })

  it('persists mastered graph nodes locally', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)
    await user.click(screen.getByRole('button', { name: /^practice$/i }))
    await user.click(screen.getByRole('button', { name: /compute one output vector/i }))
    await user.click(screen.getByRole('button', { name: /mark mastered/i }))

    expect(JSON.parse(window.localStorage.getItem('torchbloom.transformer.completedNodes') ?? '[]')).toContain(
      'attention.weighted-sum-output',
    )
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
