import time
import datetime

import selenium.common.exceptions
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

    def _shut_down_pop_video(self):
        # 找到弹出的视频
        # 等待时间5秒，如果不出现则抛出超时异常
        wait_time = 5
        try:
            # 尝试找到是否出现弹出视频
            elem = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.ID, 'pop-video')))
            # 执行JavaScript代码点击关闭视频弹窗
            self.driver.execute_script("document.querySelector('.dialog01#pop-video .dia-close').click()")
            print('关闭弹出视频成功！')
        except selenium.common.exceptions.TimeoutException:
            print(f'无弹出视频或视频出现时间超过{wait_time}秒')

    def _set_screen_size(self):
        # 窗口最大化
        self.driver.maximize_window()
        # 设置窗口大小
        # self.driver.set_window_size(1300, 800)
        # print('调整前尺寸:', self.driver.get_window_size())

    def _login(self):
        # 点击登录按钮
        login_button = self.driver.find_element(By.ID, "dologin")
        login_button.click()


    def _init(self):

        self.driver.get(self.url)

        # 设置窗口大小
        self._set_screen_size()

        # 关闭弹出视频
        self._shut_down_pop_video()

        # 登录
        self._login()

        # if self.driver.find_element_by_id()

        # time.sleep(999999)

    def run(self):
        self._init()


if __name__ == '__main__':
    x = qiang()
    x.run()
