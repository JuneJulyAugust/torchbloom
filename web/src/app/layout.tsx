import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'TorchBloom Transformer Mastery',
  description: 'A graph-based Transformer course for experienced learners.',
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
