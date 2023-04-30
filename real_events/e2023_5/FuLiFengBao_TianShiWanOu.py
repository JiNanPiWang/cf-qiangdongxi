import random
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from base_class.AutoGet import AutoGet


class mod(AutoGet):
    def __init__(self, url, target_time):
        # 父类需要用到self的内容时才传入self参数，如父类print(f"Hello, I'm {self.name}")
        super().__init__(url, target_time)

    def _init(self):
        super()._init()

        # # 关闭弹出视频
        # self._shut_down_pop_video()

        # 登录
        self._login()

        # # 关闭弹出视频
        # self._shut_down_pop_video()
        # time.sleep(random.uniform(1, 2))
        # self._shut_down_pop_video()

    def _login(self):
        # 正常情况登录
        super()._touch_top_login_button()

        # 登录页面是表单内嵌的页面，需要定位到iframe元素，通过id来定位
        login_element = self.driver.find_element(By.ID, "loginIframe")

        # 使用switch_to.frame()方法切换到该iframe中
        self.driver.switch_to.frame(login_element)

        # 点击QQ头像，一定要登录QQ！
        elem = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, 'qlogin_list')))
        # 执行JavaScript代码点击
        # self.driver.execute_script("document.querySelector('.face').click()")
        elem.find_element(By.CLASS_NAME, 'face').click()
        print('登录成功！')

        # 切换回去
        self.driver.switch_to.default_content()

    def _turn_to_the_page(self):
        time.sleep(2)
        self.driver.execute_script("document.querySelector('.toptab-old .tab5').click()")
        time.sleep(2)
        pass

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
        a = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'p5-wantonly-box'))).\
            find_element(By.XPATH, './/a[@href="javascript:DM.df.getClick(\'942035\',\'\',\'\',\'\',\'7\');"]')

        # 点击a标签
        a.click()

    def _click_QueDing_alert(self):
        # 等待确定按钮出现
        wait = WebDriverWait(self.driver, 10)
        confirm_button = wait.until(EC.element_to_be_clickable((By.ID, 'lotteryAlertDialogBtn')))

        # 点击确定按钮
        confirm_button.click()

    def run(self):
        super().run()

        time.sleep(999999)