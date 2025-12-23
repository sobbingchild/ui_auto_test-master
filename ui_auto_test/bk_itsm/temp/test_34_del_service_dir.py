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
class DelServiceDir(seldom.TestCase):
    def test_del_service_dir(self):
        #登录
        test_dir.test_0_login.Login.test_login(self)
        # 点击后台管理
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        #self.click(xpath="//div[@class='navigation-sbmenu-title']/span[contains(.,'服务管理')]")
        self.click(xpath="//div/div/div/a[2]/span[2][contains(.,'目录')]")
        #移除服务
        self.click(xpath="//div/div[@class='tree-node']/span[@title='{}']".format(settings.TEST_UI_DIR))
        self.click(xpath="//div/table/tbody/tr/td[7]/button/div/span[contains(.,移除)]")
        self.click(xpath="//div[@class='bk-dialog-footer']/div/button[@name='confirm']")
        #删除目录
        self.click(xpath="//div[@class='bk-tree-table-directory']//table/thead//span[@tabindex=0]")
        self.click(xpath="//div[@class='bk-form-content']/button[@title='批量移除']")
        self.click(xpath="//div[@class='bk-dialog-footer']/div/button[@name='confirm']")
        #判断是否删除成功
        self.click(xpath="//div/input[@placeholder='请输入搜索关键字']")
        self.type(xpath="//div/input[@placeholder='请输入搜索关键字']", text=settings.TEST_UI_DIR)
        self.Keys(xpath="//div/input[@placeholder='请输入搜索关键字']").enter()
        self.click(xpath="//ul[@class='bk-tree']//span[contains(.,'test_ui_dir1')]/../i")
        self.click(xpath="//div[@class='bk-tree-more']//li[@title='删除']")
        self.click(xpath="//div[@class='footer-wrapper']/button[@name='confirm']")
        time.sleep(3)
        assert self.get_text(xpath="//div/table/tbody/tr/td/p[contains(.,'暂无数据')]") == "暂无数据"
        print("服务目录删除成功")