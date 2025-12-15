'use client';

import { useEffect, useState } from 'react';
import { useRouter, useSearchParams } from 'next/navigation';
import { apiClient, Grant } from '@/lib/api';
import styles from './page.module.css';

export default function GrantDetail({ params }: { params: { id: string } }) {
  const router = useRouter();
  const searchParams = useSearchParams();
  const [grant, setGrant] = useState<Grant | null>(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const profileId = searchParams.get('profileId');

  useEffect(() => {
    const loadGrant = async () => {
      try {
        const grantData = await apiClient.getGrant(params.id);
        setGrant(grantData);
        setLoading(false);
      } catch (err: any) {
        setError(err.message || 'Failed to load grant');
        setLoading(false);
      }
    };

    loadGrant();
  }, [params.id]);

  const handleBack = () => {
    if (profileId) {
      router.push(`/dashboard?profileId=${profileId}`);
    } else {
      router.push('/dashboard');
    }
  };

  if (loading) {
    return (
      <div className={styles.container}>
        <div className={styles.loading}>Loading grant details...</div>
      </div>
    );
  }

  if (error || !grant) {
    return (
      <div className={styles.container}>
        <div className={styles.error}>{error || 'Grant not found'}</div>
        <button onClick={handleBack} className={styles.btnPrimary}>
          Back to Dashboard
        </button>
      </div>
    );
  }

  return (
    <div className={styles.container}>
      <div className={styles.content}>
        <button onClick={handleBack} className={styles.backButton}>
          ← Back to Dashboard
        </button>

        <div className={styles.grantCard}>
          <div className={styles.header}>
            <h1>{grant.title}</h1>
            <div className={styles.amount}>${grant.amount.toLocaleString()}</div>
          </div>

          <div className={styles.organization}>
            <strong>Organization:</strong> {grant.organization}
          </div>

          <div className={styles.deadline}>
            <strong>Application Deadline:</strong> {grant.deadline}
          </div>

          <div className={styles.section}>
            <h2>Description</h2>
            <p>{grant.description}</p>
          </div>

          <div className={styles.section}>
            <h2>Eligibility Requirements</h2>
            
            <div className={styles.requirements}>
              {grant.eligible_personas && grant.eligible_personas.length > 0 && (
                <div className={styles.requirement}>
                  <strong>Eligible Personas:</strong>
                  <div className={styles.tags}>
                    {grant.eligible_personas.map((persona, idx) => (
                      <span key={idx} className={styles.tag}>{persona}</span>
                    ))}
                  </div>
                </div>
              )}

              {grant.eligible_regions && grant.eligible_regions.length > 0 && (
                <div className={styles.requirement}>
                  <strong>Eligible Regions:</strong>
                  <div className={styles.tags}>
                    {grant.eligible_regions.map((region, idx) => (
                      <span key={idx} className={styles.tag}>{region}</span>
                    ))}
                  </div>
                </div>
              )}

              {grant.min_gpa && (
                <div className={styles.requirement}>
                  <strong>Minimum GPA:</strong> {grant.min_gpa}
                </div>
              )}

              {grant.income_requirements && grant.income_requirements.length > 0 && (
                <div className={styles.requirement}>
                  <strong>Income Requirements:</strong>
                  <div className={styles.tags}>
                    {grant.income_requirements.map((income, idx) => (
                      <span key={idx} className={styles.tag}>{income}</span>
                    ))}
                  </div>
                </div>
              )}

              {grant.requires_minority && (
                <div className={styles.requirement}>
                  <strong>Requires Minority Status:</strong> Yes
                </div>
              )}

              {grant.requires_disability && (
                <div className={styles.requirement}>
                  <strong>Requires Disability Status:</strong> Yes
                </div>
              )}
            </div>
          </div>

          {grant.url && (
            <div className={styles.section}>
              <h2>Application</h2>
              <a href={grant.url} target="_blank" rel="noopener noreferrer" className={styles.applyLink}>
                Visit Application Website →
              </a>
            </div>
          )}

          <div className={styles.actions}>
            <button onClick={handleBack} className={styles.btnSecondary}>
              Back to Dashboard
            </button>
          </div>
        </div>
      </div>
    </div>
  );
}
