# -*- coding: UTF-8 -*-
"""
@Author ：史保权
@Date   ：2020/12/20 9:52 下午
@Desc   ：
"""
from datetime import timedelta

broker_url = 'redis://root:123456@localhost/0'
# result_backend = 'redis://root:123456@localhost/1'

task_serializer = 'json'
result_serializer = 'json'
accept_content = ['json']
timezone = 'Asia/Shanghai'
enable_utc = True
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）


# 针对任务进行限速
task_annotations = {
    'tasks.add': {'rate_limit': '10/m'}
}

# 导入任务模块
imports = [
    "tasks",
]

# 定时任务配置
beat_schedule = {
    'add-every-30-seconds': {
        'task': 'tasks.add',  # 任务
        "schedule": timedelta(seconds=5),
        # "schedule": 10,
        'args': (1, 1)  # 任务参数
    },
}

# "schedule": crontab（）与crontab的语法基本一致
# "schedule": crontab(minute="*/10",  # 每十分钟执行
# "schedule": crontab(minute="*/1"),   # 每分钟执行
# "schedule": crontab(minute=0, hour="*/1"),    # 每小时执行
