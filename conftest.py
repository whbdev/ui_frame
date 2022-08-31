# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : conftest.py
# @CreateTime : 2022/8/26 10:03:41
import pytest
from webdriver_helper import get_webdriver


@pytest.fixture(scope='class', autouse=True)
def driver():
    d = get_webdriver()
    yield d
    d.quit()