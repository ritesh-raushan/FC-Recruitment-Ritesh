from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional

class Settings(BaseSettings):
    database_hostname: Optional[str] = None
    database_port: Optional[str] = None 
    database_password: Optional[str] = None
    database_name: Optional[str] = None
    database_username: Optional[str] = None
    
    database_url: Optional[str] = None

    model_config = SettingsConfigDict(env_file=".env", extra='ignore')

settings = Settings()