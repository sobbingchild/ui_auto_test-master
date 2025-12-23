# -*- coding: utf-8 -*-
# @Time : 2021/9/2 20:50
# @File : crontab_task.py
# @Project : bk_job
from bk_job import settings
# 定时任务作业模板名称
CRON_JOB_TEMP = settings.TEST_JOB_CRON_TEMP
# 周期定时任务
ROUND_CRON_NAME = 'UI_ROUND_CRON_NAME'
# 单次定时任务
ONCE_CRON_NAME = 'UI_ONCE_CRON_NAME'
# 执行策略
select_repeat_frequency = '//div[@class="bk-radio-button-text"]'
# 定时任务页面入口
crontab_task = '//div[@data-test-id="navigation_cronJob"]'

# 无定时任务存在判断
scriptPage_title = '//div[@class="product_page-title"]'
# 无定时任务新增按钮
scriptPage_button = '//div[@class="product_page-action"]/button'
# 已存在定时任务新增按钮
append_button = '//div[@class="right-box"]/button'
# 任务名称
task_name = '//div[@class="bk-input-text"]//input'
# 选择作业模板
select_job_tmp = '//div[@data-placeholder="选择作业模板"]'
# 作业模板名称
job_tmp = '//div[contains(text(),"{}")]'.format(CRON_JOB_TEMP)
# 选择执行方案
select_job_plan = '//div[@data-placeholder="选择执行方案"]'
# 选择提交
submit_button = '//span[contains(text(),"提交")]'
# 保存
save_button = '//span[contains(text(),"保存")]'

# 编辑一次定时任务按钮
edit_cron_button = '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_editCrontab"]'

#定时任务跳转
cronJob = '//div[@data-test-id="navigation_cronJob"]'
# 删除定时任务按钮
def delete_cron_button(name):
    del_button = '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_deleteCrontab"]'
    return del_button


# 确认删除按钮
confirm_del_button = '//div[@class="confirm-options"]//button[1]'
