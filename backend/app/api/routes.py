from fastapi import APIRouter

from ..dependencies import SettingsDep

router = APIRouter()


@router.get("/health", summary="Backend service health status")
def health_check(settings: SettingsDep) -> dict[str, str]:
    """Basic health check endpoint exposing environment metadata."""

    return {
        "status": "ok",
        "app_name": settings.app_name,
        "environment": settings.environment,
    }
