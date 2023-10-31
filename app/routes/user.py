from fastapi import APIRouter, Depends, Response, status
from psycopg import Connection

from app.database.connection import get_db_connection
from app.schemas.user import UserCreate
from app.usecases.user import UserUseCases

router = APIRouter(tags=["Users"],prefix='/users')


@router.get('')
def get_users(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection=db_connection)
    users = uc.get_all_users()
    return users

@router.post('')
def create_user(
    user: UserCreate,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection=db_connection)
    uc.create_user(user)
    return Response(status_code=status.HTTP_201_CREATED)

@router.get('/{user_id}')
def get_user_id(
    user_id: int,
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection)
    user = uc.get_user_by_id(user_id)
    return user