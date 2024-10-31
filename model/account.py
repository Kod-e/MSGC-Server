#model/account.py

from .basemodel import BaseModel
from sqlalchemy import Column, Integer, String, ForeignKey,Text
from sqlalchemy.orm import relationship
import uuid
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.serialization import load_pem_public_key
from cryptography.exceptions import InvalidSignature


class Account(BaseModel):
    """
    Account表用于存储账户信息，一般情况下这个表需要尽可能的短
    在区块链网络中，这个表的数据会被复制到每个节点上
    """
    __tablename__ = 'account'
    
    # 唯一标识符，一般是一个合法的uuid，用于标识一个account，在区块链网络中这个字段是唯一的
    # 在数据库中不使用unique约束，在公钥更换的过程中identifier会和之前的相同
    identifier = Column(String(36),primary_key=True, index=True, nullable=False)
    
    #昵称，可以是任意字符串，一般不建议超过128个字符，暂时约定UTF-8编码
    nickname = Column(String(128), nullable=False)
    
    # 约定的更换聊天标识符时间，目前协议可以约定三种字符串，分别代表每周一和每月一号，以及在UTC+0时区的每天的0点
    # D1代表每天的0点更换，W1代表每周一更换，M1代表每月一号更换
    # 或者可以设置为空，表示不更换
    # 双方添加好友时如果标识符不一致，使用最短的时间，如果一方为空，使用另一方的时间
    # 建议客户端请求消息时向前获取一段时间的消息，以防止消息丢失
    change_chat_id_time = Column(String(2), nullable=True)
    
    # 账号的头像，暂定为一个url
    avatar = Column(String(256), nullable=True)
    
    # 公钥，暂时约定为ECDSA，使用P-256曲线，使用PEM格式存储
    public_key = Column(String(88), nullable=False)
    
    # 上一次的公钥，暂时约定为ECDSA，使用P-256曲线, 使用PEM格式存储
    previous_public_key = Column(String(88), nullable=True)
    
    #这个account使用的消息内容服务器的地址
    message_server = Column(String(256), nullable=False)
    
    # 签名，用于验证这个account的合法性，使用上一次的公钥进行签名
    # 如果是第一次添加，在这个顺序中忽略公钥并且使用刚刚生成的公钥进行签名
    # 如果某个字段不存在就不参与签名
    # 参与签名的字段为identifier,nickname,avatar,chang_chat_id_time,message_server 如果previous_public_key存在，public_key参与签名
    # 签名的数据按照ascii码排序
    # 验证算法为ECDSA，使用SHA256哈希算法
    signature = Column(Text, nullable=True)
    
    # 签名校验函数
    def verify_signature(self) -> bool:
        """
        校验账户的签名
        :return: 返回校验结果
        """
        data =  {
            'identifier': self.identifier,
            'nickname': self.nickname,
            'change_chat_id_time': self.change_chat_id_time,
            'message_server': self.message_server,
        }
        # 检测previous_public_key是否存在
        if self.previous_public_key:
            data['public_key'] = self.public_key
        # 检测avatar是否存在
        if self.avatar:
            data['avatar'] = self.avatar
            
        # 按照ascii码排序
        data = dict(sorted(data.items(), key=lambda x: x[0]))
        
        # 将数据转换为字符串并编码
        data_str = ''.join(f'{key}:{value}' for key, value in data.items()).encode('utf-8')
        
        try:
            # 加载公钥
            public_key = load_pem_public_key(self.previous_public_key.encode('utf-8') if self.previous_public_key else self.public_key.encode('utf-8'))
            
            # 验证签名
            public_key.verify(
                bytes.fromhex(self.signature),
                data_str,
                ec.ECDSA(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False