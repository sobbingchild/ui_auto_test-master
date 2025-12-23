# -*- coding: utf-8 -*-
# @Time : 2021/1/7 16:43
# @File : test_05_create_default_flow.py
# @Project : ITSM_UI_AUTO

import seldom
import sys
import time

sys.path.append("../")
import bk_itsm.settings as settings
import bk_itsm.page.create_default as page
from  bk_itsm.test_dir import test_01_login as login

# 创建默认流程
# 已完成
class CreateDefaultFlow(seldom.TestCase):
    def test_01_create_flow(self):
        # login.Login.test_login(self)
        self.click(xpath=page.project)
        time.sleep(1)
        self.click(xpath=page.service)
        self.wait(1)
        self.click(xpath=page.new_service,index=0)
        time.sleep(1)
        self.type(xpath=page.service_name,text=settings.SERVICE_NAME_DEFAULT_FLOW_CHANGE)
        time.sleep(1)
        self.click(xpath=page.service_dir)
        self.click(xpath=page.choose_service_dir)
        self.click(xpath=page.service_type)
        self.click(xpath=page.choose_service_type)
        self.click(xpath=page.comfirm_service)
        time.sleep(1)
        self.click(xpath=page.service_temp)
        self.click(xpath=page.choose_service_temp)
        self.click(xpath=page.service_next)
        self.click(xpath=page.flow_next)
        self.click(xpath=page.flow_commit)
        # self.click(xpath=page.commit_tickets)
        # text=self.get_text(xpath=page.service_instance)
        # self.assertText(text)



if __name__ == "__main__":
    seldom.main(debug=True)
