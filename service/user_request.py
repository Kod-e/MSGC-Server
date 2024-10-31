from model import *
from storage import *
from exceptions import *
from sqlalchemy.orm import Session
import uuid

class UserRequestService():
    
    # 创建一个新的请求
    @staticmethod
    def create_request(account_identifier:str, content:str,session:Session,identifier:str=None) -> UserRequest:
        """
        创建一个新的请求
        :param identifier: 请求的唯一标识符
        :param account_identifier: 请求的账户的唯一标识符
        :param content: 请求的内容
        :return: 返回创建的请求，如果请求已经存在返回None
        """
        # 如果identifier为空，model自带的lambda函数会生成一个uuid
        user_request:UserRequest
        if identifier is None:
            new_request = UserRequest(account_identifier=account_identifier, content=content)
        else:
            new_request = UserRequest(identifier=identifier,account_identifier=account_identifier, content=content)
            
        session.add(new_request)
        session.commit()
        
        return new_request