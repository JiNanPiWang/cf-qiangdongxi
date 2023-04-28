from base_class import AutoGet_Normal

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class mod(AutoGet_Normal.AutoGet_Normal):
    def _click_LingQu(self):
        # <div class="p4box1 flex">
        #     <div class="prop-item">
        #         <p>M200-赤血龙魂</p>
        #         <a href="javascript:DM.df.getClick1('933316','','','','2');" class=...
        #     </div>
        # </div>
        # 如抢赤血龙魂

        # 等待p4box1元素出现
        wait = WebDriverWait(self.driver, 10)
        p4box1 = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'p4box1')))

        # 在p4box1元素中查找具有特定href属性值的a标签
        # 注意：在XPath表达式中，我将//更改为.//，以确保只在p4box1元素的子元素中查找a标签。
        a = p4box1.find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick1(\'933316\',\'\',\'\',\'\',\'2\');"]')

        # 点击a标签
        a.click()
