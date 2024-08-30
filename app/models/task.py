from fastapi import APIRouter
from app.backend.db import Base
from sqlalchemy import Column, ForeignKey, String, Integer, Boolean
from sqlalchemy.orm import relationship
from app.models import *

class Task(Base):
    __tablename__ = "tasks"
    __table_args__ = {'keep_existing': True}
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    priority = Column(Integer, default=0)
    slug = Column(String, unique=True, index=True)
    completed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True, index=True)


    user = relationship('User', back_populates='tasks')

from sqlalchemy.schema import CreateTable
print(CreateTable(Task.__table__))