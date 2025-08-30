# app/crud/task.py
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.models.task import Task
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete

# Example CRUD functions
async def get_tasks(db: AsyncSession, skip: int = 0, limit: int = 100):
    result = await db.execute(select(Task).offset(skip).limit(limit))
    return result.scalars().all()

async def get_task_by_id(db: AsyncSession, task_id: int):
    result = await db.execute(select(Task).where(Task.id == task_id))
    return result.scalars().first()

async def create_task(db: AsyncSession, task: TaskCreate):
    db_task = Task(**task.dict())
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def update_task(db: AsyncSession, db_task: Task, task: TaskUpdate):
    for field, value in task.dict(exclude_unset=True).items():
        setattr(db_task, field, value)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task

async def delete_task(db: AsyncSession, db_task: Task):
    await db.delete(db_task)
    await db.commit()
