'use client';

import { useEffect, useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { apiClient, MatchResult, Profile } from '@/lib/api';
import styles from './page.module.css';

export default function Dashboard() {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [profile, setProfile] = useState<Profile | null>(null);
  const [matches, setMatches] = useState<MatchResult[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const loadData = async () => {
      try {
        // Get profile ID from URL or localStorage
        let profileId = searchParams.get('profileId');
        
        if (!profileId) {
          profileId = localStorage.getItem('profileId');
        }

        if (!profileId) {
          router.push('/onboarding');
          return;
        }

        // Store in localStorage for future use
        localStorage.setItem('profileId', profileId);

        // Load profile
        const profileData = await apiClient.getProfile(profileId);
        setProfile(profileData);

        // Load or refresh matches
        const matchResults = await apiClient.refreshMatches(profileId, 5);
        setMatches(matchResults);

        setLoading(false);
      } catch (err: any) {
        setError(err.message || 'Failed to load data');
        setLoading(false);
      }
    };

    loadData();
  }, [searchParams, router]);

  const handleViewGrant = (grantId: string) => {
    router.push(`/grants/${grantId}?profileId=${profile?.id}`);
  };

  const handleGeneratePacket = () => {
    if (profile && matches.length > 0) {
      router.push(`/packets?profileId=${profile.id}`);
    }
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading your dashboard...</div>
      </div>
    );
  }

  if (error) {
    return (
      <div className={styles.container}>
        <div className={styles.error}>{error}</div>
        <button onClick={() => router.push('/onboarding')} className={styles.btnPrimary}>
          Start Over
        </button>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <header className={styles.header}>
        <h1>Welcome, {profile?.name}!</h1>
        <p>Here are your top grant matches</p>
      </header>

      <div className={styles.content}>
        <div className={styles.profileCard}>
          <h2>Your Profile</h2>
          <div className={styles.profileInfo}>
            <p><strong>Persona:</strong> {profile?.persona}</p>
            <p><strong>Region:</strong> {profile?.region}</p>
            {profile?.gpa && <p><strong>GPA:</strong> {profile.gpa}</p>}
            <p><strong>Income Level:</strong> {profile?.income_level}</p>
          </div>
        </div>

        <div className={styles.matchesSection}>
          <div className={styles.matchesHeader}>
            <h2>Top {matches.length} Grant Matches</h2>
            {matches.length > 0 && (
              <button onClick={handleGeneratePacket} className={styles.btnPrimary}>
                Generate Application Packet
              </button>
            )}
          </div>

          {matches.length === 0 ? (
            <div className={styles.noMatches}>
              <p>No grants match your profile at this time.</p>
              <p>Check back later for new opportunities!</p>
            </div>
          ) : (
            <div className={styles.matchesList}>
              {matches.map((result, index) => (
                <div key={result.grant.id} className={styles.matchCard}>
                  <div className={styles.matchHeader}>
                    <div className={styles.matchRank}>#{index + 1}</div>
                    <div className={styles.matchScore}>
                      Match: {result.match.score.toFixed(0)}%
                    </div>
                  </div>
                  
                  <h3>{result.grant.title}</h3>
                  
                  <div className={styles.grantInfo}>
                    <p className={styles.organization}>{result.grant.organization}</p>
                    <p className={styles.amount}>${result.grant.amount.toLocaleString()}</p>
                    <p className={styles.deadline}>Deadline: {result.grant.deadline}</p>
                  </div>

                  <p className={styles.description}>{result.grant.description}</p>

                  <div className={styles.explanation}>
                    <strong>Why this matches:</strong>
                    <p>{result.match.explanation}</p>
                  </div>

                  <button
                    onClick={() => handleViewGrant(result.grant.id!)}
                    className={styles.btnSecondary}
                  >
                    View Details
                  </button>
                </div>
              ))}
            </div>
          )}
        </div>
      </div>
    </div>
  );
}
