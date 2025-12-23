# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_34_del_service_dir.py
   Description : 
   Author :       v_adanchen
   date：          2021/1/19
-------------------------------------------------
"""
import seldom
import time
import test_dir.test_0_login
import settings
class DelService(seldom.TestCase):
    def test_del_service(self):
        #登录
        test_dir.test_0_login.Login.test_login(self)
        # 点击后台管理
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        #删除
        self.click(xpath="//div[@class='bk-table-header-label']//span[@tabindex=0]")
        self.click(xpath="//div[@class='bk-more-search']/button[@title='批量删除']")
        self.click(xpath="//div[@class='bk-dialog-wrapper']//div/button[@name='confirm']")
        #判断是否删除成功
        self.click(xpath="//div[@class='bk-input-text']/input[@placeholder='请输入服务名']")
        self.type_enter(xpath="//div[@class='bk-input-text']/input[@placeholder='请输入服务名']", text=settings.API_NODE_FLOW_NAME)
        assert self.get_text(xpath="//div[@class='bk-table-empty-block']/span/div") == "暂无数据"
        print("服务删除成功")