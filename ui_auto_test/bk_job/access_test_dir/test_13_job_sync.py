# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_12_job_sync.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/6
-------------------------------------------------
"""
from bk_job.page import job_sync as page
import time
from bk_job.test_dir.test_01_login import LoginBase
from bk_job import settings
from bk_job.bk_exception import ApiError

# 同步执行方案依赖cron_temp模板
class JobSync(LoginBase):
    def test_job_sync(self):
        '''同步执行方案'''
        self._test_login()
        self.click(xpath=page.navigation_taskManage)
        if not settings.CREATE_API_STATUS:
            raise ApiError('创建模板失败，执行方案失败')
        self.click(xpath=page.more)
        self.sleep(1)
        self.click(xpath=page.edit)
        time.sleep(1)
        self.click(xpath=page.step_name)
        self.type(xpath=page.edit_scrip, text=settings.TEST_SYNC_TEXT)
        self.click(xpath=page.select_account)
        time.sleep(1)
        self.click(xpath=page.save_scrip)
        time.sleep(1)
        self.click(xpath=page.save_temp)
        time.sleep(1)
        self.click(xpath=page.job_sync)
        self.click(xpath=page.job_sync_next)
        self.click(xpath=page.job_sync_close)
        time.sleep(1)
        print("同步成功")
