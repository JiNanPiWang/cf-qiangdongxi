from AutoGet import AutoGet
from AutoGet_ShenQi import AutoGet_ShenQi
from AutoGet_Normal import AutoGet_Normal

if __name__ == '__main__':
    # x = AutoGet_ShenQi("https://cf.qq.com/cp/a20230308rlr/lr/index.shtml")
    x = AutoGet_Normal("https://cf.qq.com/")
    x.run()