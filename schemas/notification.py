# schemas/notification.py

from pydantic import BaseModel
from typing import Optional


# Notification创建请求
class NotificationCreate(BaseModel):
    identifier: Optional[str] # 请求的唯一标识符
    account_identifier: str # 请求的账户的唯一标识符
    content: str # 请求的内容
    
    class Config:
        orm_mode = True
        
# Notification同步请求（用于区块链同步）
class NotificationSync(NotificationCreate):
    create_at: str # 请求的创建时间
    update_at: str # 请求的更新时间
        
# Notification返回
class NotificationResponse(NotificationCreate):
    create_time: str # 请求的创建时间
    update_time: str # 请求的更新时间
    
# Notification列表返回
class NotificationList(BaseModel):
    data: list[NotificationResponse] # 请求列表