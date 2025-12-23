# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_11_job_launch.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/3
-------------------------------------------------
"""
from bk_job.page import job_launch as page
from bk_job.test_dir.test_01_login import LoginBase
from bk_job import settings
from bk_job.bk_exception import ApiError
import time
# 不依赖执行方案
class JobLaunch(LoginBase):
    def test_01_excute(self):
        '''执行执行方案'''
        self._test_login()
        if not settings.CREATE_API_STATUS:
            raise ApiError('创建模板失败，执行方案失败')
        self.click(xpath=page.navigation_planManage)
        self.click(xpath=page.to_excute)
        self.click(xpath=page.excute)

    def test_02_check(self):
        '''检查执行执行结果'''
        if not settings.CREATE_API_STATUS:
            raise ApiError('创建模板失败，执行方案失败')
        time.sleep(1)
        status = self.get_text(xpath=page.excute_status)
        print(status)
