# -*- coding: UTF-8 -*-
"""
@Author ：史保权
@Date   ：2020/12/25 5:41 下午
@Desc   ：
"""
import time

import redis

client = redis.Redis(host="127.0.0.1", port=6379, password="123456", db=5)
print(client)

# 第一步 生成一个订阅者对象
pubsub = client.pubsub()

# 订阅一个主题
pubsub.subscribe("channel")

while True:
    print("working~~~")
    msg = pubsub.parse_response()  # 自己会阻塞，直到获取到值
    print(f"获取到的msg：{msg}")





