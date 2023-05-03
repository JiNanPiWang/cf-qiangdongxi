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
