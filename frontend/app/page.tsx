/**
 * Home Page (Index Page)
 * 
 * This is the landing page of the AI Grant Assistant application.
 * When users visit the site, this is the first page they see.
 * 
 * The 'use client' directive tells Next.js this is a Client Component,
 * which means it can use React hooks and browser APIs.
 */
'use client'

import styles from './page.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          Welcome to AI Grant Assistant
        </h1>
        
        <p className={styles.description}>
          Your AI-powered platform for finding and applying to grants
        </p>

        <div className={styles.grid}>
          <a href="/onboarding" className={styles.card}>
            <h2>Get Started &rarr;</h2>
            <p>Create your profile and find matching grants</p>
          </a>

          <a href="/dashboard" className={styles.card}>
            <h2>Dashboard &rarr;</h2>
            <p>View your top grant matches and applications</p>
          </a>

          <a href="/grants" className={styles.card}>
            <h2>Browse Grants &rarr;</h2>
            <p>Explore all available grant opportunities</p>
          </a>

          <a href="/packets" className={styles.card}>
            <h2>My Packets &rarr;</h2>
            <p>Manage your grant application documents</p>
          </a>
        </div>
      </main>

      <footer className={styles.footer}>
        <p>AI Grant Assistant - Empowering all through accessible grant opportunities</p>
      </footer>
    </div>
  )
}
