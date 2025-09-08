from fastapi import APIRouter, Body

from src.api.schemas import UserAdd
from src.database.methods import BaseMethods
router = APIRouter(prefix="/v1/user")

example = {
  "id": 1145678578,
  "name": "Никитос",
  "email": "jeson.jesonov@gmail.com",
  "phone": "+79821511893",
  "age": 20
}
@router.post("/addUser", tags=["Пользователи", "Users"])
async def _(user: UserAdd = Body(..., example=example)):
    personal_info = {
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "phone": user.phone.split(":")[1],
        "status": "Пользователь",
        "rank": "Новичок",
        "balance": 0.0,
        "num_parishes": 0,
        "authorized": True
    }
    result = await BaseMethods.add_user(personal_info)
    return {"success": True, "data": personal_info}
