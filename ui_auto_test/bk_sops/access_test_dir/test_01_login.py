# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_01_login.py
   Description : 
   Author :       v_adanchen
   date：          2021/7/9
-------------------------------------------------
"""


from bk_sops import settings

from public_method.login import LoginBase


class Login(LoginBase):
    def test_login(self):
        ''' 登录态验证'''
        self._test_login(target_url=settings.SOPS_URL, index_title=settings.INDEX_TITLE)
