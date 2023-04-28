import threading

from utils import get_time

import real_events.e2023_4.JuBaoPen4yue1_2023_4 as work1
import real_events.e2023_4.JuBaoPen4yue2_2023_4 as work2


def run1():
    x = work1.mod("https://cf.qq.com/cp/a20230403three/pc/index.shtml?e_code=535546", get_time.get_next_minute())
    x.run_qiang_once(need_time=True)


def run2():
    x = work2.mod("https://cf.qq.com/cp/a20230403three/pc/index.shtml?e_code=535546", get_time.get_next_minute())
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
