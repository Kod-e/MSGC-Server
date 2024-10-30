from sqlalchemy import Column, String, DateTime, Integer, Text
from sqlalchemy.orm import relationship
from .basemodel import BaseModel
import uuid

class Block(BaseModel):
    """
    Block表用于存储区块信息
    """
    __tablename__ = 'block'
    
    # 区块的时间戳，表示区块封装的时间,使用UTC+0时区 作为表的主键
    timestamp = Column(DateTime, nullable=False)
    
    # 区块的内容，存储过去10分钟内的Account的signature，每个signature之间安装ascii码排序
    content = Column(Text, nullable=False)
    
    # 上一个区块的哈希值，用于链式结构
    previous_hash = Column(String(64), nullable=False)
    
    # 当前区块的哈希值，用于验证区块的完整性
    current_hash = Column(String(64), nullable=False)
    
    # 区块的状态，表示是否已被广播并确认
    status = Column(String(10), nullable=False, default='pending')