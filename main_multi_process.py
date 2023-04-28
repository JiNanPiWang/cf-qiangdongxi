import multiprocessing

from utils import get_time

import real_events.JuBaoPen4yue1_2023_4 as work1
import real_events.JuBaoPen4yue2_2023_4 as work2

def run1():
    x = work1.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run()

def run2():
    x = work2.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run()


if __name__ == '__main__':
    # 创建进程
    processes = [
        multiprocessing.Process(target=run1),
        multiprocessing.Process(target=run2)
    ]

    # 启动进程
    for process in processes:
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()
