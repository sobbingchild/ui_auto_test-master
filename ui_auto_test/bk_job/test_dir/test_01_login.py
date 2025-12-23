# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_01_login.py
   Description : 
   Author :       lunckliu
   date：          2024/9/2
-------------------------------------------------
"""
from product_page import settings
from public_method.login import LoginBase


class Login(LoginBase):
    '''登录'''
    def test_login(self):
        ''' 登录态验证'''
        self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
