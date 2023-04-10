from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint


class PostBase(BaseModel):
    title: str 
    content: str  
    published: bool = True
    class Config:
        orm_mode = True

class PostCreate(PostBase):
    pass

class Userout(BaseModel):
    id: int 
    email: EmailStr 
    created_at: datetime

    class Config:
        orm_mode = True
        
class Post(PostBase):
    id: int 
    created_at: datetime
    owner_id: int 
    owner: Userout

    class Config:
        orm_mode =True

class PostOut(PostBase):
    Post: Post
    vote: int 

    class config:
        orm_mode = True

class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str  
    token_types: str

class TokenData(BaseModel):
    id: Optional[str] = None

