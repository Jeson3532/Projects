from fastapi import APIRouter

from src.database.methods import BaseMethods
router = APIRouter(prefix="/v1/admin", tags=['Admin Panel'])

@router.get("/getAll")
async def _():
    return await BaseMethods.get_all()
