# schemas/account.py

from pydantic import BaseModel
from typing import Optional

# 账号创建请求
class AccountCreate(BaseModel):
    identifier: str # 账号的唯一标识符
    nickname: str # 账号的昵称
    avatar: Optional[str] # 账号的头像，暂时约定为一个url
    change_chat_id_time: Optional[str] # 账号的更换聊天标识符时间
    public_key: str # 账号的公钥
    message_server: str # 账号使用的消息内容服务器的地址
    signature: str # 账号的签名
    
    class Config:
        orm_mode = True
    
# 账号更新请求
class AccountUpdate(AccountCreate):
    previous_public_key: Optional[str] # 账号的上一次公钥
    
# 账号同步请求（用于区块链同步）
class AccountSync(AccountCreate):
    create_at: str # 账号的创建时间
    update_at: str # 账号的更新时间
    
# 账号返回
class Account(AccountCreate):
    create_time: str # 账号的创建时间
    update_time: str # 账号的更新时间
    
# 账号列表返回
class AccountList(BaseModel):
    data: list[Account] # 账号列表