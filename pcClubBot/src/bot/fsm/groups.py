from aiogram.fsm.state import StatesGroup, State

class MenuStates(StatesGroup):
    START = State()

    # Состояния регистрации и авторизации (Общие)
    CHOICE_REG_OR_AUTH_STATE = State()
    # Состояние регистрации
    CHOICE_REGISTRATION_OPTION_STATE = State()
    REGISTER_ONE_MESSAGE_STATE = State()
    CONFIRM_REGISTRATION_STATE = State()

