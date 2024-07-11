from fastapi import Depends, APIRouter, UploadFile, File

from user.models import User
from user.schemas import UserRead, UserUpdate
from user.service import delete_user, update_user, update_user_profile_picture, get_user_by_username
from auth.base_config import current_user
from logger import test_logger as logger

router = APIRouter()

@router.delete("/")
async def delete_user_route(user: User = Depends(current_user)) -> dict[str, str]:
    """Delete user."""
    logger.info(f"Delete user {user}") 
    return await delete_user(user=user)


@router.put("/", response_model=UserRead)
async def update_user_route(
    updated_user: UserUpdate,
    user: User = Depends(current_user)
) -> UserRead:
    db_user = await update_user(user, updated_user)
    logger.info(f"Db_user is {db_user.__dict__}")
    return await get_user_by_username(username=db_user.username)


@router.put("/update_profile_image")
async def update_user_profile_image(
    profile_picture: UploadFile = File(...),
    user: User = Depends(current_user)
) -> str:
    return await update_user_profile_picture(user, profile_picture)