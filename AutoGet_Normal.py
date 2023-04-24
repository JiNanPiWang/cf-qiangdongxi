from AutoGet import AutoGet
import time
import datetime

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AutoGet_Normal(AutoGet):
    def __init__(self, url):
        # 父类需要用到self的内容时才传入self参数，如父类print(f"Hello, I'm {self.name}")
        super().__init__(url)

    def _init(self):
        super()._init()

        # 关闭弹出视频
        self._shut_down_pop_video()

        # 登录
        self._login()

        # 关闭弹出视频
        self._shut_down_pop_video()
        time.sleep(2)
        self._shut_down_pop_video()

    def _login(self):
        # 正常情况登录
        super()._touch_top_login_button()

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