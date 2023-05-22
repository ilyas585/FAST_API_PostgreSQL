import os


mode = "docker"
POSTGRES_HOST = "localhost" if mode == "local" else "192.168.99.100"
POSTGRES_DB = os.getenv("POSTGRES_DB") or "ilyas_db"
POSTGRES_USER = os.getenv("POSTGRES_USER") or "ilyas"
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD") or "admin123"
SQLALCHEMY_DATABASE_URI = os.getenv(
    "SQLALCHEMY_DATABASE_URI",
    f"postgresql+psycopg2://ilyas:admin123@{POSTGRES_HOST}:5432/ilyas_db"
)
