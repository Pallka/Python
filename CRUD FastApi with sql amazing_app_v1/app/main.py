import uvicorn
from fastapi import FastAPI

from app import models
from app.database import engine
from app.routers.users import users_router
from app.routers.records import records_router

models.Base.metadata.create_all(bind=engine)


app = FastAPI()
app.include_router(users_router)
app.include_router(records_router)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8080)
