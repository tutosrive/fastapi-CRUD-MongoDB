from fastapi import APIRouter, HTTPException
from app.models.task import Task, TaskUpdate
from app.controllers.task import TaskController

task_router = APIRouter(tags=['Task'], prefix='/tasks')
task_ctrl = TaskController()

@task_router.get('/', response_model=list[Task])
def get_all_tasks():
    tasks = task_ctrl.get_all_tasks()
    return tasks

@task_router.get('/{id}', response_model=Task)
def get_task(id: str):
    try:
        return task_ctrl.get_task(id)
    except HTTPException as e:
        raise e

@task_router.post('/', response_model=Task)
def add_task(task: Task) -> dict:
    try:
        return task_ctrl.add_task(task.model_dump())
    except HTTPException as e:
        raise e
    
@task_router.put('/{id}', response_model=Task)
def update_task(id: str, task_updated: TaskUpdate) -> dict:
    try:
        return task_ctrl.update_task(id, task_updated.model_dump())
    except HTTPException as e:
        raise e
    
@task_router.delete('/{id}')
def delete_task(id: str) -> dict:
    try:
        return task_ctrl.delete_task(id)
    except HTTPException as e:
        raise e