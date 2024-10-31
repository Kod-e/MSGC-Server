#api/rest/notification.py
from restful import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from service import *
from storage import *


#notification路由
router = APIRouter(prefix="/notification", tags=["notification"])


#创建请求
@router.post("/create", response_model=Notification)
def create_notification(notification: NotificationCreate, session: Session = Depends(get_db)):
    """
    创建请求
    :param notification: 请求创建请求
    :param session: 数据库会话
    :return: 返回创建的请求
    """
    try:
        return NotificationService.create_notification(notification.account_identifier, notification.content, session)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))
    
#通过identifier获取请求
@router.get("/get", response_model=Notification)
def get_notification(identifier: str,time:datetime=None, session: Session = Depends(get_db)):
    """
    通过identifier获取请求
    :param identifier: 请求的唯一标识符
    :param session: 数据库会话
    :return: 返回获取的请求
    """
    try:
        return NotificationService.get_notifications_after_time(identifier=identifier, session=session,time=time)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))