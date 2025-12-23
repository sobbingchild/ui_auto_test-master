# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     job_search.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/6
-------------------------------------------------
"""
from bk_job import settings

# 执行方案
navigation_planManage = "//div[@data-test-id='navigation_planManage']"

input_text = "//textarea[@class='input-box']"

text = "//div[@class='name-wraper']/div[contains(.,'{}')]".format(settings.TEST_JOB_COMMON)

