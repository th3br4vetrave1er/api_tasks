from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()
tasks = []  # список задач будем хранить в прамяти


class Task(BaseModel):        # Определяем структуру задачи
    title: str
    done: bool = False


@app.post('/tasks/')   # Добавить задачу
def add_task(task: Task):
    tasks.append(task)
    return {'message': 'Task added', 'task': task}


@app.get('/tasks/')  # Получить все задачи
def get_tasks():
    return {'tasks': tasks}


@app.get('/')  # Главная страница
def home():
    return {'message': 'Welcome to TASK API'}