import time
import platform
from datetime import datetime

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class AutoGet:
    def __init__(self, url, target_time):
        self.url = url
        self.os_type = platform.system()
        self.current_window_handle = None
        self.target_time = datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S:%f')

        chrome_options = webdriver.ChromeOptions()
        edge_options = webdriver.EdgeOptions()
        if self.os_type == 'Linux':  # Linux 系统
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            self.driver = webdriver.Chrome('/path/to/chromedriver', options=chrome_options)
        else:
            edge_options.add_argument("--mute-audio")
            self.driver = webdriver.Edge('/path/to/edgedriver', options=edge_options)

        self._wait = WebDriverWait(self.driver, 10)

    def _shut_down_pop_video(self):
        # 找到弹出的视频
        # 等待时间5秒，如果不出现则抛出超时异常
        wait_time = 10
        try:
            # 尝试找到是否出现弹出视频
            elem = WebDriverWait(self.driver, wait_time).until(EC.presence_of_element_located((By.ID, 'pop-video')))
            # 执行JavaScript代码点击关闭视频弹窗
            self.driver.execute_script("document.querySelector('.dialog01#pop-video .dia-close').click()")
            print('关闭弹出视频成功！')
        except selenium.common.exceptions.TimeoutException:
            print(f'无弹出视频或视频出现时间超过{wait_time}秒')

    def _set_screen_size(self):
        # 窗口最大化
        self.driver.maximize_window()
        # 设置窗口大小
        # self.driver.set_window_size(1300, 800)
        # print('调整前尺寸:', self.driver.get_window_size())

    def _touch_top_login_button(self):
        # 点击最上方登录按钮
        try:
            login_button = self.driver.find_element(By.ID, "dologin")
            login_button.click()
        except selenium.common.exceptions.ElementClickInterceptedException:
            print('直接弹出登录窗口，无需点击登录按钮')

    def _login(self):
        pass

    def _login_thru_passwd(self):
        pass

    def _open_new_window(self, new_window_url):
        # 开一个新窗口，并将driver转换到该窗口，url是new_window_url
        # 获取当前窗口的句柄
        self.current_window_handle = self.driver.current_window_handle

        # 执行JavaScript代码，打开新的窗口并跳转到指定URL
        self.driver.execute_script("window.open(arguments[0]);", new_window_url)

        # 获取所有窗口的句柄
        window_handles = self.driver.window_handles

        # 在新打开的窗口中进行操作
        for handle in window_handles:
            if handle != self.current_window_handle:
                self.driver.switch_to.window(handle)
                # 在新窗口中进行操作
                # ...

    def _close_new_window(self, close_icon: str):
        # 关闭现在的窗口，切回原来的窗口
        wait_time = 5
        try:
            # 查找是否存在 close_icon(LoginedCallback) 字符串
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, f"//*[contains(text(), '{close_icon}')]")))
        except selenium.common.exceptions.NoSuchElementException:
            # 如果不存在，则说明页面没有改变，不需要关闭
            pass
        else:
            # 如果存在，则说明页面已经改变，需要关闭
            self.driver.close()

    def _return_to_current_window(self):
        # 切回原来的窗口
        self.driver.switch_to.window(self.current_window_handle)
        self.driver.refresh()

    def _init(self):
        # 初始化，登录
        self.driver.get(self.url)
        # 设置窗口大小
        self._set_screen_size()

    def _turn_to_the_page(self):
        pass

    def _click_LingQu(self):
        pass

    def _click_QueDing_alert(self):
        pass

    def qiang_wu_xian_ci(self):
        if self.target_time is not None:
            # 等待抢购时间到达
            while datetime.now() < self.target_time:
                time.sleep(0.01)  # 每隔0.1秒检查一次时间

            while True:
                self._click_LingQu()
                self._click_QueDing_alert()

    def qiang_yi_ci(self, need_time=None):
        if self.target_time is not None:
            # 等待抢购时间到达
            while datetime.now() < self.target_time:
                time.sleep(0.01)  # 每隔0.01秒检查一次时间
            self._click_LingQu()
            if need_time:
                # 为了最快的测试，不调用函数
                print(datetime.now().strftime("%H:%M:%S:%f"))
            self._click_QueDing_alert()

    def run(self):
        # 登录并切换到页面
        self._init()
        self._turn_to_the_page()
        self.qiang_wu_xian_ci()
        # time.sleep(999999)

    def run_qiang_once(self, need_time=None):
        self._init()
        self._turn_to_the_page()
        self.qiang_yi_ci(need_time)
