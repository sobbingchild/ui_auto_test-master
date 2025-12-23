# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_03_model.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""
import seldom
import bk_itsm.page.model as page
import bk_itsm.settings as settings

#已完成
class AddModel(seldom.TestCase):

    def test_add_model(self):
        """"添加模式"""
        self.click(xpath=page.project)
        self.click(xpath=page.nav_model)
        self.click(xpath=page.add_model)
        self.type(xpath=page.model_name,text=settings.TEST_MODEL_NAME)
        self.click(xpath=page.model_commit)


