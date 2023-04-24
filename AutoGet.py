import time
import datetime

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoGet:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Edge('/path/to/edgedriver')
        self.is_chaojishenqi = False
        self.current_window_handle = None
        # 判断是否是超级神器，包含/lr
        if '/lr' in self.url:
            self.is_chaojishenqi = True

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

    def _touch_top_login_button(self):
        # 点击最上方登录按钮
        try:
            login_button = self.driver.find_element(By.ID, "dologin")
            login_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print('直接弹出登录窗口，无需点击登录按钮')



    def _open_new_window(self, new_window_url):
        # 开一个新窗口，url是new_window_url
        # 获取当前窗口的句柄
        self.current_window_handle = self.driver.current_window_handle

        # 执行JavaScript代码，打开新的窗口并跳转到指定URL
        self.driver.execute_script("window.open(arguments[0]);", new_window_url)

        # 获取所有窗口的句柄
        window_handles = self.driver.window_handles

        # 在新打开的窗口中进行操作
        for handle in window_handles:
            if handle != self.current_window_handle:
                self.driver.switch_to.window(handle)
                # 在新窗口中进行操作
                # ...

    def _close_new_window(self):
        # 等五秒，关闭现在的窗口，切回原来的窗口
        time.sleep(5)
        try:
            # 查找是否存在 LoginedCallback 字符串
            self.driver.find_element(By.XPATH, "//*[contains(text(), 'LoginedCallback')]")
        except selenium.common.exceptions.NoSuchElementException:
            # 如果不存在，则说明页面没有改变，不需要关闭
            pass
        else:
            # 如果存在，则说明页面已经改变，需要关闭
            self.driver.close()
        # 切回原来的窗口
        self.driver.switch_to.window(self.current_window_handle)
        self.driver.refresh()

    def _init(self):
        # 初始化，登录
        self.driver.get(self.url)
        # 设置窗口大小
        self._set_screen_size()

    def _get(self):
        pass
        # self.driver.execute_script("document.querySelector('tab6 .dia-close').click()")

    def run(self):
        self._init()
        self._get()
        time.sleep(999999)


if __name__ == '__main__':
    x = AutoGet("https://cf.qq.com/cp/a20230308rlr/lr/index.shtml")
    x.run()
