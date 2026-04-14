from fastapi import FastAPI, HTTPException, Depends
from starlette.responses import JSONResponse
import logging

from exceptions import BaseAppException, ResourceNotFound, ValidationError
from service import UserService

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

# Global exception handler
@app.exception_handler(BaseAppException)
async def app_exception_handler(request, exc):
    logger.error(f"Unhandled exception: {exc.message}", exc_info=True)
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.message}
    )

@app.get("/users/{user_id}")
async def get_user(user_id: int, service: UserService = Depends()):
    try:
        return await service.get_user(user_id)
    except ResourceNotFound as e:
        raise HTTPException(status_code=404, detail=str(e))
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Unhandled exception: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal Server Error")