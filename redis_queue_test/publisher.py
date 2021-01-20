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

# 发布者
for _ in range(10):
    sub_count = client.publish("channel", f"this is value{_} of channel")  # 返回订阅着数量
    print(sub_count)

# 发布的数据存储在内存队列，暂时缓存。然后发给订阅者，如果订阅者没准备好，那么会错过这条信息。如果期间发生宕机，重启后队列中的数据就会丢失
