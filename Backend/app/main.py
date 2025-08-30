# backend/main.py
from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.database import engine, Base, get_db
from app.models.task import Task as TaskModel
from app.schemas.task import TaskCreate, TaskUpdate, TaskOut
from app.crud.task import get_tasks, create_task, get_task_by_id, update_task, delete_task

app = FastAPI(
    title="To-Do App API",
    version="1.0.0",
    description="Simple CRUD To-Do app for Cambium AI task"
)

# Allow CORS from frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize database tables on startup
@app.on_event("startup")
async def startup_event():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# Root and health check
@app.get("/")
async def root():
    return {"message": "To-Do App API", "version": "1.0.0"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "database": "connected"}

# CRUD endpoints
@app.get("/tasks", response_model=list[TaskOut])
async def read_tasks(skip: int = 0, limit: int = 100, db: AsyncSession = Depends(get_db)):
    return await get_tasks(db, skip=skip, limit=limit)

@app.post("/tasks", response_model=TaskOut, status_code=201)
async def create_task_endpoint(task: TaskCreate, db: AsyncSession = Depends(get_db)):
    return await create_task(db, task)

@app.put("/tasks/{task_id}", response_model=TaskOut)
async def update_task_endpoint(task_id: int, task: TaskUpdate, db: AsyncSession = Depends(get_db)):
    db_task = await get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return await update_task(db, db_task, task)

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task_endpoint(task_id: int, db: AsyncSession = Depends(get_db)):
    db_task = await get_task_by_id(db, task_id)
    if not db_task:
        raise HTTPException(status_code=404, detail="Task not found")
    await delete_task(db, db_task)
    return {"success": True}
