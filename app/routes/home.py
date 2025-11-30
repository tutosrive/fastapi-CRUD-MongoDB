from fastapi import APIRouter, Response

home_router = APIRouter()

@home_router.get('/', tags=['General'])
def get_home() -> dict:
    return {
        'message': "You welcome to the FastAPI + MongoDB REST API"
    }