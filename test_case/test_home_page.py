# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术


import unittest
from appium import webdriver
from app_test_project.pages.home_page import HomePage
from time import sleep
class TestHome(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        desired_caps = {
            "appActivity": ".MainActivity",
            "appPackage": "com.antancorp.app",
            "platformName": "Android",
            "automationName": "appium",
            "noReset": True,
            # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时添True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_001_home(self):
        '''首页搜索用例'''
        login_driver = HomePage(self.driver)
        login_driver.home_search_input.send_keys('测试')
        login_driver.search_result_buttun.click()
        txt = login_driver.search_result_xiangqing.text
        self.assertIn('测试',txt,'未搜索到信息')






if __name__ == '__main__':
    unittest.main()