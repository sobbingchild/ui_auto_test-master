from time import sleep
import seldom

from bk_cmdb.test_dir import test_01_login
from bk_cmdb import settings
from bk_cmdb.page import homepage, business
from public_method.keyboard_operation import MyWebDriver


class HostSearch(seldom.TestCase):
    def test_01_single_hostsearch(self):
        """搜索单个存在的IP(主机搜索)"""
        test_01_login.Login.test_login(self)
        # 点击业务
        test_01_login.Login.click_business(self)
        # 等待后输入业务名并点击
        sleep(1)
        # 默认进入蓝鲸业务，点击公共组件
        self.click(xpath=business.common_components)
        # 获取公共组件的IP值，获取两次
        global BluekingHostIp
        sleep(1)
        global BluekingHostIp_second
        sleep(1)
        BluekingHostIp = self.get_text(xpath=business.get_host)
        BluekingHostIp_second = self.get_text(xpath=business.get_host_second)
        print(BluekingHostIp)
        print(BluekingHostIp_second)
        # 进入配置平台首页
        test_01_login.Login.test_login(self)
        # 输入单个存在的ip，搜索
        self.type(css=homepage.index_host_search, text=BluekingHostIp)
        sleep(1)
        self.click(css=homepage.index_button_search)
        sleep(1)
        # 断言
        self.assertText(settings.BUSINESS_KEY)

    def test_02_multiple_hostsearch(self):
        """搜索多个存在的IP（主机搜索）"""
        # 进入首页
        test_01_login.Login.test_login(self)
        sleep(1)
        # 输入多个存在的ip(linux_pagent)
        self.type(css=homepage.index_host_search, text=BluekingHostIp)
        # 模拟空格键键，换行
        MyWebDriver.Keys(css=homepage.index_host_search).space()
        # 再次输入ip
        self.type(css=homepage.index_host_search, text=BluekingHostIp_second)
        sleep(1)
        # 搜索
        self.click(css=homepage.index_button_search)
        sleep(1)
        # 断言
        self.assertText(settings.BUSINESS_KEY)

    def test_03_section_hostsearch(self):
        """搜索部分存在的IP（主机搜索）"""
        test_01_login.Login.test_login(self)
        sleep(1)
        # 输入部分存在及不存在的ip
        self.type(css=homepage.index_host_search, text=BluekingHostIp)
        # 模拟enter/空格键，换行
        MyWebDriver.Keys(css=homepage.index_host_search).space()
        # 再次输入ip
        self.type(css=homepage.index_host_search, text=settings.TEST_IP)
        sleep(1)
        # 搜索
        self.click(css=homepage.index_button_search)
        sleep(1)
        # 断言
        self.assertText(settings.BUSINESS_KEY)
