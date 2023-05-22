import os


mode = "docker"
POSTGRES_HOST = "localhost" if mode == "local" else "192.168.99.100"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "ilyas_db"
POSTGRES_USER = os.getenv("POSTGRES_USER") or "ilyas"
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") or "admin123"
