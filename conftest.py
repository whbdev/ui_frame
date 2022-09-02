# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : conftest.py
# @CreateTime : 2022/8/26 10:03:41
import json
import logging
from pathlib import Path
import pytest
from webdriver_helper import get_webdriver
from core import pom


logger = logging.getLogger(__name__)


@pytest.fixture(scope='class')
def driver():
    d = get_webdriver()
    yield d
    d.quit()


@pytest.fixture(scope='session')
def user_driver():
    """前置登录"""
    cookies = []
    driver = get_webdriver()
    driver.get("http://101.34.221.219:8010/")

    path = Path('temp/cookie/cookies.json')
    if path.exists():
        cookies = json.loads(path.read_text())
    logger.info("加载cookie")
    for cookie in cookies:
        driver.add_cookie(cookie)
        logger.warning(f"设置cookie:{cookie}")

    driver.get("http://101.34.221.219:8010/")

    if "退出" in driver.page_source:
        pass
    else:
        page = pom.HomePage(driver)
        page = page.to_login()

        page.login('whb01', 'admin123')
        msg = page.get_msg()

        assert '登录成功' == msg

        # 保存Cookie
        cookie = driver.get_cookies()
        with open('temp/cookie/cookies.json', 'w') as f:
            f.write(json.dumps(cookie))

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