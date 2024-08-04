from fastapi import APIRouter
from fastapi import Depends,status,Response
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from typing import List
from ..repository import blogs


router = APIRouter(prefix='/blog',tags=['blogs'])


@router.get('',response_model=List[schemas.Blog])
def all(db: Session = Depends(get_db)):
    return blogs.get_all(db)

@router.post('',status_code=status.HTTP_201_CREATED)
def create(blog:schemas.BlogBase,limit:int=10, db: Session = Depends(get_db)):
    return blogs.create(blog,db)

@router.get('/{id}')
def getSingle(id,res:Response,db:Session = Depends(get_db)):
    return blogs.getOne(id,res,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def delteBlog(id,db:Session = Depends(get_db)):
    return blogs.delete(id,db)

@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updateBlog(id,blogBody:schemas.BlogBase,db:Session = Depends(get_db)):
    return blogs.updateBlog(id,blogBody,db)