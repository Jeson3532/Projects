from ..routers.user import message, callback
from ..routers.user.register.router import router as reg_router

routers = [message.msr, callback.cbr, reg_router]