# Onboarding Flow

This document describes the user onboarding process for the AI Grant Assistant platform.

## Overview

The onboarding flow is designed to collect essential information from users to match them with the most relevant grant opportunities. The process is user-friendly, with autosave functionality to prevent data loss.

## Onboarding Steps

### Step 1: Welcome & Introduction
- Users are greeted with a welcome message
- Brief explanation of what the platform offers
- Privacy notice and terms acceptance

### Step 2: Personal Information
Users provide basic demographic information:
- **Name**: Full legal name
- **Email**: Contact email address
- **Phone**: Optional contact number
- **Date of Birth**: For age-specific grants

### Step 3: Educational Background
Collect educational details for academic grants:
- **Current Education Level**: High school, undergraduate, graduate, etc.
- **GPA**: Current grade point average
- **Field of Study**: Major or area of focus
- **Institution**: Current or most recent school

### Step 4: Financial Information
Information to match income-based grants:
- **Household Income Level**: Income bracket selection
- **Financial Need**: Self-assessment of financial need
- **Current Financial Aid**: Existing scholarships or aid

### Step 5: Identity & Background
Details for diversity and inclusion grants:
- **Minority Status**: Self-identification (optional)
- **Disability Status**: Self-disclosure (optional)
- **First Generation Student**: Whether first in family to attend college
- **Veteran Status**: Military service background

### Step 6: Geographic Information
Location-based grant matching:
- **Country**: Current country of residence
- **State/Province**: Current state or province
- **Region**: Urban, suburban, or rural
- **Willing to Relocate**: For grants requiring relocation

### Step 7: Areas of Interest
Match users with purpose-driven grants:
- **Career Goals**: Intended career path
- **Research Interests**: Academic or professional interests
- **Community Service**: Volunteer experience and interests
- **Special Talents**: Unique skills or achievements

### Step 8: Review & Submit
- Summary of all entered information
- Opportunity to edit any section
- Final submission and profile creation

## Technical Implementation

### Autosave Feature
- Data is automatically saved every 30 seconds
- Prevents data loss if user closes browser
- Visual indicator shows save status
- Users can return to complete profile later

### Progress Tracking
- Visual progress bar shows completion percentage
- Users can navigate between steps
- Previously completed steps are marked

### Validation
- Real-time field validation
- Clear error messages for invalid input
- Required fields clearly marked
- Help text for complex questions

## Privacy & Data Security

- All data is encrypted in transit and at rest
- Users can update their profile anytime
- Optional fields clearly marked
- Users control what information is shared with grant providers
- See [security-privacy.md](./security-privacy.md) for details

## Next Steps After Onboarding

1. **Profile Created**: User profile is saved to database
2. **Grant Matching**: System analyzes profile and finds matches
3. **Dashboard Redirect**: User is taken to their dashboard
4. **Top Matches Displayed**: Best grant opportunities shown
5. **Application Support**: Guidance for applying to grants
