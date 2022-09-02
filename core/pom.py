# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : pom.py
# @CreateTime : 2022/8/30 16:10:24
import logging

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_helper import debugger

logger = logging.getLogger(__name__)


class BasePage:

    def __init__(self, driver: WebDriver):
        self.driver = driver
        # 显示等待,最多10s
        self.wait = WebDriverWait(driver, 10)
        self.check_element()

    def check_element(self):
        """
        把属性中的字符串，变成真正的元素
        检查是否有元素丢失
        """
        for attr in dir(self):
            if attr.startswith("ele_"):  # 我们定义的元素属性
                loc = getattr(self, attr)   # 获取属性的内容
                el = self.find_element(By.XPATH, loc)  # 定位元素
                setattr(self, attr, el)  # 设置属性

    def find_element(self, *args):
        """封装过的元素定位方法，自动使用显示等待"""
        logger.info(f"正在定位元素：{args}")
        el = self.wait.until(lambda _: self.driver.find_element(*args))
        logger.info("定位元素成功")
        return el

    def input(self, ele: WebElement, content=None):
        # 等待元素变成可用状态
        self.wait.until(lambda _: ele.is_enabled())  # _ 下划线的本质是没有意义
        #  清空元素里面的内容
        ele.clear()
        # 判断是否传递了参数
        if content is not None:
            # 如果传递了参数，输入进去
            ele.send_keys(content)

    def click(self, ele: WebElement):
        self.wait.until(lambda _: ele.is_enabled())
        ele.click()

    def get_msg(self):
        msg = self.wait.until(
            lambda _: self.find_element(By.XPATH, '//p[@class="prompt-msg"]').text
        )
        return msg


class HomePage(BasePage):
    ele_a_login = "/html/body/div[2]/div/ul[1]/div/div/a[1]"
    ele_ipt_search = '//*[@id="search-input"]'
    ele_btn_search = '//*[@id="ai-topsearch"]'

    def to_login(self):
        """跳转到登录界面"""
        self.click(self.ele_a_login)

        return LoginPage(self.driver)


class LoginPage(BasePage):
    ele_ipt_username = (
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input"
    )
    ele_ipt_password = (
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input"
    )
    ele_btn_submit = (
        "/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button"
    )

    def login(self, username, password):
        self.input(self.ele_ipt_username, username)
        self.input(self.ele_ipt_password, password)
        self.click(self.ele_btn_submit)


class GoodsPage(BasePage):
    """商品收藏"""
    ele_btn_favor = '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[1]'
    ele_num_favor = '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[2]'
    ele_text_favor = '/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[1]'

    def favor(self):
        """进行收藏"""
        self.click(self.ele_btn_favor)

    def get_favor_count(self):
        """获取收藏数量"""
        text = self.ele_num_favor.text
        text = text.replace("(", "").replace(")", "")
        value = int(text)
        return value

    def get_favor_text(self):
        """获取已收藏的text"""
        text = self.ele_text_favor.text
        return text


class UserGoodsFavorPage(BasePage):
    """个人中心-商品收藏进行全选，删除所有的收藏"""
    ele_btn_all = '/html/body/div[4]/div[3]/div/div[2]/form/div[3]/table/thead/tr[1]/th[1]/button'
    ele_btn_del = '/html/body/div[4]/div[3]/div/div[2]/form/div[2]/button[1]'
    loc_btn_sure = '//div/span[text()="确定"]'

    def delete_favor(self):
        """判断个人中心收藏界面的全选按钮是否可以点击"""
        if self.ele_btn_all.is_enabled():
            self.click(self.ele_btn_all)
            self.click(self.ele_btn_del)
            # loc前缀的元素不会被初始化
            self.click(self.find_element(By.XPATH, self.loc_btn_sure))
            return True
        else:
            return False