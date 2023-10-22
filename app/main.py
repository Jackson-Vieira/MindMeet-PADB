from fastapi import FastAPI

from app.database.connection import start_db
from app.routes.users import router as users_router

app = FastAPI()
start_db()

@app.get("/")
async def get_health_status():
    return {"mindmeet": "online"}

app.include_router(users_router)