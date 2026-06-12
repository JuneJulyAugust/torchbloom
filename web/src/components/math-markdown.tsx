'use client'

import ReactMarkdown from 'react-markdown'
import rehypeKatex from 'rehype-katex'
import remarkGfm from 'remark-gfm'
import remarkMath from 'remark-math'

type MathMarkdownProps = {
  children: string
}

export function MathMarkdown({ children }: MathMarkdownProps) {
  return (
    <div className="mathMarkdown">
      <ReactMarkdown rehypePlugins={[rehypeKatex]} remarkPlugins={[remarkGfm, remarkMath]}>
        {children}
      </ReactMarkdown>
    </div>
  )
}
