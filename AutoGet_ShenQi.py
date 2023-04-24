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

class AutoGet_ShenQi(AutoGet):
    def __init__(self, url):
        super().__init__(url)

    def _init(self):
        super()._init()

        # 登录
        self._login()

    def _login(self):
        # 超级神器登录需要，先切换frame，再打开登录链接登录
        qqLoginFrame = self.driver.find_element(By.CLASS_NAME, 'qqLoginFrame')
        qqLoginUrl = qqLoginFrame.get_attribute('src')
        # 开一个新页面，登录qq
        super()._open_new_window(qqLoginUrl)
        self.driver.get(qqLoginUrl)

        # 此处偷懒，.face应该不是可交互按钮
        try:
            self.driver.execute_script("document.querySelector('.face').click()")
        except selenium.common.exceptions.ElementNotInteractableException:
            pass

        super()._close_new_window('LoginedCallback')