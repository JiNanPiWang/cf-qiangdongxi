import time

from base_class import AutoGet_Normal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class mod(AutoGet_Normal.AutoGet_Normal):
    def _turn_to_the_page(self):
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.toptab-old .tab5').click()")

    def _click_LingQu(self):
        pass

    def run(self):
        super()._init()
        self._turn_to_the_page()
