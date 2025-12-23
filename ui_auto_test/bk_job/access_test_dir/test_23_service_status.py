# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_22_service_status.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/18
-------------------------------------------------
"""
from bk_job.page import service_status as  page
from bk_job.test_dir.test_01_login import LoginBase
import time


class ServiceStatus(LoginBase):
    def test_service_status(self):
        '''检查服务状态'''
        self._test_login()
        self.click(xpath=page.navigation_publicScriptList)
        self.click(xpath=page.service_status)
        time.sleep(3)
        status = self.get_text(xpath=page.status)
        print(status)
        assert status == "正常"
        self.click(xpath=page.line_job_analysis)
        time.sleep(1)
        #
        self.click(xpath=page.line_job_backup)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_backup)
        time.sleep(1)
        #
        self.click(xpath=page.line_job_config)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_config)
        #
        self.click(xpath=page.line_job_crontab)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_crontab)
        #
        self.click(xpath=page.line_job_execute)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_execute)
        #
        self.click(xpath=page.line_job_gateway)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_gateway)
        #
        self.click(xpath=page.line_job_logsvr)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_logsvr)
        #
        self.click(xpath=page.line_job_manage)
        assert self.get_text(xpath=page.status) == "正常"
        self.click(xpath=page.line_job_manage)
