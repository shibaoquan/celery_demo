import tasks

if __name__ == '__main__':

    # 调用任务

    for _ in range(3):
        import time
        # time.sleep(3)
        tasks.add.delay(_, _+1)
        tasks.mul.delay(_, _+2)



