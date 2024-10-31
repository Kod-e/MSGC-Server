#model/user_request.py

from .basemodel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship
import uuid


class Notification(BaseModel):
    """
    Request表用于存储请求信息
    在区块链网络中，这个表的数据会被复制到每个节点上
    这个表的内容可以不用长时间保存
    """
    __tablename__ = 'user_request'
    # 唯一标识符，一般是一个合法的uuid，用于标识一个request，在区块链网络中这个字段是唯一的，请求不存在签名更改机制，所以使用unique约束
    # 如果不存在默认使用uuid4生成
    identifier = Column(String(36), index=True, nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    # request指向的account的identifier
    account_identifier = Column(String(36), ForeignKey('account.identifier'), nullable=False)
    # 请求的内容，一般用被请求者的公钥加密
    content = Column(Text, nullable=False)

    