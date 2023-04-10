from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List, Optional
from sqlalchemy import func

router = APIRouter(
    prefix="/posts", 
    tags=['Posts']
)
# , response_model=List[schemas.PostOut]
@router.get("/", response_model=List[schemas.Post])
def get_posts(db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user),
              limit: int = 10, skip: int=0, search: Optional[str] = ""):
    # cursor.execute("""SELECT * FROM post""")
    # posts = cursor.fetchall()
    # print(posts)
    posts = db.query(models.Post).filter(
       models.Post.title.contains(search)).limit(limit).offset(skip).all()
    
    #results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(
    #    models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    

    return posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), 
                 current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""INSERT INTO post (title, content, published) VALUES (%s, %s, %s) 
    # RETURNING * """, (post.title, post.content, post.published))
    # created_posts = cursor.fetchone()
    # conn.commit()
    print(current_user.email)
    new_posts = models.Post(owner_id=current_user.id, **post.dict())
    db.add(new_posts)
    db.commit()
    db.refresh(new_posts)
    return new_posts

@router.get("/{id}", response_model=schemas.Post)
def get_posts(id: int, db: Session = Depends(get_db),
              current_user: int = Depends(oauth2.get_current_user)):    #id: int
    # cursor.execute("""SELECT * FROM post WHERE id =%s """, (str(id)))
    # post = cursor.fetchone()
    posts = db.query(models.Post).filter(models.Post.id == id).first()
    if not posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} was not found')
    return posts

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    #deleting a post with an index from an array
    # cursor.execute("""DELETE FROM post WHERE id = %s RETURNING * """, (str(id)))
    # deleted_post = cursor.fetchone()
    # conn.commit()
    posts_query = db.query(models.Post).filter(models.Post.id == id)
    posts = posts_query.first()

    if posts == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not exist')
    if posts.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    posts_query.delete(synchronize_session=False)
    db.commit()
    
    return Response(status_code= status.HTTP_204_NO_CONTENT)

@router.put("/{id}", response_model=schemas.Post)
def update_post(id: int, updated_post: schemas.PostCreate, db: Session = Depends(get_db),
                current_user: int = Depends(oauth2.get_current_user)):
    # cursor.execute("""UPDATE POST SET title = %s, content = %s, published = %s WHERE id=%s RETURNING * """,
    #                (post.title, post.content, post.published, str(id)))
    # updated_post = cursor.fetchone()
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id: {id} does not exist')
    
    if post.owner_id != current_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Not authorized to perform requested action")
    
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()

    return post_query.first()