import time
import os
import sys
import platform

if platform.system() == 'Linux':
    sys.path.append("../..")

from utils import get_time
from base_class.AutoGet_ShenQi import AutoGet_ShenQi
from base_class.AutoGet_Normal import AutoGet_Normal
import real_events.e2023_5.FuLiFengBao_JinNiuZuo as work1

def test_AutoGet_Normal():
    x = work1.mod("https://cf.qq.com/", get_time.get_next_hour_micro_early(860000))
    x.run()
    time.sleep(999999)


if __name__ == '__main__':
    # test_AutoGet_ShenQi()
    test_AutoGet_Normal()
