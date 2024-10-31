#model/node.py

from sqlalchemy import Column, String, DateTime, Boolean,Integer
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime, timezone
from .basemodel import BaseModel


class Node(BaseModel):
    """
    Node表用于存储连接到的节点信息
    """
    __tablename__ = 'nodes'
    
    # 节点地址
    address = Column(String, primary_key=True, nullable=False)
    
    # 节点端口
    port = Column(Integer, nullable=False)
    
    # 节点状态（在线/离线）
    status = Column(Boolean, default=True)
    
    # 节点延迟
    delay = Column(Integer, nullable=True)