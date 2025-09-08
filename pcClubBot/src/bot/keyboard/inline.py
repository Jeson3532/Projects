from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import KeyboardBuilder

async def get_main_menu_keyboard():
    ...

async def get_auth_or_reg_keyboard():
    buttons = [[InlineKeyboardButton(text='Регистрация', callback_data="registration")],
               [InlineKeyboardButton(text='Авторизация', callback_data="authorization")]]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup

async def get_choice_registration_keyboard():
    buttons = [[InlineKeyboardButton(text='Одним сообщением', callback_data="reg_var1")],
               [InlineKeyboardButton(text='Пошаговая', callback_data="reg_var2")]]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup


async def get_confirm_reg_keyboard():
    buttons = [
        [InlineKeyboardButton(text="✅ Подтвердить", callback_data="confirm_reg")],
        [InlineKeyboardButton(text="❌ Отменить", callback_data="cancel_reg")]
    ]
    markup = InlineKeyboardMarkup(inline_keyboard=buttons)
    return markup
