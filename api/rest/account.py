#api/rest/account.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from schemas import *
from service import *
from storage import *


#account路由
router = APIRouter(prefix="/account", tags=["account"])

#创建账号
@router.post("/create", response_model=AccountResponse)
def create_account(account: AccountCreate, session: Session = Depends(get_db)):
    """
    创建账号
    :param account: 账号创建请求
    :param session: 数据库会话
    :return: 返回创建的账号
    """
    try:
        return AccountService.create_account(account.identifier, account.nickname, account.avatar, account.public_key, account.message_server, account.signature, session)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))
    
#更新账号
@router.put("/update", response_model=AccountResponse)
def update_account(account: AccountUpdate, session: Session = Depends(get_db)):
    """
    更新账号
    :param account: 账号更新请求
    :param session: 数据库会话
    :return: 返回更新的账号
    """
    try:
        return AccountService.update_account(account.identifier, account.nickname, account.avatar, account.public_key, account.message_server, account.signature, session)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))

#通过identifier获取账号
@router.get("/get", response_model=AccountResponse)
def get_account(identifier: str, session: Session = Depends(get_db)):
    """
    通过identifier获取账号
    :param identifier: 账号的唯一标识符
    :param session: 数据库会话
    :return: 返回获取的账号
    """
    try:
        return AccountService.get_account_by_identifier(identifier=identifier, session=session)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))
    
#通过nickname获取账号
@router.get("/get_by_nickname", response_model=list[AccountResponse])
def get_account_by_nickname(nickname: str, session: Session = Depends(get_db)):
    """
    通过nickname获取账号
    :param nickname: 账号的昵称
    :param session: 数据库会话
    :return: 返回获取的账号
    """
    try:
        return AccountService.get_accounts_by_nickname(nickname=nickname, session=session)
    except Exception as e:
        # 如果e.message存在，返回400，detail为e.message，否则返回500，detail为str(e)
        raise HTTPException(status_code=400 if hasattr(e, 'message') else 500, detail=e.message if hasattr(e, 'message') else str(e))