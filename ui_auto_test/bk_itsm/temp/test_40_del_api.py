# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_40_del_api.py
   Description : 
   Author :       v_adanchen
   date：          2021/1/26
-------------------------------------------------
"""
import seldom
import time
import test_dir.test_0_login
import settings
class DelApi(seldom.TestCase):
    def test_del_api(self):
        test_dir.test_0_login.Login.test_login(self)
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        self.click(xpath="//div[@class='nav-slider-list']/div/div/div/span[contains(.,'流程管理')]")
        self.click(xpath="//div[@class='navigation-sbmenu-content collapse-transition']/div/a[3]")
        self.click(xpath="//table/tbody/tr[1]/td[10]//button[@title='移除']")
        self.click(xpath="//div[@class='footer-wrapper']/button[@name='confirm']")

