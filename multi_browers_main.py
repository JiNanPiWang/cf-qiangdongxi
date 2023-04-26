import os
import threading

import get_time
from AutoGet import AutoGet
from AutoGet_ShenQi import AutoGet_ShenQi
from AutoGet_Normal import AutoGet_Normal

import real_circum.JuBaoPen4yue1
import real_circum.JuBaoPen4yue2

def run1():
    x = real_circum.JuBaoPen4yue1.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run()

def run2():
    x = real_circum.JuBaoPen4yue2.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run()


if __name__ == '__main__':

    current_path = os.path.dirname(__file__)

    # 创建线程
    threads = [
        threading.Thread(target=run1()),
        threading.Thread(target=run2())
    ]

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()
