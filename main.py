import uvicorn
from fastapi import FastAPI
from controller import user_controller
from sqlmodel import create_engine, SQLModel

app = FastAPI()
app.include_router(user_controller.router)


try:
    DATABASE_URL = "sqlite:///database.db"
    engine = create_engine(DATABASE_URL, echo=True)
    SQLModel.metadata.create_all(engine)
except Exception as e:
    e.add_note("DB connection failed")


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
