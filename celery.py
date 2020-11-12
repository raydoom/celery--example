from __future__ import absolute_import, unicode_literals
from celery import Celery
from celery.schedules import crontab

app = Celery('celery-example',
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['celery-example.tasks'])

# Optional configuration, see the application user guide.
app.conf.update(
    result_expires=3600,
)

app.conf.beat_schedule={
    "each10s_task":{
        "task":"celery-example.tasks.add",
        "schedule":10, # 每10秒钟执行一次
        "args":(10,10)
    },
    "each1m_task": {
        "task": "celery-example.tasks.mul",
        "schedule": crontab(), # 每一分钟执行一次
        "args": (10, 10)
    },
    "each24hours_task": {
        "task": "celery-example.tasks.add",
        "schedule": crontab(hour=22), # 每24小时执行一次
        "args": (10, 10)
    }

}

if __name__ == '__main__':
    app.start()