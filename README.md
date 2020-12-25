
## celery 学习
### 官网文档
https://www.celerycn.io/yong-hu-zhi-nan/ren-wu-tasks/ri-zhi-logging


##### 发布定时任务
celery -A tasks beat --loglevel=info

##### 执行任务
celery -A tasks worker --loglevel=info 

##### 同时启动 
celery -A tasks beat --loglevel=info &  nohup celery -A tasks worker --loglevel=info & 

##### 任务进程关闭方法一
ps auxww|grep "celery worker"|grep -v grep|awk '{print $2}'|xargs kill -9
##### 任务进程关闭方法二
celery multi start w1 -A proj -l info
celery  multi restart w1 -A proj -l info

###### 异步关闭 立即返回
celery multi stop w1 -A proj -l info
###### 等待关闭操作完成
celery multi stopwait w1 -A proj -l info
