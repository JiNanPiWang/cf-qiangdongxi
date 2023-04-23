import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class qiang:
    def __init__(self):
        self.url = "https://cf.qq.com/"
        self.driver = webdriver.Edge('/path/to/edgedriver')

    def _login(self):
        self.driver.get(self.url)
        # 窗口最大化
        self.driver.maximize_window()
        # 设置窗口大小
        # self.driver.set_window_size(1300, 800)
        # print('调整前尺寸:', self.driver.get_window_size())
        # 显式等待
        # 这里进行手动登录，可以扫码，也可以输入账号密码点击登录
        # 等待目标元素加载完成
        wait = WebDriverWait(self.driver, 10)

        # 找到弹出的视频
        elem = wait.until(EC.presence_of_element_located((By.ID, 'pop-video')))

        # 执行JavaScript代码关闭视频弹窗
        self.driver.execute_script("document.querySelector('.dialog01#pop-video .dia-close').click()")
        # if self.driver.find_element_by_id()

        time.sleep(1000)
        print('登录成功！')


    def run(self):
        pass


if __name__ == '__main__':
    x = qiang()
    x._login()
