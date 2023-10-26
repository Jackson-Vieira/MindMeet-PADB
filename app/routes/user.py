from fastapi import APIRouter, Depends
from psycopg import Connection

from app.database.connection import get_db_connection
from app.usecases.user import UserUseCases

router = APIRouter(prefix='/users')


@router.get('')
def get_users(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection=db_connection)
    users = uc.get_all_users()
    return users