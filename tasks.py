from __future__ import absolute_import, unicode_literals
from .celery import app

@app.task
def add(x, y):
    print('add.....')
    return x + y

@app.task
def mul(x, y):
    print('mul.....')
    return x * y

@app.task
def xsum(numbers):
    return sum(numbers)