from sqlalchemy.orm import Session
import logging

from exceptions import ResourceNotFound

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user(self, user_id: int):
        try:
            user = self.db.query(User).get(user_id)
            if not user:
                raise ResourceNotFound(f'User with ID {user_id} not found.')
            return user
        except Exception as e:
            logger.exception("Database error while fetching user %s", user)
            raise BaseException("Internal database error") from e