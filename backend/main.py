"""
Main FastAPI application entry point.

This file sets up the FastAPI app with CORS middleware to allow requests
from the frontend running on http://localhost:3000.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Create the FastAPI application instance
# The title and version will appear in the auto-generated API documentation
app = FastAPI(
    title="AI Grant Assistant API",
    version="1.0.0",
    description="Backend API for the AI Grant Assistant platform"
)

# Configure CORS (Cross-Origin Resource Sharing)
# This allows the frontend (running on localhost:3000) to make requests to this API
# Without CORS, browsers block requests between different origins for security
origins = [
    "http://localhost:3000",  # Next.js development server
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Which origins can access this API
    allow_credentials=True,  # Allow cookies to be sent with requests
    allow_methods=["*"],     # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],     # Allow all headers
)


# Health check endpoint
# This simple endpoint helps verify the API is running properly
# Useful for monitoring, load balancers, and development testing
@app.get("/ping")
async def ping():
    """
    Simple health check endpoint.
    
    Returns:
        dict: A message confirming the API is running
    """
    return {"message": "pong"}
