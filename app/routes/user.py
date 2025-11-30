from fastapi import APIRouter, HTTPException
from app.models.user import User
from app.controllers.user import UserController

user_router = APIRouter(tags=['User'], prefix='/users')
user_ctrl = UserController()

@user_router.get('/', response_model=list[User])
def get_all_users():
    users = user_ctrl.get_all_users()
    return users

@user_router.get('/{id}', response_model=User)
def get_user(id: str):
    try:
        return user_ctrl.get_user(id)
    except HTTPException as e:
        raise e

@user_router.post('/', response_model=User)
def add_user(user: User) -> dict:
    try:
        return user_ctrl.add_user(user.model_dump())
    except HTTPException as e:
        raise e
    
@user_router.put('/{id}', response_model=User)
def update_user(id: str, user_updated: User) -> dict:
    try:
        return user_ctrl.update_user(id, user_updated.model_dump())
    except HTTPException as e:
        raise e
    
@user_router.delete('/{id}')
def delete_user(id: str) -> dict:
    try:
        return user_ctrl.delete_user(id)
    except HTTPException as e:
        raise e