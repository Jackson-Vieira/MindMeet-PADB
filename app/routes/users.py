from fastapi import APIRouter, Depends, status, Response
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from psycopg import Connection

from app.database.connection import get_db_connection
from app.usecases.users import UserUseCases
from app.schemas.users import UserCreate
from app.schemas.users import User

router = APIRouter(prefix='/users')


@router.get('')
def get_users(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection=db_connection)
    users = uc.get_all_users()
    print(users)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users))

@router.get('/{user_id}')
def get_user_id(
    user_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection)
    appointment = uc.get_user_id(user_id)
    return appointment

@router.post('')
def create_user(
    create_user: UserCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection)
    uc.create_user(create_user)
    return Response(status_code=status.HTTP_201_CREATED)

@router.delete('/{user_id}')
def delete_user(
    users: User,
    user_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection)
    uc.delete_user_id(user_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{user_id}')
def update_user(
    user_id: int,
    user: UserCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection)
    uc.update_user(user_id, user)
    return Response(status_code=status.HTTP_204_NO_CONTENT)