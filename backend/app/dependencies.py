"""Shared dependency wiring for the FastAPI application."""

from typing import Annotated

from fastapi import Depends

from .core.config import Settings, get_settings


SettingsDep = Annotated[Settings, Depends(get_settings)]
