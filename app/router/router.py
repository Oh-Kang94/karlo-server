from fastapi import APIRouter

from app.controller import (images_ctrl, updater_ctrl)


router = APIRouter()

router.include_router(
    images_ctrl.router,
    prefix="/images",
    tags=["images"]
)

router.include_router(
    updater_ctrl.router,
    prefix="/update",
    tags = ["update"]
)