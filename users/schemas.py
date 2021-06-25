from typing import Optional

from pydantic import BaseModel


class User(BaseModel):
    username: str
    email: str
    password: str
    permission_id: int


class UserDetail(BaseModel):
    username: str
    email: str
    permission_id: int

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserInDB(User):
    hashed_password: str
