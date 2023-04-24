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
        self.url = "https://cf.qq.com/cp/a20230308rlr/lr/index.shtml"
        self.driver = webdriver.Edge('/path/to/edgedriver')
        self.is_chaojishenqi = False
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

    def _login(self):
        # 点击登录按钮
        try:
            login_button = self.driver.find_element(By.ID, "dologin")
            login_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print('直接弹出登录窗口，无需点击登录按钮')

        # 登录页面是表单内嵌的页面，需要定位到iframe元素，通过id来定位
        login_element = self.driver.find_element(By.ID, "loginIframe")

        # 使用switch_to.frame()方法切换到该iframe中
        self.driver.switch_to.frame(login_element)

        # 点击QQ头像，一定要登录QQ！
        # elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'qlogin_list')))
        # 执行JavaScript代码点击
        self.driver.execute_script("document.querySelector('.face').click()")
        print('登录成功！')

        # 切换回去
        self.driver.switch_to.default_content()

    def _open_new_window(self, new_window_url):
        # 获取当前窗口的句柄
        current_window_handle = self.driver.current_window_handle

        # 执行JavaScript代码，打开新的窗口并跳转到指定URL
        self.driver.execute_script("window.open(arguments[0]);", new_window_url)

        # 获取所有窗口的句柄
        window_handles = self.driver.window_handles

        # 在新打开的窗口中进行操作
        for handle in window_handles:
            if handle != current_window_handle:
                self.driver.switch_to.window(handle)
                # 在新窗口中进行操作
                # ...

        # 切回原来的窗口
        self.driver.switch_to.window(current_window_handle)

    def _chaojishenqi_login(self):
        # 超级神器登录需要，先切换frame，再打开登录链接登录
        qqLoginFrame = self.driver.find_element(By.CLASS_NAME, 'qqLoginFrame')
        qqLoginUrl = qqLoginFrame.get_attribute('src')
        # 开一个新页面，登录qq
        self._open_new_window(qqLoginUrl)
        # qqLoginDriver.get(qqLoginUrl)
        # # 需要等一段时间
        # time.sleep(10)
        # qqLoginDriver.execute_script("document.querySelector('.face').click()")
        # qqLoginDriver.close()

        self.driver.refresh()

    def _init(self):

        self.driver.get(self.url)

        # 设置窗口大小
        self._set_screen_size()

        # 关闭弹出视频
        self._shut_down_pop_video()

        # 登录
        if self.is_chaojishenqi:
            self._chaojishenqi_login()
        self._login()

        # 关闭弹出视频
        self._shut_down_pop_video()
        time.sleep(2)
        self._shut_down_pop_video()

    def _get(self):
        pass
        # self.driver.execute_script("document.querySelector('tab6 .dia-close').click()")

    def run(self):
        self._init()
        self._get()


if __name__ == '__main__':
    x = qiang()
    x.run()
