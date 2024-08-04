from sqlalchemy.orm import Session
from fastapi import status,HTTPException
from ..models import Blog


def get_all(db:Session):
    blogs = db.query(Blog).order_by(Blog.id.desc()).all()
    return blogs

def create(blog,db:Session):
    new_blog = Blog(title=blog.title,body=blog.body,isActive=blog.isActive,userId=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def getOne(id,res,db:Session):
    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
        # res.status_code=status.HTTP_404_NOT_FOUND
        # return {'detail':f'Blog with {id} not found'}
    return blog

def delete(id,db:Session):
    blog = db.query(Blog).filter(Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    db.query(Blog).filter(Blog.id==id).delete(synchronize_session=False)
    db.commit()
    return {'message':'Blog deleted'}

def updateBlog(id,blogBody,db:Session):
    blog = db.query(Blog).filter(Blog.id==id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Blog with {id} not found')
    blog.update(dict(blogBody), synchronize_session=False)
    db.commit()
    return 'done'
