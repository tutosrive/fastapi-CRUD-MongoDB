from bson import ObjectId
from fastapi import HTTPException, Response, status
from app.models.user import User
from app.config.db import mong_conn
from app.schemas.user import user_entity, users_entity

class UserController:
    def __init__(self):
        pass

    def get_all_users(self) -> list[dict]:
        users: list[dict] = users_entity(mong_conn.local.user.find())
        return users

    def get_user(self, id: str) -> dict:
        user = mong_conn.local.user.find_one({'_id': ObjectId(id)})
        if user:
            return user_entity(user)
        self.__raise_404()
    
    def add_user(self, user: User) -> dict:
        result = mong_conn.local.user.insert_one(user)
        if result:
            __user = mong_conn.local.user.find_one({'_id': ObjectId(result.inserted_id)})
            __user_entity = user_entity(__user)
            return __user_entity
        raise HTTPException(status_code=400, detail="The user can't bee added!")
    
    def delete_user(self, id: str) -> Response:
        result = mong_conn.local.user.find_one_and_delete({'_id': ObjectId(id)})
        if result:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        self.__raise_404()
    
    def update_user(self, id: str, user: User) -> dict:
        result = mong_conn.local.user.find_one_and_update({'_id': ObjectId(id)}, {'$set': user})
        if result:
            __user = self.get_user(id)
            return __user
        self.__raise_404()
    
    def __raise_404(self):
        raise HTTPException(status_code=404, detail='User Not Found!')
