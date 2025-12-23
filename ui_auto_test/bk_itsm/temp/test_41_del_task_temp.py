# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_41_del_task_temp.py
   Description : 
   Author :       v_adanchen
   date：          2021/1/26
-------------------------------------------------
"""
import seldom
import time
import test_dir.test_0_login
import settings
class DelTaskTemp(seldom.TestCase):
    def test_del_task_temp(self):
        test_dir.test_0_login.Login.test_login(self)
        # 点击后台管理
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        self.click(xpath="//div[@class='nav-slider-list']/div/div/div/span[contains(.,'流程管理')]")
        self.click(xpath="//div[@class='navigation-sbmenu-content collapse-transition']/div/a[8]")
        assert self.get_text(xpath="//ul/li/span[@title='{}']".format(settings.TASK_TEMPLATE))
        self.move_to_element(xpath="//ul/li/span[@title='{}']".format(settings.TASK_TEMPLATE))
        self.click(xpath="//span[@title='{}']/../span/i[@class='bk-icon icon-delete']".format(settings.TASK_TEMPLATE))
        self.click(xpath="//div[@class='footer-wrapper']/button[@name='confirm']")
        print("删除成功")
        self.assertText("删除成功")


