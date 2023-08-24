from typing import Optional

from pydantic import BaseSettings, EmailStr


class Settings(BaseSettings):
    APP_TITLE: str = 'Куаркот'
    DESCRIPTION: str = 'Жертвуй всем'
    DATABASE_URL: str = 'sqlite+aiosqlite:///./fastapi.db'
    SECRET: str = 'SECRET'

    FIRST_SUPERUSER_EMAIL: Optional[EmailStr] = None
    FIRST_SUPERUSER_PASSWORD: Optional[str] = None

    ZERO: int = 0
    LENGTH_NAME: int = 100
    MIN_ANYSTR_LENGTH: int = 1
    MIN_LENGTH_PASS: int = 3
    LIFETIME_JWT: int = 3600

    FORMAT: Optional[str] = None
    ROW_COUNT: int = 15
    COLUMN_COUNT: int = 5
    ROW: int = 10

    type: Optional[str] = None
    project_id: Optional[str] = None
    private_key_id: Optional[str] = None
    private_key: Optional[str] = None
    client_email: Optional[str] = None
    client_id: Optional[str] = None
    auth_uri: Optional[str] = None
    token_uri: Optional[str] = None
    auth_provider_x509_cert_url: Optional[str] = None
    client_x509_cert_url: Optional[str] = None

    email: Optional[str] = None

    class Config:
        env_file = '.env'


settings = Settings()
