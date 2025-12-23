# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     job_plan.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/2
-------------------------------------------------
"""
from bk_job import settings

# 执行方案
navigation_planManage = "//div[@data-test-id='navigation_planManage']"
# 新建执行方案
new_plan = "//div[@class='task-manage-plan-product_page']//div//button//span[contains(.,'新建')]"
# 选择作业模板
choose_job_temp = "//div[@class='jb-form-item-content']"
job_temp_name = "//ul/li/div[@class='bk-option-content']/div[@title='{}']".format(settings.TEST_JOB_COMMON)
job_temp_comfirm = "//div[@class='bk-dialog-footer']//span[contains(.,'确定')]"

# 提交执行方案
commit_plan = "//button[@data-test-id='button_createPlanSubmit']"

# 执行
to_excute_plan = "//div[@class='layout-footer']//span[contains(.,'去执行')]"

# 确定执行
confirm_excute = "//div[@class='bk-dialog-footer']//button[1]"

excute_plan = "//div[@class='action-wraper']//span[contains(.,'执行')]"

step_comfirm_to = "//div[@class='step-action']//span[contains(.,'确认继续')]"
step_comfirm = "//div[@class='confirm-options']//span[contains(.,'确定')]"

excute_status = "//div[@class='task-exection-status-bar']//div[@class='status']//span[2]"

status_success = "成功"
status_fail = "失败"

# 执行方案删除
plan_more = '//div[@class="bk-table-fixed-right"]//tr//td//i'
plan_del = "//div[@class='tippy-content']/div/div[contains(.,'删除')]"
plan_del_text_pos = "//div[@class='jb-popover-content']/h2"
plan_del_text = settings.TEST_PLAN_DEL_TEXT
plan_del_confirm = "//div[@class='confirm-options']/button[1]"
