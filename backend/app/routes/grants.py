from fastapi import APIRouter, HTTPException, status
from typing import List
from app.models import Grant
from app.services.firestore_service import FirestoreService

router = APIRouter(prefix="/grants", tags=["grants"])
firestore_service = FirestoreService()


@router.post("/", response_model=Grant, status_code=status.HTTP_201_CREATED)
async def create_grant(grant: Grant):
    """Create a new grant"""
    try:
        return await firestore_service.create_grant(grant)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{grant_id}", response_model=Grant)
async def get_grant(grant_id: str):
    """Get a grant by ID"""
    grant = await firestore_service.get_grant(grant_id)
    if not grant:
        raise HTTPException(status_code=404, detail="Grant not found")
    return grant


@router.get("/", response_model=List[Grant])
async def list_grants(limit: int = 100):
    """List all grants"""
    try:
        return await firestore_service.list_grants(limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/{grant_id}", response_model=Grant)
async def update_grant(grant_id: str, grant: Grant):
    """Update a grant"""
    updated_grant = await firestore_service.update_grant(grant_id, grant)
    if not updated_grant:
        raise HTTPException(status_code=404, detail="Grant not found")
    return updated_grant


@router.delete("/{grant_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_grant(grant_id: str):
    """Delete a grant"""
    success = await firestore_service.delete_grant(grant_id)
    if not success:
        raise HTTPException(status_code=404, detail="Grant not found")
    return None


@router.post("/seed", status_code=status.HTTP_201_CREATED)
async def seed_grants(seed_file: str = "data/grants_seed.json"):
    """Load grant seed data from JSON file"""
    try:
        count = await firestore_service.load_seed_data(seed_file)
        return {"message": f"Successfully loaded {count} grants", "count": count}
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail=f"Seed file not found: {seed_file}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
