celery计划任务

启动方式
celery -A celery-example beat

和work一起启动，只能启动一个worker节点
celery -A celery-example worker -B -s /tmp/celerybeat-schedule

指定celerybeat-schedule数据文件保存的位置
celery -A celery-example beat -s /tmp/celerybeat-schedule