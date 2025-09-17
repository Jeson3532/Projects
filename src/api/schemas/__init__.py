from pydantic import BaseModel, EmailStr, Field
from pydantic_extra_types.phone_numbers import PhoneNumber
from typing import Annotated

class UserAdd(BaseModel):
    id: Annotated[int, Field(..., description="Айди ТГ")]
    name: Annotated[str, Field(..., description="Имя пользователя")]
    email: Annotated[EmailStr, Field(..., description="Почта пользователя")]
    phone: Annotated[PhoneNumber, Field(..., description="Номер телефона пользователя")]
    age: Annotated[int, Field(..., description="Возраст пользователя")]