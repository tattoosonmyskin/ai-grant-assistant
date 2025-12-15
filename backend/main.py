from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

from app.routes import profiles, grants, matches, packets

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(
    title="AI Grant Assistant API",
    description="API for AI-driven grant matching and application assistance",
    version="1.0.0"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://127.0.0.1:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(profiles.router)
app.include_router(grants.router)
app.include_router(matches.router)
app.include_router(packets.router)


@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to AI Grant Assistant API",
        "version": "1.0.0",
        "docs": "/docs"
    }


@app.get("/health")
async def health():
    """Health check endpoint"""
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
