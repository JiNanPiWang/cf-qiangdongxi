from datetime import datetime

import real_events.e2023_5.FuLiFengBao_TianShiWanOu as TianShi
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_class.AutoGet import AutoGet

class mod(TianShi.mod):
    def _click_LingQu(self):
        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p5-wantonly-box'))). \
            find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick(\'942035\',\'\',\'\',\'\',\'4\');"]')

        # 点击a标签
        # print(f'金牛座函数点击前计算时间：{datetime.now().strftime("%H:%M:%S:%f")}')
        a.click()

    def _login(self):
        super()._touch_top_login_button()

        # 登录页面是表单内嵌的页面，需要定位到iframe元素，通过id来定位
        login_element = self.driver.find_element(By.ID, "loginIframe")

        # 使用switch_to.frame()方法切换到该iframe中
        self.driver.switch_to.frame(login_element)

        # 找到密码登录四个字
        passwd_login = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'switcher_plogin')))
        passwd_login.click()

        # username = driver.find_element_by_name('username')
        # password = driver.find_element_by_name('password')
        # username.send_keys('your_username')
        # password.send_keys('your_password')

        # 切换回去
        self.driver.switch_to.default_content()

        pass