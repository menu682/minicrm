import uvicorn
from fastapi import FastAPI
from DB import lifespan

from controller import user_controller, status_controller, role_controller


app = FastAPI(lifespan = lifespan)

app.include_router(user_controller.router)
app.include_router(status_controller.router)
app.include_router(role_controller.router)


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
