from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from src.database.methods import BaseMethods
def get_reply_main_menu_keyboard_guest():

    buttons = [
        [KeyboardButton(text="👤 Авторизация/Регистрация")],
        [KeyboardButton(text="💄 Бронь места"), KeyboardButton(text="👀 Информация о клубе")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup

def get_reply_main_menu_keyboard_user():

    buttons = [
        [KeyboardButton(text="💼 Личный кабинет")],
        [KeyboardButton(text="💄 Бронь места"), KeyboardButton(text="👀 Информация о клубе")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup




async def get_reply_main_menu_keyboard(id_: int):
    result = await BaseMethods.check_auth_user(id_)
    if result:
        return get_reply_main_menu_keyboard_user()
    return get_reply_main_menu_keyboard_guest()

