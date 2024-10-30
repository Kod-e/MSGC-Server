from .basemodel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship
import uuid


class Account(BaseModel):
    """
    Account表用于存储账户信息，一般情况下这个表需要尽可能的短
    在区块链网络中，这个表的数据会被复制到每个节点上
    """
    __tablename__ = 'account'
    
    # 唯一标识符，一般是一个合法的uuid，用于标识一个account，在区块链网络中这个字段是唯一的
    # 在数据库中不使用unique约束，在公钥更换的过程中identifier会和之前的相同
    identifier = Column(String(36), index=True, nullable=False)
    
    #昵称，可以是任意字符串，一般不建议超过128个字符，暂时约定UTF-8编码
    nickname = Column(String(128), nullable=False)
    
    # 约定的更换聊天标识符时间，目前协议可以约定三种字符串，分别代表每周一和每月一号，以及在UTC+0时区的每天的0点
    # D1代表每天的0点更换，W1代表每周一更换，M1代表每月一号更换
    # 或者可以设置为空，表示不更换
    # 双方添加好友时如果标识符不一致，使用最短的时间，如果一方为空，使用另一方的时间
    # 建议客户端请求消息时向前获取一段时间的消息，以防止消息丢失
    change_chat_id_time = Column(String(2), nullable=True)
    
    # 公钥
    public_key = Column(Text, nullable=False)
    
    #这个account使用的消息内容服务器的地址
    message_server = Column(String, nullable=False)
    
    # 签名，用于验证这个account的合法性，使用上一次的公钥进行签名
    # 如果是第一次添加，在这个顺序中忽略公钥并且使用刚刚生成的公钥进行签名
    # 如果某个字段不存在就不参与签名
    # 格式为 identifier + nickname + public_key + change_chat_id_time + message_server
    signature = Column(Text, nullable=True)
    