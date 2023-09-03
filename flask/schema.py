from typing import Optional

from pydantic import BaseModel, validator

class CreateUser(BaseModel):
    name: str
    password: str
    
    @validator("password")
    def secure_password(cls, value):
        if len(value) <= 8:
            raise ValueError("Password is to short")
        return value

class UpdateUser(BaseModel):
    name: Optional[str]
    password: Optional[str]
    
    @validator("password")
    def secure_password(cls, value):
        if len(value) <= 8:
            raise ValueError("Password is to short")
        return value
    
class CreateAd(BaseModel):
    title: str
    description: str
    owner: int
    
    @validator("title")
    def title_length(cls, value):
        if len(value) > 50:
            raise ValueError("Title must be under 50 charachters")
        return value

class UpdateAd(BaseModel):
    title: Optional[str]
    description: Optional[str]
    
    @validator("title")
    def title_length(cls, value):
        if len(value) > 50:
            raise ValueError("Title must be under 50 charachters")
        return value