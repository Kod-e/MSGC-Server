from model import *
from storage import *
from exceptions import *
from sqlalchemy.orm import Session
import uuid
from datetime import datetime

class NotificationService():
    
    # 创建一个新的请求
    @staticmethod
    def create_notification(account_identifier:str, content:str,session:Session,identifier:str=None) -> Notification:
        """
        创建一个新的请求
        :param identifier: 请求的唯一标识符
        :param account_identifier: 请求的账户的唯一标识符
        :param content: 请求的内容
        :return: 返回创建的请求，如果请求已经存在返回None
        """
        # 如果identifier为空，model自带的lambda函数会生成一个uuid
        new_notification:Notification
        if identifier is None:
            new_notification = Notification(account_identifier=account_identifier, content=content)
        else:
            new_notification = Notification(identifier=identifier,account_identifier=account_identifier, content=content)
            
        session.add(new_notification)
        session.commit()
        
        return new_notification
    
    # 查询某个identifier在某个time之后的所有请求
    @staticmethod
    def get_notifications_after_time(account_identifier:str, session:Session,time:datetime=None) -> list[Notification]:
        """
        查询某个identifier在某个time之后的所有请求
        :param account_identifier: 请求的账户的唯一标识符
        :param time: 请求的时间
        :return: 返回请求列表
        """
        if time is None:
            return session.query(Notification).filter(Notification.account_identifier == account_identifier).all()
        else:
            return session.query(Notification).filter(Notification.account_identifier == account_identifier).filter(Notification.created_at > time).all()