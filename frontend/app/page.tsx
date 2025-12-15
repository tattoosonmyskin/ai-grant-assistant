'use client';

import { useRouter } from 'next/navigation';
import styles from './page.module.css';

export default function Home() {
  const router = useRouter();

  return (
    <div className={styles.container}>
      <main className={styles.main}>
        <h1 className={styles.title}>
          AI Grant Assistant
        </h1>
        
        <p className={styles.description}>
          AI-driven grant matching and application assistance for the empowerment of all
        </p>

        <div className={styles.grid}>
          <button
            onClick={() => router.push('/onboarding')}
            className={styles.card}
          >
            <h2>Get Started &rarr;</h2>
            <p>Create your profile and find matching grants</p>
          </button>

          <button
            onClick={() => router.push('/dashboard')}
            className={styles.card}
          >
            <h2>Dashboard &rarr;</h2>
            <p>View your grant matches and applications</p>
          </button>
        </div>

        <div className={styles.features}>
          <div className={styles.feature}>
            <h3>🎯 Smart Matching</h3>
            <p>AI-powered grant matching based on your profile</p>
          </div>
          <div className={styles.feature}>
            <h3>📄 Packet Generation</h3>
            <p>Automated document generation for applications</p>
          </div>
          <div className={styles.feature}>
            <h3>💡 Personalized Recommendations</h3>
            <p>Get grants tailored to your unique situation</p>
          </div>
        </div>
      </main>
    </div>
  );
}
