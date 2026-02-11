# test_ui.py
from selenium.webdriver.common.by import By

from tests.ui_test.pages.baidu_home_page import BaiduHomePage


class TestUI:
    def test_open_baidu(self, firefox_browser):
        """测试用例：打开百度网页"""
        firefox_browser.get("https://www.baidu.com")
        assert "百度" in firefox_browser.title
        print(f"当前 URL: {firefox_browser.current_url}")
        print(f"页面标题: {firefox_browser.title}")

        """点击百度首页的百度logo"""
        baidu_home_page = BaiduHomePage(firefox_browser)
        baidu_home_page.wait_for_baidu_logo()
        baidu_home_page.click_baidu_logo()

        """获取当前所有窗口句柄"""
        handles = firefox_browser.window_handles
        print(f"当前所有窗口句柄: {handles}")
        """切换到最新打开的窗口"""
        firefox_browser.switch_to.window(handles[-1])
        """等待百度首页的按钮显示"""
        baidu_home_page.wait_for_element(10, (By.CLASS_NAME, "_tab-item_7dbe9_12"))
        print(f"当前 URL: {firefox_browser.current_url}")
        assert firefox_browser.find_element(By.CLASS_NAME, "_tab-item_7dbe9_12").is_displayed(), "百度首页的按钮未显示"
