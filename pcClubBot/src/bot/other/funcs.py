import re
from typing import Annotated
from pydantic import EmailStr, constr, BaseModel
from pydantic_extra_types.phone_numbers import PhoneNumber
class PersonalInfo(BaseModel):
    name: str
    email: EmailStr
    phone: PhoneNumber
    age: int


num_of_questions: Annotated[int, "Количество вопросов в окне регистрации"] = 4


def parse_reg_info(text: str):
    filter_ = re.findall(r"\d+\.\s*(.*)", text)

    except_incomplete_response = {"status": False, "detail": "Ответ дан неполноценно."}
    except_error_validate = {"status": False, "detail": "Ошибка валидации данных. Проверьте корректность введенных данных."}
    personal_info = dict()

    if filter_:
        if len(filter_) == num_of_questions:
            try:
                personal_info['name'] = filter_[0]
                personal_info['email'] = filter_[1]
                if '+' == filter_[2][0]:
                    personal_info['phone'] = filter_[2]
                else:
                    personal_info['phone'] = '+' + filter_[2]
                personal_info['age'] = filter_[3]
                return {"status": True, "data": PersonalInfo(**personal_info)}
            except:
                return except_error_validate
        return except_incomplete_response

    split_message = text.split("\n")
    if len(split_message) == num_of_questions:
        try:
            personal_info['name'] = split_message[0]
            personal_info['email'] = split_message[1]
            personal_info['phone'] = split_message[2]
            personal_info['age'] = split_message[3]
            return {"status": True, "data": PersonalInfo(**personal_info)}
        except:
            return except_error_validate

    return except_incomplete_response


