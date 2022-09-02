# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : test_web.py
# @CreateTime : 2022/8/26 17:21:09
import logging

from webdriver_helper import debugger

from core import pom


logger = logging.getLogger(__name__)


def test_login(driver):
    """登录"""
    driver.get("http://101.34.221.219:8010/")

    page = pom.HomePage(driver)
    page = page.to_login()

    page.login('whb01', 'admin123')
    msg = page.get_msg()

    assert '登录成功' == msg


def test_goods_favor(user_driver, clear_favor):
    """商品收藏"""
    user_driver.get("http://101.34.221.219:8010/?s=goods/index/id/5.html")
    page = pom.GoodsPage(user_driver)
    """获取收藏之前的数量"""
    favor_count = page.get_favor_count()
    page.favor()
    msg = page.get_msg()
    assert msg == "收藏成功"
    text = page.get_favor_text()
    assert text == "已收藏"
    new_favor_count = page.get_favor_count()
    assert new_favor_count == favor_count + 1
