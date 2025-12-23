# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_20_ip_whitelist.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/17
-------------------------------------------------
"""
from bk_job import settings
import time
from bk_job.test_dir.test_01_login import LoginBase
from bk_job.page import ip_whitelist  as page
from pre_data.job_api_demo import JobApi
from bk_job.bk_exception import ApiError

api = JobApi()
ip_list = api.get_hosts_ip()
# 依赖IP
class IpWhite(LoginBase):
    def test_01_new_ip(self):
        '''新建IP白名单'''
        self._test_login()
        self.click(xpath=page.navigation_publicScriptList)
        time.sleep(1)
        self.click(xpath=page.navigation_whiteIp)
        time.sleep(1)
        self.click(xpath=page.new_ip)
        time.sleep(1)
        #self.click(xpath=page.bz_blueking,index=1)
        text = self.get_text(xpath=page.bz_blueking,index=1)
        self.click(xpath=page.bz_blueking,index=1)
        self.click(xpath=page.bz_unselected.format(text))
        self.click(xpath=page.bz_selected)
        self.click(xpath=page.slider_title)
        if ip_list:
            self.type(xpath=page.input_ip, text=ip_list[0])
        else:
            raise ApiError("API请求错误")
        self.type(xpath=page.input_notes, text=settings.TEST_JOB_COMMON)
        self.click(xpath=page.action_on)
        self.click(xpath=page.commit)
        time.sleep(1)

    def test_02_edit_ip(self):
        '''修改IP'''
        self.click(xpath=page.edit_ipwhite)
        time.sleep(1)
        self.type(xpath=page.input_notes, text=settings.TEST_JOB_COMMON)
        self.click(xpath=page.save_ip)
        time.sleep(1)

    def test_03_search_ip(self):
        '''搜索IP'''
        self.click(xpath=page.search_ip)
        if ip_list:
            self.type_enter(xpath=page.search_ip, text=ip_list[0])
        else:
            raise ApiError("API请求错误")
        assert self.get_text(xpath=page.ip_num) == ip_list[0]

    def test_04_def_ip(self):
        '''删除IP'''
        time.sleep(1)
        self.click(xpath=page.del_ip)
        self.click(xpath=page.del_comfirm)
