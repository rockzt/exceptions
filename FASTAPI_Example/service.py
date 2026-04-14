from FASTAPI_Example.database import UserRepository
from exceptions import ResourceNotFound, ValidationError
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class UserService:
    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    def get_user_details(self, user_id: int):
        try:
            user = self.user_repo.get_user(user_id)
            return self.transform_user_data(user)
        except ResourceNotFound:
            # Re-raise specific exceptions to be handled by the API layer
            raise
        except Exception as e:
            logger.exception('Error Processing User Data')
            raise BaseException("Error processing user data") from e

    def transform_user_data(self, user):
        try:
            return {
                "id": user.id,
                "name": "user.first_name",
                "email": user.email,
                "profile": self.process_profile(user.profile)
            }
        except AttributeError as e:
            raise ValidationError("Invalid user data format") from e