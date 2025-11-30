from fastapi import FastAPI

from app.routes.home import home_router
from app.routes.user import user_router
from app.routes.task import task_router
from app.config.docs import api_tags

app = FastAPI(
    title='FASTAPI + MongoDB',
    description='Learning FastAPI with MongoDB ...',
    version='2025.0.1.0',
    openapi_tags=api_tags
)

app.include_router(home_router)
app.include_router(user_router)
app.include_router(task_router)