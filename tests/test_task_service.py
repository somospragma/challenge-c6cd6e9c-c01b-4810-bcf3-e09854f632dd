from unittest.mock import Mock
from src.main.application.task_service import TaskService
from src.main.domain.task import Task, TaskStatus

def test_create_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    task = Task(title="Test Task", description="Test Description", status=TaskStatus.PENDING, due_date=datetime.now())
    created_task = task_service.create_task(task)
    assert created_task.title == "Test Task"

def test_update_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    task = Task(title="Test Task", description="Test Description", status=TaskStatus.PENDING, due_date=datetime.now())
    updated_task = task_service.update_task(1, task)
    assert updated_task is not None

def test_delete_task():
    task_repo_mock = Mock()
    task_service = TaskService(task_repo_mock)
    deleted_task = task_service.delete_task(1)
    assert deleted_task is not None