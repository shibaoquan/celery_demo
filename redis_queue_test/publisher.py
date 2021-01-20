# -*- coding: UTF-8 -*-
"""
@Author ：史保权
@Date   ：2020/12/25 5:41 下午
@Desc   ：
"""


import redis

client = redis.Redis(host="127.0.0.1", port=6379, password="123456", db=3)
print(client)

# 发布者

for _ in range(10):
    sub_count = client.publish("channel", f"this is value{_} of channel")  # 返回订阅着数量
    print(sub_count)




