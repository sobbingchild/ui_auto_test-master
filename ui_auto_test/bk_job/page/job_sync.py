# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     job_sync.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/6
-------------------------------------------------
"""
from bk_job import settings


navigation_taskManage = "//div[@data-test-id='navigation_taskManage']"

# 提前埋好的执行方案名称
# job_name="//div[@class='plan-name-box']/div/div[contains(.,'{}')]".format(settings.TEST_JOB_USE)


more = '//div[@class="bk-table-fixed-right"]//td//div//i'
edit = '//div[@data-test-id="button_editTemplate"]'
step_name = "//div[@class='step-content']/div[@class='step-name']"
edit_scrip = "//textarea[@class='ace_text-input']"
select_account ="//span[contains(.,'执行账号')]/../../div"

save_scrip = "//div[@class='bk-sideslider-footer']/div//span[contains(.,'保存')]"
save_temp = "//button//span[contains(.,'保存')]"
job_sync = "//div[@class='bk-dialog-type-sub-header']//button//span[contains(.,'立即同步')]"

job_sync_next = "//div[@class='sync-plan-action']//button//span[contains(.,'立即同步')]"
job_sync_close="//div[@class='sync-plan-action']//button//span[contains(.,'完成')]"
