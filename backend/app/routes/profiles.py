from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Profile
from app.services.firestore_service import FirestoreService

router = APIRouter(prefix="/profiles", tags=["profiles"])


def get_firestore_service():
    """Get firestore service instance"""
    return FirestoreService()


@router.post("/", response_model=Profile, status_code=status.HTTP_201_CREATED)
async def create_profile(profile: Profile):
    """Create a new profile"""
    try:
        firestore_service = get_firestore_service()
        return await firestore_service.create_profile(profile)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{profile_id}", response_model=Profile)
async def get_profile(profile_id: str):
    """Get a profile by ID"""
    firestore_service = get_firestore_service()
    profile = await firestore_service.get_profile(profile_id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile


@router.get("/", response_model=List[Profile])
async def list_profiles(limit: int = 100):
    """List all profiles"""
    try:
        firestore_service = get_firestore_service()
        return await firestore_service.list_profiles(limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{profile_id}", response_model=Profile)
async def update_profile(profile_id: str, profile: Profile):
    """Update a profile"""
    firestore_service = get_firestore_service()
    updated_profile = await firestore_service.update_profile(profile_id, profile)
    if not updated_profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return updated_profile


@router.delete("/{profile_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_profile(profile_id: str):
    """Delete a profile"""
    firestore_service = get_firestore_service()
    success = await firestore_service.delete_profile(profile_id)
    if not success:
        raise HTTPException(status_code=404, detail="Profile not found")
    return None
