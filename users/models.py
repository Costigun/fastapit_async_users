from database import Base
from sqlalchemy import Column, Integer, String, Boolean,ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)
    permission_id = Column(Integer,ForeignKey('permission.id'))

    permissions = relationship("Permission",back_populates='users')


class Permission(Base):
    __tablename__ = 'permission'
    id = Column(Integer, primary_key=True, index=True)
    rights = Column(String)

    users = relationship("User",back_populates='permissions')