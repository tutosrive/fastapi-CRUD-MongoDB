from bson import ObjectId
from fastapi import HTTPException, Response, status
from app.models.task import Task, TaskUpdate
from app.config.db import mong_conn
from app.schemas.task import task_entity, tasks_entity, task_update_entity

class TaskController:
    def __init__(self):
        pass

    def get_all_tasks(self) -> list[dict]:
        tasks: list[dict] = tasks_entity(mong_conn.local.task.find())
        return tasks

    def get_task(self, id: str) -> dict:
        task = mong_conn.local.task.find_one({'_id': ObjectId(id)})
        if task:
            return task_entity(task)
        self.__raise_404()
    
    def add_task(self, task: Task) -> dict:
        result = mong_conn.local.task.insert_one(task)
        if result:
            __task = mong_conn.local.task.find_one({'_id': ObjectId(result.inserted_id)})
            __task_entity = task_entity(__task)
            return __task_entity
        raise HTTPException(status_code=400, detail="The task can't bee added!")
    
    def delete_task(self, id: str) -> Response:
        result = mong_conn.local.task.find_one_and_delete({'_id': ObjectId(id)})
        if result:
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        self.__raise_404()
    
    def update_task(self, id: str, task: TaskUpdate) -> dict:
        task = task_update_entity(task)
        result = mong_conn.local.task.find_one_and_update({'_id': ObjectId(id)}, {'$set': task})
        if result:
            __task = self.get_task(id)
            return __task
        self.__raise_404()
    
    def __raise_404(self):
        raise HTTPException(status_code=404, detail='Task Not Found!')
