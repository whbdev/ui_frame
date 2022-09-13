# -*- coding: utf-8 -*-
# @Author : WangHongBing
# @File : test_kdt.py
# @CreateTime : 2022/9/7 9:06:29
from core.kdt import KeyWord


def test_login(driver):

    kw = KeyWord(driver)
    kw.key_get("http://101.34.221.219:8010/")
    kw.key_click("/html/body/div[2]/div/ul[1]/div/div/a[1]")
    kw.key_input("/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input", "whb01")
    kw.key_input("/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input", "admin123")
    kw.key_click("/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button")
    kw.key_assert_text('//p[@class="prompt-msg"]', "登录成功")


def test_goods_favor(user_driver, clear_favor):
    kw = KeyWord(user_driver)
    kw.key_get("http://101.34.221.219:8010/?s=goods/index/id/5.html")
    kw.key_click("/html/body/div[4]/div[2]/div[2]/div/div[3]/div[1]/span/em[1]")
    kw.key_assert_text('//p[@class="prompt-msg"]', "收藏成功")


def test_update_user_info(user_driver):
    test_user_name = 'whb123'
    kw = KeyWord(user_driver)
    kw.key_get("http://101.34.221.219:8010/?s=personal/index.html")
    kw.key_click('/html/body/div[4]/div[3]/div/legend/a')
    kw.key_input('/html/body/div[4]/div[3]/div/form/div[1]/input', test_user_name)
    kw.key_click('//button[@class="am-close"]')
    kw.key_click('/html/body/div[4]/div[3]/div/form/div[2]/div/label[3]')
    kw.key_input('/html/body/div[4]/div[3]/div/form/div[3]/input', '2008-10-15')
    kw.key_click('/html/body/div[4]/div[3]/div/form/div[4]/button')
    kw.key_assert_text('//p[@class="prompt-msg"]', '编辑成功')

    kw.key_get("http://101.34.221.219:8010/?s=personal/index.html")
    kw.key_assert_text('/html/body/div[4]/div[3]/div/dl/dd[2]', test_user_name)


def test_update_user_avatar(user_driver):
    kw = KeyWord(user_driver)
    kw.key_get("http://101.34.221.219:8010/?s=personal/index.html")
    kw.key_click("/html/body/div[4]/div[3]/div/dl/dd[1]/span/a")
    kw.key_input('//*[@id="user-avatar-popup"]/div/div[2]/form/div[2]/div/input', r"D:\1.png")
    kw.key_click('//*[@id="user-avatar-popup"]/div/div[2]/form/button')

    kw.key_assert_text('//p[@class="prompt-msg"]', "上传成功")