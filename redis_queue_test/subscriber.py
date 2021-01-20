# -*- coding: UTF-8 -*-
"""
@Author ：史保权
@Date   ：2020/12/25 5:41 下午
@Desc   ：
"""
import time

import redis

client = redis.Redis(host="127.0.0.1", port=6379, password="123456", db=3)
print(client)

# 第一步 生成一个订阅者对象
pubsub = client.pubsub()

# 订阅一个主题
pubsub.subscribe("channel")

while True:
    time.sleep(5)
    print("working~~~")
    msg = pubsub.parse_response()
    print(msg)


