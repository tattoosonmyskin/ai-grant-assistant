'use client';

import { useState } from 'react';
import { useRouter } from 'next/navigation';
import { apiClient, Profile } from '@/lib/api';
import styles from './page.module.css';

export default function Onboarding() {
  const router = useRouter();
  const [step, setStep] = useState(1);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const [formData, setFormData] = useState<Partial<Profile>>({
    name: '',
    email: '',
    persona: 'student',
    region: '',
    gpa: undefined,
    is_minority: false,
    has_disability: false,
    income_level: 'medium',
  });

  const handleInputChange = (e: React.ChangeEvent<HTMLInputElement | HTMLSelectElement>) => {
    const { name, value, type } = e.target;
    
    if (type === 'checkbox') {
      const checked = (e.target as HTMLInputElement).checked;
      setFormData(prev => ({ ...prev, [name]: checked }));
    } else if (name === 'gpa') {
      const gpaValue = value === '' ? undefined : parseFloat(value);
      setFormData(prev => ({ ...prev, [name]: gpaValue }));
    } else {
      setFormData(prev => ({ ...prev, [name]: value }));
    }
  };

  const handleNext = () => {
    setError('');
    
    // Validation for step 1
    if (step === 1) {
      if (!formData.name || !formData.email) {
        setError('Please fill in all required fields');
        return;
      }
    }
    
    // Validation for step 2
    if (step === 2) {
      if (!formData.region) {
        setError('Please select your region');
        return;
      }
    }
    
    setStep(step + 1);
  };

  const handleBack = () => {
    setError('');
    setStep(step - 1);
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');
    setLoading(true);

    try {
      // Create profile
      const profile = await apiClient.createProfile(formData as Profile);
      
      // Store profile ID in localStorage for later use
      localStorage.setItem('profileId', profile.id!);
      
      // Redirect to dashboard
      router.push(`/dashboard?profileId=${profile.id}`);
    } catch (err: any) {
      setError(err.message || 'Failed to create profile');
      setLoading(false);
    }
  };

  return (
    <div className={styles.container}>
      <div className={styles.card}>
        <h1 className={styles.title}>Create Your Profile</h1>
        
        <div className={styles.progress}>
          <div 
            className={styles.progressBar} 
            style={{ width: `${(step / 3) * 100}%` }}
          />
        </div>

        <p className={styles.stepIndicator}>Step {step} of 3</p>

        {error && <div className={styles.error}>{error}</div>}

        <form onSubmit={handleSubmit} className={styles.form}>
          {step === 1 && (
            <div className={styles.step}>
              <h2>Personal Information</h2>
              
              <div className={styles.formGroup}>
                <label htmlFor="name">Full Name *</label>
                <input
                  type="text"
                  id="name"
                  name="name"
                  value={formData.name}
                  onChange={handleInputChange}
                  required
                  placeholder="John Doe"
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="email">Email Address *</label>
                <input
                  type="email"
                  id="email"
                  name="email"
                  value={formData.email}
                  onChange={handleInputChange}
                  required
                  placeholder="john@example.com"
                />
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="persona">I am a... *</label>
                <select
                  id="persona"
                  name="persona"
                  value={formData.persona}
                  onChange={handleInputChange}
                  required
                >
                  <option value="student">Student</option>
                  <option value="researcher">Researcher</option>
                  <option value="entrepreneur">Entrepreneur</option>
                </select>
              </div>
            </div>
          )}

          {step === 2 && (
            <div className={styles.step}>
              <h2>Location & Education</h2>
              
              <div className={styles.formGroup}>
                <label htmlFor="region">Region/State *</label>
                <select
                  id="region"
                  name="region"
                  value={formData.region}
                  onChange={handleInputChange}
                  required
                >
                  <option value="">Select a region</option>
                  <option value="California">California</option>
                  <option value="New York">New York</option>
                  <option value="Texas">Texas</option>
                  <option value="Florida">Florida</option>
                  <option value="Illinois">Illinois</option>
                  <option value="Pennsylvania">Pennsylvania</option>
                  <option value="Ohio">Ohio</option>
                  <option value="Georgia">Georgia</option>
                  <option value="North Carolina">North Carolina</option>
                  <option value="Michigan">Michigan</option>
                  <option value="Washington">Washington</option>
                  <option value="Massachusetts">Massachusetts</option>
                </select>
              </div>

              <div className={styles.formGroup}>
                <label htmlFor="gpa">GPA (optional)</label>
                <input
                  type="number"
                  id="gpa"
                  name="gpa"
                  value={formData.gpa || ''}
                  onChange={handleInputChange}
                  step="0.01"
                  min="0"
                  max="4.0"
                  placeholder="3.5"
                />
                <small>Leave blank if not applicable</small>
              </div>
            </div>
          )}

          {step === 3 && (
            <div className={styles.step}>
              <h2>Additional Information</h2>
              
              <div className={styles.formGroup}>
                <label htmlFor="income_level">Income Level *</label>
                <select
                  id="income_level"
                  name="income_level"
                  value={formData.income_level}
                  onChange={handleInputChange}
                  required
                >
                  <option value="low">Low Income</option>
                  <option value="medium">Medium Income</option>
                  <option value="high">High Income</option>
                </select>
              </div>

              <div className={styles.checkboxGroup}>
                <label>
                  <input
                    type="checkbox"
                    name="is_minority"
                    checked={formData.is_minority}
                    onChange={handleInputChange}
                  />
                  <span>I identify as a minority</span>
                </label>
              </div>

              <div className={styles.checkboxGroup}>
                <label>
                  <input
                    type="checkbox"
                    name="has_disability"
                    checked={formData.has_disability}
                    onChange={handleInputChange}
                  />
                  <span>I have a disability</span>
                </label>
              </div>

              <p className={styles.note}>
                This information helps us find the most relevant grants for you.
              </p>
            </div>
          )}

          <div className={styles.buttons}>
            {step > 1 && (
              <button
                type="button"
                onClick={handleBack}
                className={styles.btnSecondary}
                disabled={loading}
              >
                Back
              </button>
            )}
            
            {step < 3 ? (
              <button
                type="button"
                onClick={handleNext}
                className={styles.btnPrimary}
              >
                Next
              </button>
            ) : (
              <button
                type="submit"
                className={styles.btnPrimary}
                disabled={loading}
              >
                {loading ? 'Creating Profile...' : 'Complete Setup'}
              </button>
            )}
          </div>
        </form>
      </div>
    </div>
  );
}
