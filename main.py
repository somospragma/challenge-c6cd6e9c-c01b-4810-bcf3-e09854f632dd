from fastapi import FastAPI
from src.main.api.task_endpoints import router as task_router

app = FastAPI()

app.include_router(task_router)