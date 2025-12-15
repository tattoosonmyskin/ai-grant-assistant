from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


class Profile(BaseModel):
    """User profile model"""
    id: Optional[str] = None
    name: str
    email: str
    persona: str  # e.g., "student", "researcher", "entrepreneur"
    region: str
    gpa: Optional[float] = None
    is_minority: bool = False
    has_disability: bool = False
    income_level: str  # "low", "medium", "high"
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "name": "John Doe",
                "email": "john@example.com",
                "persona": "student",
                "region": "California",
                "gpa": 3.8,
                "is_minority": False,
                "has_disability": False,
                "income_level": "medium"
            }
        }


class Grant(BaseModel):
    """Grant model"""
    id: Optional[str] = None
    title: str
    description: str
    amount: float
    deadline: str  # ISO format date string
    eligible_personas: List[str] = []
    eligible_regions: List[str] = []
    min_gpa: Optional[float] = None
    requires_minority: bool = False
    requires_disability: bool = False
    income_requirements: List[str] = []  # ["low", "medium", "high"]
    organization: str
    url: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "title": "STEM Excellence Grant",
                "description": "Grant for STEM students",
                "amount": 5000,
                "deadline": "2024-12-31",
                "eligible_personas": ["student"],
                "eligible_regions": ["California", "New York"],
                "min_gpa": 3.5,
                "requires_minority": False,
                "requires_disability": False,
                "income_requirements": ["low", "medium"],
                "organization": "Tech Foundation",
                "url": "https://example.com"
            }
        }


class Match(BaseModel):
    """Match model representing a grant match for a profile"""
    id: Optional[str] = None
    profile_id: str
    grant_id: str
    score: float  # Match score 0-100
    explanation: str  # Explanation of why this grant matches
    created_at: Optional[datetime] = None

    class Config:
        json_schema_extra = {
            "example": {
                "profile_id": "profile123",
                "grant_id": "grant456",
                "score": 85.5,
                "explanation": "This grant matches your student persona and GPA requirements."
            }
        }


class MatchResult(BaseModel):
    """Extended match result with grant details"""
    match: Match
    grant: Grant


class PacketRequest(BaseModel):
    """Request model for packet generation"""
    profile_id: str
    grant_ids: List[str]
    format: str = "pdf"  # "pdf" or "docx"

    class Config:
        json_schema_extra = {
            "example": {
                "profile_id": "profile123",
                "grant_ids": ["grant456", "grant789"],
                "format": "pdf"
            }
        }
