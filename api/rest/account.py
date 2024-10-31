#api/rest/account.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from service import *
from storage import *


#account路由
router = APIRouter(prefix="/account", tags=["account"])

#创建账号
@router.post("/create", response_model=Account)
def create_account(account: AccountCreate, session: Session = Depends(get_db)):
    """
    创建账号
    :param account: 账号创建请求
    :param session: 数据库会话
    :return: 返回创建的账号
    """
    return AccountService.create_account(account.identifier, account.nickname, account.avatar, account.public_key, account.message_server, account.signature, session)
