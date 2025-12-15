import os
import json
from typing import List, Optional
from datetime import datetime
import firebase_admin
from firebase_admin import credentials, firestore
from google.cloud.firestore_v1.base_query import FieldFilter

from app.models import Profile, Grant, Match

# Initialize Firebase
_db = None


def get_firestore_db():
    """Get or initialize Firestore database"""
    global _db
    if _db is None:
        # Check if Firebase is already initialized
        if not firebase_admin._apps:
            # For local development, use FIRESTORE_EMULATOR_HOST
            if os.getenv("FIRESTORE_EMULATOR_HOST"):
                # Use emulator without credentials
                firebase_admin.initialize_app()
            else:
                # Production: use service account credentials
                cred_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
                if cred_path and os.path.exists(cred_path):
                    cred = credentials.Certificate(cred_path)
                    firebase_admin.initialize_app(cred)
                else:
                    # Fallback: initialize without credentials for emulator
                    firebase_admin.initialize_app()
        
        _db = firestore.client()
    return _db


class FirestoreService:
    """Service for Firestore CRUD operations"""
    
    def __init__(self):
        self.db = get_firestore_db()
        self.profiles_collection = "profiles"
        self.grants_collection = "grants"
        self.matches_collection = "matches"
    
    # Profile CRUD operations
    async def create_profile(self, profile: Profile) -> Profile:
        """Create a new profile"""
        profile_dict = profile.model_dump(exclude={"id"})
        profile_dict["created_at"] = datetime.now()
        profile_dict["updated_at"] = datetime.now()
        
        doc_ref = self.db.collection(self.profiles_collection).document()
        doc_ref.set(profile_dict)
        
        profile.id = doc_ref.id
        profile.created_at = profile_dict["created_at"]
        profile.updated_at = profile_dict["updated_at"]
        return profile
    
    async def get_profile(self, profile_id: str) -> Optional[Profile]:
        """Get a profile by ID"""
        doc = self.db.collection(self.profiles_collection).document(profile_id).get()
        if doc.exists:
            data = doc.to_dict()
            data["id"] = doc.id
            return Profile(**data)
        return None
    
    async def list_profiles(self, limit: int = 100) -> List[Profile]:
        """List all profiles"""
        docs = self.db.collection(self.profiles_collection).limit(limit).stream()
        profiles = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            profiles.append(Profile(**data))
        return profiles
    
    async def update_profile(self, profile_id: str, profile: Profile) -> Optional[Profile]:
        """Update a profile"""
        doc_ref = self.db.collection(self.profiles_collection).document(profile_id)
        if not doc_ref.get().exists:
            return None
        
        profile_dict = profile.model_dump(exclude={"id", "created_at"})
        profile_dict["updated_at"] = datetime.now()
        
        doc_ref.update(profile_dict)
        profile.id = profile_id
        profile.updated_at = profile_dict["updated_at"]
        return profile
    
    async def delete_profile(self, profile_id: str) -> bool:
        """Delete a profile"""
        doc_ref = self.db.collection(self.profiles_collection).document(profile_id)
        if not doc_ref.get().exists:
            return False
        doc_ref.delete()
        return True
    
    # Grant CRUD operations
    async def create_grant(self, grant: Grant) -> Grant:
        """Create a new grant"""
        grant_dict = grant.model_dump(exclude={"id"})
        grant_dict["created_at"] = datetime.now()
        grant_dict["updated_at"] = datetime.now()
        
        doc_ref = self.db.collection(self.grants_collection).document()
        doc_ref.set(grant_dict)
        
        grant.id = doc_ref.id
        grant.created_at = grant_dict["created_at"]
        grant.updated_at = grant_dict["updated_at"]
        return grant
    
    async def get_grant(self, grant_id: str) -> Optional[Grant]:
        """Get a grant by ID"""
        doc = self.db.collection(self.grants_collection).document(grant_id).get()
        if doc.exists:
            data = doc.to_dict()
            data["id"] = doc.id
            return Grant(**data)
        return None
    
    async def list_grants(self, limit: int = 100) -> List[Grant]:
        """List all grants"""
        docs = self.db.collection(self.grants_collection).limit(limit).stream()
        grants = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            grants.append(Grant(**data))
        return grants
    
    async def update_grant(self, grant_id: str, grant: Grant) -> Optional[Grant]:
        """Update a grant"""
        doc_ref = self.db.collection(self.grants_collection).document(grant_id)
        if not doc_ref.get().exists:
            return None
        
        grant_dict = grant.model_dump(exclude={"id", "created_at"})
        grant_dict["updated_at"] = datetime.now()
        
        doc_ref.update(grant_dict)
        grant.id = grant_id
        grant.updated_at = grant_dict["updated_at"]
        return grant
    
    async def delete_grant(self, grant_id: str) -> bool:
        """Delete a grant"""
        doc_ref = self.db.collection(self.grants_collection).document(grant_id)
        if not doc_ref.get().exists:
            return False
        doc_ref.delete()
        return True
    
    # Match CRUD operations
    async def create_match(self, match: Match) -> Match:
        """Create a new match"""
        match_dict = match.model_dump(exclude={"id"})
        match_dict["created_at"] = datetime.now()
        
        doc_ref = self.db.collection(self.matches_collection).document()
        doc_ref.set(match_dict)
        
        match.id = doc_ref.id
        match.created_at = match_dict["created_at"]
        return match
    
    async def get_match(self, match_id: str) -> Optional[Match]:
        """Get a match by ID"""
        doc = self.db.collection(self.matches_collection).document(match_id).get()
        if doc.exists:
            data = doc.to_dict()
            data["id"] = doc.id
            return Match(**data)
        return None
    
    async def list_matches_by_profile(self, profile_id: str, limit: int = 100) -> List[Match]:
        """List matches for a profile"""
        docs = (
            self.db.collection(self.matches_collection)
            .where(filter=FieldFilter("profile_id", "==", profile_id))
            .limit(limit)
            .stream()
        )
        matches = []
        for doc in docs:
            data = doc.to_dict()
            data["id"] = doc.id
            matches.append(Match(**data))
        return matches
    
    async def delete_match(self, match_id: str) -> bool:
        """Delete a match"""
        doc_ref = self.db.collection(self.matches_collection).document(match_id)
        if not doc_ref.get().exists:
            return False
        doc_ref.delete()
        return True
    
    async def delete_matches_by_profile(self, profile_id: str) -> int:
        """Delete all matches for a profile"""
        docs = (
            self.db.collection(self.matches_collection)
            .where(filter=FieldFilter("profile_id", "==", profile_id))
            .stream()
        )
        count = 0
        for doc in docs:
            doc.reference.delete()
            count += 1
        return count
    
    # Seed data loader
    async def load_seed_data(self, seed_file_path: str) -> int:
        """Load grant seed data from JSON file"""
        with open(seed_file_path, 'r') as f:
            grants_data = json.load(f)
        
        count = 0
        for grant_data in grants_data:
            grant = Grant(**grant_data)
            await self.create_grant(grant)
            count += 1
        
        return count
