import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TransformerCourseApp } from '@/components/transformer-course-app'

describe('TransformerCourseApp', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('renders the graph-first course, diagnostic, and attention lab', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)

    expect(screen.getByRole('heading', { name: /transformer mastery course/i })).toBeInTheDocument()
    expect(screen.getByLabelText(/transformer course knowledge graph/i)).toBeInTheDocument()
    expect(screen.getByText(/42 graph nodes/i)).toBeInTheDocument()
    expect(screen.getByText(/Ask Before Naming/i)).toBeInTheDocument()
    expect(screen.getAllByText(/Source Anchors/i).length).toBeGreaterThan(0)

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
})
