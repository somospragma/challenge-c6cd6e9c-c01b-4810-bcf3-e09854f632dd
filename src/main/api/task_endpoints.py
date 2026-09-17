from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from..application.task_service import TaskService
from..domain.task import Task, TaskStatus
from..infrastructure.database import TaskRepository

router = APIRouter()

def get_task_service():
    task_repo = TaskRepository()
    return TaskService(task_repo)

@router.post('/tasks/', response_model=Task)
async def create_task(task: Task, task_service: TaskService = Depends(get_task_service)):
    return task_service.create_task(task)

@router.put('/tasks/{task_id}', response_model=Task)
async def update_task(task_id: int, task: Task, task_service: TaskService = Depends(get_task_service)):
    updated_task = task_service.update_task(task_id, task)
    if updated_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return updated_task

@router.delete('/tasks/{task_id}', response_model=Task)
async def delete_task(task_id: int, task_service: TaskService = Depends(get_task_service)):
    deleted_task = task_service.delete_task(task_id)
    if deleted_task is None:
        raise HTTPException(status_code=404, detail='Task not found')
    return deleted_task