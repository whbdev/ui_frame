# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : conftest.py
# @CreateTime : 2022/8/26 10:03:41
import pytest
from webdriver_helper import get_webdriver

from core import pom


@pytest.fixture(scope='class')
def driver():
    d = get_webdriver()
    yield d
    d.quit()


@pytest.fixture(scope='session')
def user_driver():
    """前置登录"""
    driver = get_webdriver()
    driver.get("http://101.34.221.219:8010/")

    page = pom.HomePage(driver)
    page = page.to_login()

    page.login('whb01', 'admin123')
    msg = page.get_msg()

    assert '登录成功' == msg

    yield driver

    driver.quit()


@pytest.fixture()
def clear_favor(user_driver):
    # 清除已收藏的商品
    user_driver.get('http://101.34.221.219:8010/?s=usergoodsfavor/index.html')
    page = pom.UserGoodsFavorPage(user_driver)
    is_click = page.delete_favor()
    if is_click:
        msg = page.get_msg()
        assert msg == "删除成功"