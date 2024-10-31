#model/basemodel.py

from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Boolean, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import relationship, sessionmaker
from datetime import datetime, timezone

from storage.base import Base


class BaseModel(Base):
    __abstract__ = True

    #当model被创建时，自动更新created_at字段
    @declared_attr
    def created_at(cls):
        return Column(DateTime, default=lambda: datetime.now(timezone.utc))

    #当model被更新时，自动更新updated_at字段
    @declared_attr
    def updated_at(cls):
        return Column(DateTime, default=lambda: datetime.now(timezone.utc), onupdate=lambda: datetime.now(timezone.utc))