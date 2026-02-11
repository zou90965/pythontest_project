from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class BaiduHomePage:
    """百度首页"""
    def __init__(self, driver):
        self.driver = driver
        self.baidu_logo = (By.ID, "s_lg_img")

    def wait_for_element(self, timeout, locator):
        """显示等待元素出现"""
        WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_baidu_logo(self, timeout=10):
        """等待百度logo加载"""
        self.wait_for_element(timeout, self.baidu_logo)

    def click_baidu_logo(self):
        """点击百度logo"""
        self.driver.find_element(*self.baidu_logo).click()
