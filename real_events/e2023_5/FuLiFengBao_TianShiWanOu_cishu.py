import real_events.e2023_5.FuLiFengBao_TianShiWanOu as TianShi
import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_class.AutoGet import AutoGet


class mod(TianShi.mod):
    def _click_LingQu(self):
        # href="javascript:DM.df.getClick('942290','','','','1');"
        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p5-lottery-box'))). \
            find_element(By.CLASS_NAME, 'btn5-1')

        # 点击a标签
        a.click()
