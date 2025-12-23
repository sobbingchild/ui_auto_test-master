# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_39_del_trigger.py
   Description : 
   Author :       v_adanchen
   date：          2021/1/26
-------------------------------------------------
"""

import seldom
import time
import test_dir.test_0_login
import settings
class DelTrigger(seldom.TestCase):
    def test_1_del_trigger_into_branch(self):
        test_dir.test_0_login.Login.test_login(self)
        # 点击后台管理
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        self.click(xpath="//div[@class='nav-slider-list']/div/div/div/span[contains(.,'流程管理')]")
        self.click(xpath="//div[@class='navigation-sbmenu-content collapse-transition']/div/a[7]")
        self.del_trigger(settings.TRIGGER_INTO_BRANCH)

    def test_2_del_trigger_into_nodes(self):
        self.del_trigger(settings.TRIGGER_INTO_NODES)


    def test_3_del_trigger_create_ticket(self):
        self.del_trigger(settings.TRIGGER_CREATE_TICKET)

    def test_4_del_trigger_into_branch_task(self):
        self.del_trigger(settings.TRIGGER_BRANCH_TASK)

    def del_trigger(self,name):
        self.move_to_element(
            xpath="//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(name))
        self.click(
            xpath="//span[@title='{}']/../span[@class='bk-trigger-delete']".format(name))
        self.click(xpath="//div[@class='bk-dialog-footer']/div/button[@name='confirm']")
        time.sleep(3)







