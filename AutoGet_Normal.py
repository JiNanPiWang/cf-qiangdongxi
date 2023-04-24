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