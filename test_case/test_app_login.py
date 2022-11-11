# !/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author : 狂师
# @Email : 公众号：测试开发技术

import os,sys
import unittest
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
print(sys.path)

# from app_test_project.pages.home_page import ContactManagerAddPage
from pages.login_page import LoginPage

class TestLogin(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        dir_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'test_app')
        app_path = os.path.join(dir_path, 'antian_test.apk')


        desired_caps = {
            "appActivity": ".MainActivity",
            "appPackage": "com.antancorp.app",
            "platformName": "Android",
            "automationName": "appium",
            # 'unicodeKeyboard': True,  # 使用自带输入法，输入中文时添True
            'resetKeyboard': True,  # 执行完程序恢复原来输入法
            'app': app_path,  #重新安装待测app
        }
        cls.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        cls.driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def test_001_login(self):
        '''测试安装登陆用例'''
        login_driver = LoginPage(self.driver)
        # 授权程序3个权限
        login_driver.add_quanxian_button.click()
        login_driver.add_quanxian_button.click()
        login_driver.add_quanxian_button.click()
        login_driver.user_input.send_keys('cs')
        login_driver.passwd_inpuet.send_keys('123456')
        login_driver.jizhumima.click()
        login_driver.login_button.click()
        shouye = login_driver.shouye.text
        self.assertEqual('首页',shouye,'登录失败')


if __name__ == '__main__':
    unittest.main()