import time

from selenium.common import StaleElementReferenceException
from selenium.webdriver import ActionChains

from base_class import AutoGet_Normal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class mod(AutoGet_Normal.AutoGet_Normal):
    def _turn_to_the_page(self):
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.toptab-old .tab5').click()")

    def _click_LingQu(self):
        # a = EC.presence_of_element_located((By.CLASS_NAME, 'p5-wantonly-item')). \
        #     find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick1(\'942035\',\'\',\'\',\'\',\'7\');"]')
        time.sleep(2)
        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p5-wantonly-item'))). \
            find_element(By.XPATH, '//a[@href="javascript:DM.df.getClick1(\'942035\',\'\',\'\',\'\',\'7\');"]')

        # 点击a标签
        a.click()

    def run(self):
        super()._init()
        self._turn_to_the_page()
        super().qiang_wu_xian_ci()
