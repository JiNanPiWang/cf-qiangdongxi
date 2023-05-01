import multiprocessing
import threading

from utils import get_time

import real_events.e2023_5.FuLiFengBao_TianShiWanOu as work1
import real_events.e2023_5.FuLiFengBao_QBZ as work2

def run1():
    x = work1.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run()

def run2():
    x = work2.mod("https://cf.qq.com/", get_time.get_next_minute())
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
        threading.Thread(target=run3)
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
