from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from src.bot.fsm.groups import MenuStates
from src.bot.other.funcs import parse_reg_info
from src.bot.keyboard.inline import get_confirm_reg_keyboard

import aiohttp as http

router = Router()
register_states = [
    MenuStates.CHOICE_REGISTRATION_OPTION_STATE,
    MenuStates.REGISTER_ONE_MESSAGE_STATE,
    MenuStates.CONFIRM_REGISTRATION_STATE
]
@router.message(MenuStates.REGISTER_ONE_MESSAGE_STATE)
async def register(msg: Message, state: FSMContext):
    reg_info = msg.text
    result = parse_reg_info(reg_info)
    status = result.get("status")
    if status:
        data = result.get("data")
        await msg.answer("📃 Проверьте правильность введенных данных:\n"
                         f"- Имя: {data.name}\n"
                         f"- Email: {data.email}\n"
                         f"- Номер телефона: {data.phone.split(":")[1]}\n"
                         f"- Возраст: {data.age}", reply_markup=await get_confirm_reg_keyboard())
        await state.set_data(data.model_dump())
        await state.set_state(MenuStates.CONFIRM_REGISTRATION_STATE)

    else:
        detail = result.get("detail")
        await msg.answer("💥 Произошла ошибка при попытке собрать информацию.\n"
                         f"📃Детали ошибки: {detail}")

@router.message(MenuStates.CONFIRM_REGISTRATION_STATE)
async def echo_confirm_reg(msg: Message):
    await msg.answer(text="🤖 Сейчас от тебя требуется только принять решение и сообщить его мне. Воспользуйся кнопками для принятия решения, которые я тебе предоставил.")

@router.callback_query(F.data == "confirm_reg", MenuStates.CONFIRM_REGISTRATION_STATE)
async def confirm_registration(cb: CallbackQuery, state: FSMContext):
    async with http.ClientSession() as session:
        await state.update_data(id=cb.from_user.id)
        async with session.post("http://127.0.0.1:8000/v1/user/addUser", json=await state.get_data()) as response:
            if response.status == 200:
                await cb.message.answer(text=f"🌟 Регистрация прошла успешно! ")
            else:
                await cb.message.answer(text=f"🤬 Произошла ошибка при регистрации пользователя. Обратитесь к администрации для устранения проблем.")
            await state.clear()



@router.callback_query(F.data == "cancel_reg", MenuStates.CONFIRM_REGISTRATION_STATE)
async def cancel_registration(cb: CallbackQuery, state: FSMContext):
    await cb.answer("Регистрация отменена")
    await cb.message.answer(text='⛔ Регистрация отменена. Вы можете начать её заново.')
    await state.clear()
