# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     job_launch.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/3
-------------------------------------------------
"""
from bk_job import settings

# 执行方案
navigation_planManage = "//div[@data-test-id='navigation_planManage']"

# 去执行
to_excute = '//div[@class="bk-table-fixed-right"]//td//button[@data-test-id="button_execPlan"]'

# 确认执行
comfirm_lanuch = "//div[@class='footer-wrapper']/button[1]"

# 执行
excute = "//div[@class='action-wraper']/button/div/span[contains(.,'执行')]"
comfirm_to = "//div[@class='step-action']//span[contains(.,'确认继续')]"
comfirm = "//div[@class='confirm-options']//span[contains(.,'确定')]"

excute_status = "//div[@class='task-exection-status-bar']//div[@class='status']//span[2]"

status_success = "执行成功"
status_fail = "执行失败"
