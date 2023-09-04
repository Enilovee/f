from pydantic_settings import BaseSettings,  SettingsConfigDict
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):
   
    database_hostname: str 
    database_port: str 
    database_password: str 
    database_name: str 
    database_username: str 
    secret_key: str 
    algorithm: str 
    access_token_expire_minutes: int 
    
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    
settings = Settings(BaseSettings)   