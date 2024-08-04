from fastapi import APIRouter
from fastapi import Depends,status,Response,HTTPException
from .. import schemas
from ..database import get_db
from ..models import User
from sqlalchemy.orm import Session

router = APIRouter(prefix='/user',tags=['users'])

@router.post('',status_code=status.HTTP_201_CREATED)
def createUser(user:schemas.UserBase,db:Session=Depends(get_db)):
    newUser = User(name=user.name,email=user.email,password=user.password)
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

@router.get('/{id}',response_model=schemas.User)
def getSingleUser(id,db:Session=Depends(get_db)):
    user = db.query(User).filter(User.id==id).first()
    return user