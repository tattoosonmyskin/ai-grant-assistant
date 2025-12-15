import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AI Grant Assistant',
  description: 'AI-driven grant assistant for the empowerment of all',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  )
}
