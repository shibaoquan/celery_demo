import time

from celery import Celery
# app = Celery('tasks', broker='redis://root:123456@localhost', backend='redis://root:123456@localhost')
app = Celery("tasks")
app.config_from_object('celeryconfig')


@app.task()
def add(x, y):
    print(f"add:{x}, {y}, sleep....")
    time.sleep(3)
    return x + y


@app.task
def mul(x, y):
    print(f"mul:{x}, {y}, sleep....")
    return x * y