from fastapi import Depends, APIRouter, HTTPException

from auth.models import User
from auth.schemas import UserRead
from auth.base_config import current_user
from auth.service import verify_verification_token
from auth.manager import send_verification
from logger import logger

router = APIRouter()

@router.get('/ask_verification')
async def ask_verification(user: User = Depends(current_user)):
    await send_verification(user=user)
    return {
        'status': 'success',
    }

@router.get("/verify-account", response_model=UserRead)
async def verify_user(token: str, user: User = Depends(current_user)):
    if user.is_verified:
        logger.warning(f"User with verification token {token} already verified")
        raise HTTPException(status_code=400, detail=f"User with this verification token {token} already verified")
    return await verify_verification_token(token)
