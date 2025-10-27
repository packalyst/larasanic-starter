"""
Database Configuration
Database connection and model configuration
"""
from larasanic.support import Storage, EnvHelper

# Database URL
# Supports:
# - SQLite: sqlite://path/to/db.sqlite3
# - PostgreSQL: postgres://user:pass@host:port/dbname
DATABASE_URL = EnvHelper.get(
    'DATABASE_URL',
    f"sqlite://{Storage.database('database.sqlite3')}"
)

# Models to register with Tortoise ORM
# Add your model module paths here
MODELS = [
    "larasanic.auth.models.user",
]