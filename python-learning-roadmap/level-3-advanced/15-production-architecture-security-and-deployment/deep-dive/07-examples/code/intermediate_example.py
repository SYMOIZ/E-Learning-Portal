from dataclasses import dataclass
import os

@dataclass(frozen=True)
class Settings:
    database_url: str
    debug: bool = False

settings = Settings(
    database_url=os.environ["DATABASE_URL"],
    debug=os.getenv("DEBUG", "false").lower() == "true",
)
