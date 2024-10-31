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
        
# Notification返回
class Notification(NotificationCreate):
    create_time: str # 请求的创建时间
    update_time: str # 请求的更新时间

# Notification列表返回
class NotificationList(BaseModel):
    data: list[Notification] # 请求列表
    total: int # 请求总数
    total_page: int # 总页数
    page: int # 当前页码
    page_size: int # 每页数量