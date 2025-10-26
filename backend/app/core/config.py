from functools import lru_cache
from typing import Literal

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        env_nested_delimiter="__",
        extra="ignore",
    )

    app_name: str = "Travel Planner API"
    debug: bool = False
    environment: Literal["development", "production", "test"] = "development"
    api_v1_prefix: str = "/api/v1"
    database_url: str = Field(
        default="sqlite+aiosqlite:///./travel_planner.db",
        description="Connection URL for the application's primary database.",
    )


@lru_cache()
def get_settings() -> "Settings":
    """Cached settings instance for use as a dependency."""

    return Settings()
