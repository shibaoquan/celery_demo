# -*- coding: UTF-8 -*-
"""
@Author ：史保权
@Date   ：2021/1/20 11:06 上午
@Desc   ：
"""
import time

import redis

client = redis.Redis(host="127.0.0.1", port=6379, password="123456", db=5)
print(client)

# 生产者
for _ in range(10):
    client.lpush("key", _)


# 消费者
while True:
    value = client.rpop("key")
    print(value)
    time.sleep(3)

