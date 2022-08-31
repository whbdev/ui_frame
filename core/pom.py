# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : pom.py
# @CreateTime : 2022/8/30 16:10:24
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    ele_a = ''

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 显示等待
        self.wait = WebDriverWait(driver, 10)
        # 把属性中的元素变成真正的元素

    def check_element(self):
        """
        把属性中的字符串，变成真正的元素
        检查是否有元素丢失
        """
        for attr in dir(self):
            if attr.startswith("ele_"):  # 我们定义的元素属性
                loc = getattr(self, attr)
                self.driver.find_element(By.XPATH, loc)

    def test_master(self):
        print("dev2更新第一次")
        print("dev第一次更新")

