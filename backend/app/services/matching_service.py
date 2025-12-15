from typing import List, Tuple
from datetime import datetime
from app.models import Profile, Grant, Match, MatchResult
from app.services.firestore_service import FirestoreService


class MatchingService:
    """Service for matching grants to profiles based on rules"""
    
    def __init__(self, firestore_service: FirestoreService):
        self.firestore_service = firestore_service
    
    async def find_matches(self, profile_id: str, limit: int = 5) -> List[MatchResult]:
        """Find matching grants for a profile"""
        # Get the profile
        profile = await self.firestore_service.get_profile(profile_id)
        if not profile:
            return []
        
        # Get all grants
        grants = await self.firestore_service.list_grants(limit=1000)
        
        # Calculate match score for each grant
        matches = []
        for grant in grants:
            score, explanation = self._calculate_match_score(profile, grant)
            if score > 0:
                match = Match(
                    profile_id=profile_id,
                    grant_id=grant.id,
                    score=score,
                    explanation=explanation
                )
                matches.append((match, grant, score))
        
        # Sort by score (descending) and limit results
        matches.sort(key=lambda x: x[2], reverse=True)
        matches = matches[:limit]
        
        # Save matches to Firestore and return results
        results = []
        for match, grant, _ in matches:
            saved_match = await self.firestore_service.create_match(match)
            results.append(MatchResult(match=saved_match, grant=grant))
        
        return results
    
    def _calculate_match_score(self, profile: Profile, grant: Grant) -> Tuple[float, str]:
        """
        Calculate match score and generate explanation
        Returns: (score, explanation) where score is 0-100
        """
        score = 0.0
        reasons = []
        
        # Check persona match (20 points)
        if not grant.eligible_personas or profile.persona in grant.eligible_personas:
            score += 20
            reasons.append(f"Your {profile.persona} persona is eligible")
        else:
            return 0.0, "Your persona does not match the eligibility criteria"
        
        # Check region match (15 points)
        if not grant.eligible_regions or profile.region in grant.eligible_regions:
            score += 15
            reasons.append(f"Your region ({profile.region}) is eligible")
        else:
            return 0.0, f"Your region ({profile.region}) is not eligible for this grant"
        
        # Check GPA requirement (20 points)
        if grant.min_gpa is not None:
            if profile.gpa is not None and profile.gpa >= grant.min_gpa:
                score += 20
                reasons.append(f"Your GPA ({profile.gpa}) meets the minimum requirement ({grant.min_gpa})")
            else:
                return 0.0, f"Your GPA does not meet the minimum requirement of {grant.min_gpa}"
        else:
            score += 20
            reasons.append("No GPA requirement")
        
        # Check minority status (15 points)
        if grant.requires_minority:
            if profile.is_minority:
                score += 15
                reasons.append("You meet the minority status requirement")
            else:
                return 0.0, "This grant requires minority status"
        else:
            score += 15
            reasons.append("No minority status requirement")
        
        # Check disability status (15 points)
        if grant.requires_disability:
            if profile.has_disability:
                score += 15
                reasons.append("You meet the disability status requirement")
            else:
                return 0.0, "This grant requires disability status"
        else:
            score += 15
            reasons.append("No disability status requirement")
        
        # Check income level (15 points)
        if not grant.income_requirements or profile.income_level in grant.income_requirements:
            score += 15
            reasons.append(f"Your income level ({profile.income_level}) is eligible")
        else:
            return 0.0, f"Your income level ({profile.income_level}) is not eligible"
        
        # Check deadline (not expired) - bonus points for urgency
        try:
            deadline = datetime.fromisoformat(grant.deadline.replace('Z', '+00:00'))
            if deadline < datetime.now(deadline.tzinfo):
                return 0.0, "This grant deadline has passed"
            
            # Bonus points for upcoming deadlines
            days_until_deadline = (deadline - datetime.now(deadline.tzinfo)).days
            if days_until_deadline < 30:
                reasons.append(f"Deadline is approaching ({days_until_deadline} days)")
            else:
                reasons.append(f"Deadline: {grant.deadline}")
        except Exception:
            # If deadline parsing fails, just note it
            reasons.append(f"Deadline: {grant.deadline}")
        
        # Generate explanation
        explanation = f"Match score: {score}/100. " + "; ".join(reasons) + "."
        
        return score, explanation
    
    async def refresh_matches(self, profile_id: str, limit: int = 5) -> List[MatchResult]:
        """Delete old matches and create new ones"""
        # Delete existing matches
        await self.firestore_service.delete_matches_by_profile(profile_id)
        
        # Find new matches
        return await self.find_matches(profile_id, limit)
