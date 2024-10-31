from model import *
from storage import *
from exceptions import *
from sqlalchemy.orm import Session
import uuid
class AccountService():
    
    # 创建一个新的账户
    @staticmethod
    def create_account(identifier:str, nickname:str, public_key:str, message_server:str, signature:str,session:Session) -> Account:
        """
        创建一个新的账户
        :param uuid: 账户的唯一标识符
        :param nickname: 账户的昵称
        :param public_key: 账户的公钥
        :param message_server: 账户的消息服务器地址
        :param signature: 账户的签名
        :return: 返回创建的账户，如果账户已经存在返回None
        """
        # 检查账户是否存在
        account = session.query(Account).filter(Account.identifier == identifier).first()
        if account is not None:
            # 抛出异常
            raise AccountExistException()
        account = Account(identifier=uuid, nickname=nickname, public_key=public_key, message_server=message_server, signature=signature)
        if account.verify_signature():
            session.add(account)
            session.commit()
            return account
        else:
            # 抛出异常
            raise AccountSignatureVerifyException()