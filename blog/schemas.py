from pydantic import BaseModel
from typing import List,Optional

class BlogBase(BaseModel):
    title:str
    body:str
    isActive:bool
    userId:int
    
# class BlogCreate(BlogBase):
#     pass

class UserBase(BaseModel):
    name:str
    email:str
    
# class UserCreate(UserBase):
#     password: str
    
class Blog(BlogBase):
    id:int
    user: Optional[UserBase]
    class Config():
        from_attributes = True
      
class User(UserBase):
    id:int
    blogs:List[BlogBase]=[]
    class Config():
        from_attributes = True
        

        
