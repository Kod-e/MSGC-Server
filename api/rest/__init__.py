#api/rest/__init__.py


from .account import router as account_router
from .notification import router as notification_router

routers = [
    account_router,
    notification_router,
]