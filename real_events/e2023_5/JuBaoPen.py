import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_class.AutoGet import AutoGet
from base_class.AutoGet_Normal import AutoGet_Normal


class mod(AutoGet_Normal):
    def _turn_to_the_page(self):
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.list_nav .nav4').click()")
        time.sleep(2)

    def _click_LingQu(self):
        # <div class="p4box1 flex">
        #     <div class="prop-item">
        #         <p>M200-赤血龙魂</p>
        #         <a href="javascript:DM.df.getClick1('933316','','','','2');" class=...
        #     </div>
        # </div>
        # 如抢赤血龙魂

        # 等待p4box1元素出现
        # wait = WebDriverWait(self.driver, 10)
        # p4box1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'p4box1')))

        # 在p4box1元素中查找具有特定href属性值的a标签
        # 注意：在XPath表达式中，我将//更改为.//，以确保只在p4box1元素的子元素中查找a标签。
        # a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p4box1'))). \
        #     find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick1(\'933316\',\'\',\'\',\'\',\'2\');"]')
        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 't4part1'))).\
            find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick(\'942008\',\'\',\'\',\'\',\'2\');"]')

        # 点击a标签
        a.click()
