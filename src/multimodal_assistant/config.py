"""Centralized configuration loaded from environment variables (.env).

This file is complete — you should not need to modify it for the core modules,
but feel free to add new settings as your implementation needs them.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    # LLM
    llm_provider: str = "openai"
    openai_api_key: str = ""
    llm_model_name: str = "gpt-3.5-turbo"

    # Embeddings
    embedding_model_name: str = "sentence-transformers/all-MiniLM-L6-v2"

    # Vector store
    vector_db_provider: str = "lancedb"
    lancedb_uri: str = "./data/lancedb"
    pinecone_api_key: str = ""
    pinecone_environment: str = ""
    weaviate_url: str = ""

    # Text generation
    text_gen_base_model: str = "gpt2"
    text_gen_model_dir: str = "./models/text_generation"

    # Image generation
    image_gen_provider: str = "stable_diffusion"
    stable_diffusion_model_id: str = "stabilityai/stable-diffusion-2-1"
    dalle_api_key: str = ""

    # API
    api_host: str = "0.0.0.0"
    api_port: int = 8000
    jwt_secret_key: str = "change-me"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60
    rate_limit_per_minute: int = 30
    redis_url: str = "redis://localhost:6379/0"

    # Frontend
    frontend_api_base_url: str = "http://localhost:8000"

    # Observability
    log_level: str = "INFO"
    enable_metrics: bool = True


settings = Settings()
