import os
import time
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

global  driver
def startChrome():
    global driver
    # chromedriver的文件位置
    chrome_driver_path = '/opt/google/chrome/chrom'
    #driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver = webdriver.Chrome()

def startUrl():
    global driver
    url = "http://baidu.com"
    driver.get(url)


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
def refresh():
    global driver
    #刷新
    driver.refresh()
    #
    driver.switch_to.window(driver.window_handles[-1])
    driver.current_window_handle
    #
    driver.maximize_window()
    # 通过 id 切换框架
   # driver.switch_to.frame("iframe")


    # 启动驱动程序
    # 打开网址
    driver.get("https://blog.csdn.net/wenming111")
    # 设置等待
    wait = WebDriverWait(driver, 10)
    # 存储原始窗口的 ID
    original_window = driver.current_window_handle
    # 检查一下，我们还没有打开其他的窗口
    assert len(driver.window_handles) == 1