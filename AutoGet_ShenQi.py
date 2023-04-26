from AutoGet import AutoGet
import random

from AutoGet import AutoGet
import time
from datetime import datetime, timedelta

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AutoGet_ShenQi(AutoGet):
    def __init__(self, url, target_time):
        # target_time: 2023-04-25 13:55:00
        super().__init__(url, target_time)

    def _init(self):
        super()._init()

        # 登录
        self._login()

    def _login(self):
        # 超级神器登录需要，先切换frame，再打开登录链接登录
        wait = WebDriverWait(self.driver, 10)
        qqLoginFrame = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'qqLoginFrame')))
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
        super()._return_to_current_window()

    def _turn_to_the_page(self):
        self.driver.execute_script("document.querySelector('.tab_2.sp1').click()")

    def _click_LingQu(self):
        # 示例见normal
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            './/a[@href="javascript:OUT.user.getTeamPointGift(12);"]')))
        # 点击a标签
        button.click()

    def _click_QueDing_alert(self):
        # 等待确定按钮出现
        wait = WebDriverWait(self.driver, 10)
        confirm_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'amsdialog_bconfirm')))

        # 点击确定按钮
        confirm_button.click()

    def run(self):
        super().run()
        time.sleep(999999)
