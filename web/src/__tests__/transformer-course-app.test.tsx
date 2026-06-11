import { render, screen, within } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import { TransformerCourseApp } from '@/components/transformer-course-app'

describe('TransformerCourseApp', () => {
  beforeEach(() => {
    window.localStorage.clear()
  })

  it('renders the course graph, equation panel, diagnostic, and attention lab', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)

    expect(screen.getByRole('heading', { name: /transformer mastery course/i })).toBeInTheDocument()
    expect(screen.getByRole('tab', { name: /graph/i })).toBeInTheDocument()
    expect(screen.getAllByText(/softmax/i).length).toBeGreaterThan(0)
    expect(screen.getByText(/A = softmax/i)).toBeInTheDocument()

    await user.click(screen.getByRole('tab', { name: /diagnostic/i }))
    await user.click(screen.getByLabelText(/weighted average: 2.6/i))
    await user.click(screen.getByLabelText(/dot product: 11/i))
    await user.click(screen.getByLabelText(/softmax assigns/i))
    await user.click(screen.getByLabelText(/tokens\[1\] returns "learn"/i))
    await user.click(screen.getByLabelText(/future tokens get zero attention share/i))
    await user.click(screen.getByRole('button', { name: /score diagnostic/i }))

    expect(screen.getByText(/ready for attention core/i)).toBeInTheDocument()

    await user.click(screen.getByRole('tab', { name: /attention lab/i }))
    const lab = screen.getByTestId('attention-lab')

    expect(within(lab).getByText(/query token/i)).toBeInTheDocument()
    expect(within(lab).getByText(/attention shares/i)).toBeInTheDocument()
  })

  it('persists mastered graph nodes locally', async () => {
    const user = userEvent.setup()

    render(<TransformerCourseApp />)
    await user.click(screen.getByRole('button', { name: /mark mastered/i }))

    expect(JSON.parse(window.localStorage.getItem('torchbloom.transformer.completedNodes') ?? '[]')).toContain(
      'transformer.self-attention',
    )
  })
})
