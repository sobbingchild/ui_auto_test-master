# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_06_del_triger.py
   Description : 
   Author :       v_adanchen
   date：          2022/1/10
-------------------------------------------------
"""
import seldom
from bk_itsm.page import triger as page
import time
import bk_itsm.settings as settings
from bk_itsm.test_dir import test_01_login

class DelTriger(seldom.TestCase):
    def test_01_del_recover(self):
        # test_01_login.Login.test_login(self)
        self.click(xpath=page.project)
        self.click(xpath=page.nav_triger)
        self.del_trigger(settings.TRIGGER_RECOVER)

    def test_02_del_hang(self):
        self.del_trigger(settings.TRIGGER_HANG)

    def test_03_del_distri(self):
        self.del_trigger(settings.TRIGGER_DISTRIBUTION)

    def test_03_del_claim_tickets(self):
        self.del_trigger(settings.TRIGGER_CLAIM_TICKETS)

    def test_04_del_out_nodes(self):
        self.del_trigger(settings.TRIGGER_OUT_NODES)

    def test_05_del_into_branch_task(self):
        self.del_trigger(settings.TRIGGER_BRANCH_TASK)

    def test_06_del_into_nodes(self):
        self.del_trigger(settings.TRIGGER_INTO_NODES)

    def test_07_del_create_tickets(self):
        self.del_trigger(settings.TRIGGER_CREATE_TICKET)

    def test_08_del_into_branch(self):
        self.del_trigger(settings.TRIGGER_INTO_BRANCH)



    def del_trigger(self, trigger_name):
        self.move_to_element(xpath=page.trigger_name(trigger_name))
        self.click(xpath=page.del_trigger(trigger_name))
        self.click(xpath=page.del_confirm)
        time.sleep(1)
