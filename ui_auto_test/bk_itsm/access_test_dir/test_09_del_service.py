# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_11_del_service.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""

import seldom
from bk_itsm.page import add_service as page
import time
from bk_itsm.test_dir import test_01_login as login

class DelService(seldom.TestCase):
    def test_del_service(self):
        # login.Login.test_login(self)
        self.click(xpath=page.project)
        self.click(xpath=page.nav_service)
        self.type_enter(xpath=page.search_service,text=page.service_input)
        self.click(xpath=page.all_service)
        self.click(xpath=page.all_service_del)
        self.click(xpath=page.all_service_del_confirm)
        time.sleep(1)


