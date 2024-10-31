from .account import router as account_router
from .notification import router as notification_router

# 路由列表
routers = [account_router, notification_router]