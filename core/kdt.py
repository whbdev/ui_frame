# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : kdt.py
# @CreateTime : 2022/9/7 8:55:20
"""Keyword Driver Testing"""
import logging
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait


class KeyWord:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 显示等待,最多10s
        self.wait = WebDriverWait(driver, 10)

    def find_element(self, *args):
        """封装过的元素定位方法，自动使用显示等待"""
        el = self.wait.until(lambda _: self.driver.find_element(*args))
        return el

    def key_get(self, url):
        self.driver.get(url)

    def key_js_code(self, loc, code):
        ele: WebElement = self.find_element(By.XPATH, loc)
        self.driver.execute_script(code, ele)
        time.sleep(1)

    def key_input(self, loc, content=None):
        ele = self.find_element(By.XPATH, loc)
        # 等待元素变成可用状态
        self.wait.until(lambda _: ele.is_enabled())  # _ 下划线的本质是没有意义
        #  清空元素里面的内容
        ele.clear()
        # 判断是否传递了参数
        if content is not None:
            # 如果传递了参数，输入进去
            ele.send_keys(content)

    def key_click(self, loc):
        ele = self.find_element(By.XPATH, loc)
        self.wait.until(lambda _: ele.is_enabled())
        ele.click()

    def key_assert_text(self, loc, text):
        ele_text = self.wait.until(
            lambda _: self.find_element(By.XPATH, loc).text
        )
        ele_text = ele_text.strip()
        text = text.strip()

        assert ele_text == text