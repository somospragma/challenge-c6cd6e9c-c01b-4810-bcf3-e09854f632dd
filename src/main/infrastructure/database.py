from sqlalchemy import create_engine, Column, Integer, String, Enum, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from..domain.task import Task, TaskStatus

Base = declarative_base()

class TaskModel(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)
    status = Column(Enum(TaskStatus))
    due_date = Column(DateTime)

engine = create_engine('sqlite:///./test.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

class TaskRepository:
    def __init__(self):
        self.db = SessionLocal()

    def create_task(self, task: Task):
        db_task = TaskModel(**task.dict())
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return db_task

    def update_task(self, task_id: int, task: Task):
        db_task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            for key, value in task.dict().items():
                setattr(db_task, key, value)
            self.db.commit()
            self.db.refresh(db_task)
            return db_task
        return None

    def delete_task(self, task_id: int):
        db_task = self.db.query(TaskModel).filter(TaskModel.id == task_id).first()
        if db_task:
            self.db.delete(db_task)
            self.db.commit()
            return db_task
        return None