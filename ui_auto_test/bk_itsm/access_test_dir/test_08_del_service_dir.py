# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_10_del_service_dir.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""

from bk_itsm.page import add_servicedir as page
import seldom
import time
from bk_itsm.test_dir import test_01_login
class DelServiceDir(seldom.TestCase):
    def test_01_remove_service(self):
        # test_01_login.Login.test_login(self)
        self.click(xpath=page.project)
        # self.click(xpath=page.nav_service_dir)
        self.click(xpath=page.service_new_dir)
        self.click(xpath=page.remove_flow)
        self.click(xpath=page.service_del_comfirm)
        time.sleep(1)

    # def test_02_del_service_dir(self):
    #     # self.click(xpath=page.service_new_dir)
    #     # self.click(xpath=page.service_dir_more)
    #     # self.click(xpath=page.service_del)
    #     # self.click(xpath=page.service_del_comfirm)
    #
    #     time.sleep(1)