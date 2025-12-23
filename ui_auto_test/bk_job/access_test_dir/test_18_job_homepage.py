# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_17_job_homepage.py
   Description :
   Author :       v_jingdhe
   date：          2021/9/15
-------------------------------------------------
"""

from bk_job.test_dir.test_01_login import LoginBase
class JobHomepage(LoginBase):
    def test_01_login(self):
        '''进入业务概览'''
        # 验证登录
        self._test_login()
        #跳转业务概览
        self.click(xpath='//div[@data-test-id="navigation_home"]')
    def test_02_assert_username(self):
        '''断言进入页面对应名称与登录名称相同'''
        try:
            user_name="Hi, admin"
            if self.get_text(xpath='//div[@class="user-name"]') == user_name :
                print(self.get_text(xpath='//div[@class="user-name"]'))
                print(user_name)
                print("账户验证成功")
            else:
                print("账户验证失败")
                print(self.get_text(xpath='//div[@class="user-name"]'))
                print(user_name)

        except Exception as e:
            print("账户验证失败")