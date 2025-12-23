# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_03_add_servicedir.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""
import seldom
import bk_itsm.page.add_servicedir
import bk_itsm.settings as settings
from bk_itsm.test_dir import test_01_login as login
import bk_itsm.page.create_default as page
import time
#已完成
class AddServiceDir(seldom.TestCase):
    def test_01_add_service_dir(self):
        login.Login.test_login(self)
        self.click(xpath=page.project)
        time.sleep(1)
        self.click(xpath=page.service)
        time.sleep(5)
        # self.click(xpath=page.nav_service_dir)
        self.click(xpath=bk_itsm.page.add_servicedir.root_dir_more)
        self.click(xpath=bk_itsm.page.add_servicedir.root_dir_add)
        self.type(xpath=page.service_name,text=settings.SERVICE_DIR)
        self.click(xpath=bk_itsm.page.add_servicedir.service_comfirm)
