import multiprocessing
import threading

from utils import get_time

import real_events.e2023_5.FuLiFengBao_JinNiuZuo as work1
import real_events.e2023_5.FuLiFengBao_QBZ as work2

def work_time():
    # 一秒等于一百万（1,000,000）微秒。
    return get_time.get_next_minute_mirco_early(850000)
    # return get_time.get_next_minute()

def run1():
    x = work1.mod("https://cf.qq.com/", work_time())
    x.run_qiang_once(need_time=True)

def run2():
    x = work2.mod("https://cf.qq.com/", work_time())
    x.run_qiang_once(need_time=True)


def multi_process():
    # 创建进程
    processes = [
        multiprocessing.Process(target=run1),
        multiprocessing.Process(target=run2),
    ]

    # 启动进程
    for process in processes:
        process.start()

    # 等待所有进程完成
    for process in processes:
        process.join()


def multi_thread():
    # 创建线程
    threads = [
        threading.Thread(target=run1),
        threading.Thread(target=run2),
    ]

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()


if __name__ == '__main__':
    # multi_thread()
    multi_process()
