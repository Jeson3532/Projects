from src.api.routers.admin import router as admin_router
from src.api.routers.user import router as user_router

routers = [user_router, admin_router]