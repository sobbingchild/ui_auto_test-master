# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_11_del_trigger.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""
import seldom
from bk_itsm.page import triger as page
import time
import bk_itsm.settings as settings



class DelTriger(seldom.TestCase):
    def test_01_del_recover(self):
        """"删除恢复单据触发器"""
        self.click(xpath=page.project)
        self.click(xpath=page.nav_triger)
        self.del_trigger(settings.TRIGGER_RECOVER)

    def test_02_del_hang(self):
        """"删除挂起单据触发器"""
        self.del_trigger(settings.TRIGGER_HANG)

    def test_03_del_distri(self):
        """"删除分发单据触发器"""
        self.del_trigger(settings.TRIGGER_DISTRIBUTION)

    def test_03_del_claim_tickets(self):
        """"删除认领单据触发器"""
        self.del_trigger(settings.TRIGGER_CLAIM_TICKETS)

    def test_04_del_out_nodes(self):
        """"删除离开节点触发器"""
        self.del_trigger(settings.TRIGGER_OUT_NODES)

    def test_05_del_into_branch_task(self):
        """"删除进入分支触发器"""
        self.del_trigger(settings.TRIGGER_BRANCH_TASK)

    def test_06_del_into_nodes(self):
        """"删除进入节点触发器"""
        self.del_trigger(settings.TRIGGER_INTO_NODES)

    def test_07_del_create_tickets(self):
        """"删除创建单据触发器"""
        self.del_trigger(settings.TRIGGER_CREATE_TICKET)

    def test_08_del_into_branch(self):
        """"删除进入分支触发器"""
        self.del_trigger(settings.TRIGGER_INTO_BRANCH)



    def del_trigger(self, trigger_name):
        self.move_to_element(xpath=page.trigger_name(trigger_name))
        self.click(xpath=page.del_trigger(trigger_name))
        self.click(xpath=page.del_confirm)
        time.sleep(1)

