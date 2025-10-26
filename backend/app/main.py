from fastapi import FastAPI

from .api.routes import router as api_router
from .core.config import get_settings

settings = get_settings()

app = FastAPI(
    title=settings.app_name,
    debug=settings.debug,
    version="0.1.0",
    docs_url="/docs" if settings.debug else None,
    redoc_url="/redoc" if settings.debug else None,
)


@app.get("/", summary="API index")
def read_root() -> dict[str, str]:
    """Return a simple welcome message with the API name."""

    return {"message": f"Welcome to {settings.app_name}"}


app.include_router(api_router, prefix=settings.api_v1_prefix)
