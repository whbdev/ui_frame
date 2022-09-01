# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : test_web.py
# @CreateTime : 2022/8/26 17:21:09
from core import pom


def test_login(driver):
    driver.get("http://101.34.221.219:8010/")

    page = pom.HomePage(driver)
    page = page.to_login()

    page.login('whb01', 'admin123')
    msg = page.get_msg()

    assert '登录成功' == msg