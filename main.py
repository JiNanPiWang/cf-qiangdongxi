from AutoGet import AutoGet
from AutoGet_ShenQi import AutoGet_ShenQi
from AutoGet_Normal import AutoGet_Normal


def test_AutoGet_ShenQi():
    x = AutoGet_ShenQi("https://cf.qq.com/cp/a20230308rlr/lr/index.shtml")
    x.run()


def test_AutoGet_Normal():
    x = AutoGet_Normal("https://cf.qq.com/")
    x.run()


if __name__ == '__main__':
    test_AutoGet_ShenQi()
