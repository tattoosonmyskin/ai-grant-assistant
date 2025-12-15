/**
 * Root Layout Component
 * 
 * This component wraps all pages in the application.
 * It sets up the HTML structure, metadata, and global styles.
 */

import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'AI Grant Assistant',
  description: 'AI-powered platform for finding and applying to grants',
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
