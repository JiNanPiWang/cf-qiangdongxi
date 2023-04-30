import threading

from utils import get_time

import real_events.e2023_5.FuLiFengBao_TianShiWanOu as work1
import real_events.e2023_5.FuLiFengBao_QBZ as work2


def run1():
    x = work1.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run_qiang_once(need_time=True)


def run2():
    x = work2.mod("https://cf.qq.com/", get_time.get_next_minute())
    x.run_qiang_once(need_time=True)


if __name__ == '__main__':
    # 创建线程
    threads = [
        threading.Thread(target=run1),
        threading.Thread(target=run2)
    ]

    # 启动线程
    for thread in threads:
        thread.start()

    # 等待所有线程完成
    for thread in threads:
        thread.join()

    # print(datetime.datetime.now().strftime("%H:%M:%S:%f"))
