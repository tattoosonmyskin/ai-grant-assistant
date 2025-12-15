from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Match, MatchResult
from app.services.firestore_service import FirestoreService
from app.services.matching_service import MatchingService

router = APIRouter(prefix="/matches", tags=["matches"])


def get_services():
    """Get service instances"""
    firestore_service = FirestoreService()
    matching_service = MatchingService(firestore_service)
    return firestore_service, matching_service


@router.post("/find/{profile_id}", response_model=List[MatchResult])
async def find_matches(profile_id: str, limit: int = 5):
    """Find matching grants for a profile"""
    try:
        firestore_service, matching_service = get_services()
        # Check if profile exists
        profile = await firestore_service.get_profile(profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        # Find matches
        matches = await matching_service.find_matches(profile_id, limit=limit)
        return matches
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.post("/refresh/{profile_id}", response_model=List[MatchResult])
async def refresh_matches(profile_id: str, limit: int = 5):
    """Refresh matches for a profile (delete old and create new)"""
    try:
        firestore_service, matching_service = get_services()
        # Check if profile exists
        profile = await firestore_service.get_profile(profile_id)
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found")
        
        # Refresh matches
        matches = await matching_service.refresh_matches(profile_id, limit=limit)
        return matches
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/profile/{profile_id}", response_model=List[Match])
async def get_profile_matches(profile_id: str, limit: int = 100):
    """Get all matches for a profile"""
    try:
        firestore_service, _ = get_services()
        matches = await firestore_service.list_matches_by_profile(profile_id, limit=limit)
        return matches
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{match_id}", response_model=Match)
async def get_match(match_id: str):
    """Get a match by ID"""
    firestore_service, _ = get_services()
    match = await firestore_service.get_match(match_id)
    if not match:
        raise HTTPException(status_code=404, detail="Match not found")
    return match


@router.delete("/{match_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_match(match_id: str):
    """Delete a match"""
    firestore_service, _ = get_services()
    success = await firestore_service.delete_match(match_id)
    if not success:
        raise HTTPException(status_code=404, detail="Match not found")
    return None
