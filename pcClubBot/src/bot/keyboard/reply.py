from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
async def get_reply_main_menu_keyboard_guest():
    buttons = [
        [KeyboardButton(text="👤 Авторизация/Регистрация")],
        [KeyboardButton(text="💄 Бронь места"), KeyboardButton(text="👀 Информация о клубе")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup

async def get_reply_main_menu_keyboard_user():
    buttons = [
        [KeyboardButton(text="💼 Личный кабинет")],
        [KeyboardButton(text="💄 Бронь места"), KeyboardButton(text="👀 Информация о клубе")]
    ]
    markup = ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)
    return markup
