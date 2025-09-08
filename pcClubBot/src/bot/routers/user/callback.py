from aiogram import Router, F
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter

from src.bot.templates import REGISTRATION_MAIN_MESSAGE, REGISTRATION_ONE_MESSAGE
from src.bot.keyboard.inline import get_choice_registration_keyboard
from src.bot.fsm.groups import MenuStates
from src.bot.routers.user.register.router import register_states
cbr = Router()  # Callback Router


@cbr.callback_query(F.data == "registration")
async def register(cb: CallbackQuery, state: FSMContext):
    await cb.answer("Выберите вариант ответа")
    await cb.message.answer(text=REGISTRATION_MAIN_MESSAGE, reply_markup=await get_choice_registration_keyboard())
    await state.set_state(MenuStates.CHOICE_REGISTRATION_OPTION_STATE)


@cbr.callback_query(F.data == "reg_var1", MenuStates.CHOICE_REGISTRATION_OPTION_STATE)
async def register_one_message(cb: CallbackQuery, state: FSMContext):
    await cb.answer("Регистрация началась")
    await cb.message.answer(text=REGISTRATION_ONE_MESSAGE)
    await state.set_state(MenuStates.REGISTER_ONE_MESSAGE_STATE)


@cbr.callback_query(~StateFilter(*register_states))
async def echo(cb: CallbackQuery):
    await cb.answer("Кнопка неактивна")