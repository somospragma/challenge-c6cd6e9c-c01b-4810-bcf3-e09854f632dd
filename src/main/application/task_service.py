from..domain.task import Task, TaskStatus
from..infrastructure.database import TaskRepository

class TaskService:
    def __init__(self, task_repo: TaskRepository):
        self.task_repo = task_repo

    def create_task(self, task: Task):
        return self.task_repo.create_task(task)

    def update_task(self, task_id: int, task: Task):
        return self.task_repo.update_task(task_id, task)

    def delete_task(self, task_id: int):
        return self.task_repo.delete_task(task_id)