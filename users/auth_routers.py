from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from starlette import status
import models, hashing, jwt_token
from database import get_db

router = APIRouter(
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm=Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='ivalid credentials')
    if not hashing.Hash.verify(user.password, request.password):
        print(request.password)
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Incorrect password')

    access_token = jwt_token.create_access_token(
        data={"sub": user.username},
    )
    return {"access_token": access_token, "token_type": "bearer"}
