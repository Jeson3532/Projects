import logging

from aiogram import Router, F
from aiogram.types import Message

from aiogram.filters import CommandStart, StateFilter, Command
from aiogram.fsm.context import FSMContext

from src.bot.templates import HELLO_MESSAGE, CHOICE_REG_OR_AUTH_MESSAGE
from src.bot.fsm.groups import MenuStates
from src.bot.keyboard.reply import get_reply_main_menu_keyboard
from src.bot.keyboard.inline import get_auth_or_reg_keyboard
from src.bot.routers.user.register.router import register_states
from src.database.methods import BaseMethods

msr = Router(name=__name__)  # Message Router




@msr.message(CommandStart())
async def start_command(msg: Message, state: FSMContext):
    start_state = MenuStates.START
    user_id = msg.from_user.id
    if await state.get_state() == start_state:
        await msg.answer("🤖 Я уже дал тебе инструкцию, тебе осталось только определиться с выбором.")
        return
    await msg.answer(text=HELLO_MESSAGE, reply_markup=await get_reply_main_menu_keyboard(user_id))
    await state.set_state(start_state)


@msr.message(MenuStates.START, F.text == "👤 Авторизация/Регистрация")
async def authorization_registration(msg: Message, state: FSMContext):
    choice_reg_or_auth = MenuStates.CHOICE_REG_OR_AUTH_STATE

    await msg.answer(text=CHOICE_REG_OR_AUTH_MESSAGE, reply_markup=await get_auth_or_reg_keyboard())
    await state.set_state(choice_reg_or_auth)


@msr.message(MenuStates.START, F.text == "💼 Личный кабинет")
async def personal_account(msg: Message, state: FSMContext):
    await msg.answer(text=...)

@msr.message(Command("test"))
async def personal_account(msg: Message):
    result = await BaseMethods.check_auth_user(123)
    await msg.answer(text=f"{msg.from_user.id}")


@msr.message(~StateFilter(MenuStates.START), ~StateFilter(*register_states))
async def echo(msg: Message, state: FSMContext):
    start_state = MenuStates.START
    user_id = msg.from_user.id
    await msg.answer(text=HELLO_MESSAGE, reply_markup=await get_reply_main_menu_keyboard(user_id))
    await state.set_state(start_state)


@msr.message(~StateFilter(*register_states))
async def not_understand(msg: Message):
    await msg.answer("🤖 Извини, но я ничего не понял. Просто выбери то, что тебе требуется")
