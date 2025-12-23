# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_13_del_mode.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""

import seldom
import bk_itsm.page.model as page
import time

class DelMode(seldom.TestCase):
    def test_del_mode(self):
        """"删除模式"""
        self.click(xpath=page.project)
        self.click(xpath=page.nav_model)
        self.move_to_element(xpath=page.model_del_obj)
        time.sleep(1)
        self.click(xpath=page.model_del_icon)
        self.click(xpath=page.model_del_confrim)



