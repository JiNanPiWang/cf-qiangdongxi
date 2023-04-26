import threading
from selenium import webdriver

def run_browser():
    driver = webdriver.Chrome()
    driver.get("https://www.example.com")
    # 在此处添加其他Selenium操作
    driver.quit()

# 创建线程
threads = []
for i in range(5):
    t = threading.Thread(target=run_browser)
    threads.append(t)

# 启动线程
for thread in threads:
    thread.start()

# 等待所有线程完成
for thread in threads:
    thread.join()
