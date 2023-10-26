from fastapi import FastAPI

from app.database.connection import start_db
from app.routes.agenda import router as agenda_router
from app.routes.appointment import router as appointments_router
from app.routes.request_appointment import router as requests_appointment_router
from app.routes.user import router as users_router

app = FastAPI()
start_db()

@app.get("/")
async def get_health_status():
    return {"mindmeet": "online"}

app.include_router(users_router)
app.include_router(agenda_router)
app.include_router(appointments_router)
app.include_router(requests_appointment_router)