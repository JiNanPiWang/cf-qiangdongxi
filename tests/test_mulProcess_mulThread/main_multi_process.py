import multiprocessing

from utils import get_time

import real_events.e2023_4.JuBaoPen4yue1_2023_4 as work1
import real_events.e2023_4.JuBaoPen4yue2_2023_4 as work2


def run1():
    x = work1.mod("https://cf.qq.com/cp/a20230403three/pc/index.shtml?e_code=535546", get_time.get_next_2minute())
    x.run_qiang_once(need_time=True)


def run2():
    x = work2.mod("https://cf.qq.com/cp/a20230403three/pc/index.shtml?e_code=535546", get_time.get_next_2minute())
    x.run_qiang_once(need_time=True)


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

    # print(datetime.datetime.now().strftime("%M:%S:%f"))
