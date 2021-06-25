from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status
import schemas, database, models, hashing, oauth
from typing import List

router = APIRouter(
    tags=['User']
)


@router.get('/user', status_code=status.HTTP_200_OK, response_model=List[schemas.UserDetail])
async def all_user(db: Session = Depends(database.get_db), ):
    users = db.query(models.User).all()
    return users


@router.post('/user', status_code=status.HTTP_201_CREATED, response_model=schemas.UserDetail)
async def create_user(request: schemas.User, db: Session = Depends(database.get_db),
                      current_user: schemas.User = Depends(oauth.get_current_user)):
    permission = db.query(models.Permission).filter(models.Permission.id == current_user.permission_id).first()
    if permission.rights == 'superuser':
        new_user = models.User(username=request.username, email=request.email,
                               password=hashing.Hash.bcrypt(request.password), permission_id=request.permission_id)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='no permissions')


@router.get('/user/{id}', status_code=status.HTTP_200_OK, response_model=schemas.UserDetail)
async def user_detail(id, db: Session = Depends(database.get_db),
                      current_user: schemas.UserDetail = Depends(oauth.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    return user


@router.delete('/user/{id}', status_code=status.HTTP_204_NO_CONTENT)
async def destroy(id, db: Session = Depends(database.get_db),
                  current_user: schemas.UserDetail = Depends(oauth.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id)
    # get current user permission
    permission = db.query(models.Permission).filter(models.Permission.id == current_user.permission_id).first()
    if permission.rights == 'superuser':
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found!')
        user.delete(synchronize_session=False)
        db.commit()
        return {'data': f'User with {id} id was successfully deleted!'}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail='no permissions to delete!')


@router.put('/user/{id}', status_code=status.HTTP_202_ACCEPTED)
async def update(id, request: schemas.UserDetail, db: Session = Depends(database.get_db),
                 current_user: schemas.UserDetail = Depends(oauth.get_current_user)):
    user = db.query(models.User).filter(models.User.id == id)
    # get current user permission
    permission = db.query(models.Permission).filter(models.Permission.id == current_user.permission_id).first()
    if permission.rights == 'superuser':
        if not user.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'User with id {id} not found!')
        user.update(request.dict())
        db.commit()
        return {'detail': 'updated!'}
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f'no permissions to update')
