<<<<<<< HEAD
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
=======
from fastapi import APIRouter, Body, HTTPException

from src.api.schemas import UserAdd
from src.database.methods import BaseMethods
from src.utils.enums import Ranking, Status

import logging

router = APIRouter(prefix="/v1/user")
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG)

@router.post("/addUser", tags=["Пользователи", "Users"])
async def _(user: UserAdd = Body(..., example={
        "id": 1145678578,
        "name": "Никита",
        "email": "jeson.jesonov@gmail.com",
        "phone": "+79821511893",
        "age": 20
})):

    if BaseMethods.check_registration(user.id):
        raise HTTPException(status_code=400, detail="Данный пользователь уже зарегистрирован.")
>>>>>>> develop
    personal_info = {
        "id": user.id,
        "name": user.name,
        "age": user.age,
        "email": user.email,
        "phone": user.phone.split(":")[1],
<<<<<<< HEAD
        "status": "Пользователь",
        "rank": "Новичок",
=======
        "status": Status.ORDINARY_USER,
        "rank": Ranking.BEGINNER,
>>>>>>> develop
        "balance": 0.0,
        "num_parishes": 0,
        "authorized": True
    }
<<<<<<< HEAD
    result = await BaseMethods.add_user(personal_info)
    return {"success": True, "data": personal_info}
=======
    await BaseMethods.add_user(personal_info)
    return {"success": True, "data": personal_info}

>>>>>>> develop
