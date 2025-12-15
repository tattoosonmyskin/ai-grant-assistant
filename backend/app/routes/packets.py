from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse
from app.models import PacketRequest
from app.services.firestore_service import FirestoreService
from app.services.packet_service import PacketGeneratorService

router = APIRouter(prefix="/packets", tags=["packets"])


def get_services():
    """Get service instances"""
    firestore_service = FirestoreService()
    packet_service = PacketGeneratorService(firestore_service)
    return firestore_service, packet_service


@router.post("/generate")
async def generate_packet(request: PacketRequest):
    """Generate a grant application packet"""
    try:
        _, packet_service = get_services()
        filepath = await packet_service.generate_packet(
            profile_id=request.profile_id,
            grant_ids=request.grant_ids,
            format=request.format
        )
        
        # Return file info (in production, you might upload to cloud storage)
        return {
            "message": "Packet generated successfully",
            "filepath": filepath,
            "format": request.format,
            "download_url": f"/packets/download?filepath={filepath}"
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/download")
async def download_packet(filepath: str):
    """Download a generated packet"""
    try:
        # Determine media type based on file extension
        media_type = "application/pdf" if filepath.endswith(".pdf") else "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        
        return FileResponse(
            path=filepath,
            media_type=media_type,
            filename=filepath.split("/")[-1]
        )
    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
