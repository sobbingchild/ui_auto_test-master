# -*- coding: utf-8 -*-
# @Time : 2021/11/11 15:22
# @File : test_02_index_page_check.py

# from bk_sops.access_test_dir.test_01_login import LoginBase
from public_method.login import LoginBase
from bk_sops import settings


class IndexPage(LoginBase):
    def test_01_check_index_message(self):
        '''检查标准运维首页 对应模块加载情况'''
        # 登录态验证
        #self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
        self.open(settings.SOPS_URL)
        # 检查是否进入首页
        self.assertText('首页')
        # 断言常用项目
        self.assertText('常用项目')
        # 断言我的收藏
        self.assertText('我的收藏')
        # 断言我的动态
        self.assertText('我的动态')
        print('首页页面加载成功')
