import logging
from typing import Protocol

logger = logging.getLogger(__name__)

class UserRepository(Protocol):
    def create(self, email: str) -> dict:
        ...

def register_user(email: str, repository: UserRepository) -> dict:
    if "@" not in email:
        raise ValueError("Invalid email address")
    user = repository.create(email)
    logger.info("user_registered", extra={"user_id": user["id"]})
    return user
