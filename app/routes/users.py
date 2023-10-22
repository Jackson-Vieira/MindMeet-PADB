from fastapi import APIRouter, Depends, status
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from psycopg import Connection

from app.database.connection import get_db_connection
from app.usecases.users import UserUseCases

router = APIRouter(prefix='/users')


@router.get('')
def get_users(
    db_connection: Connection = Depends(get_db_connection)
):
    uc = UserUseCases(db_connection=db_connection)
    users = uc.get_all_users()
    print(users)
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(users))