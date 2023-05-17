import multiprocessing
import threading

from utils import get_time

import real_events.e2023_5.ChaoJiShenQi as work1

def work_time(idx: int):
    return get_time.get_next_hour_micro_early(800000 + idx * 20000)

def run1():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(0))
    x.run()

def run2():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(1))
    x.run()

def run3():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(2))
    x.run()

def run4():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(3))
    x.run()

def run5():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(4))
    x.run()

def run6():
    x = work1.mod("https://cf.qq.com/cp/a20230407rlr/lr/index.shtml", work_time(5))
    x.run()

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
        threading.Thread(target=run3),
        threading.Thread(target=run4),
        threading.Thread(target=run5),
        threading.Thread(target=run6),
    ]

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
        
    
if __name__ == '__main__':
    # multi_thread()
    multi_thread()
