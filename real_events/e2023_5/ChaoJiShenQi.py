import random
import time
from datetime import datetime

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_class.AutoGet import AutoGet
from base_class.AutoGet_ShenQi import AutoGet_ShenQi


class mod(AutoGet_ShenQi):
    def _click_LingQu(self):
        # 示例见normal
        wait = WebDriverWait(self.driver, 10)
        button = wait.until(EC.presence_of_element_located((By.XPATH,
                                                            './/a[@href="javascript:OUT.user.getTeamPointGift(21);"]')))
        # 点击a标签
        button.click()

    def qiang_wu_xian_ci(self):
        if self.target_time is not None:
            # 等待抢购时间到达
            while datetime.now() < self.target_time:
                time.sleep(0.01)  # 每隔0.1秒检查一次时间

            while True:
                self._click_LingQu()
                time.sleep(0.01)
                self._click_QueDing_alert()
