# -*- coding: utf-8 -*-
# @Time : 2024/10/24 15:59
# @File : crons.py

crons_name = {
    'path': '//div[@class="jb-input"]//div[@class="bk-input-text"]/input[@class="bk-form-input"]',
    'msg': '任务名称'
}

time_input = {
    'path': '//div[@class="time-input"]/input[@class="input"]',
    'msg': '时间输入框'
}

run_once = {
    'path': '//div[contains(text(),"单次执行")]',
    'msg': '单次执行'
}

notify_to = {
    'path': '//div[@class="user-selector"]/div[@class="user-selector-layout"]',
    'msg': '通知对象'
}

notify_to_personnel = {
    'path': '//span[contains(text(),"运维人员")]',
    'msg': '选择运维人员'
}

notify_by = {
    'path': '//span[contains(text(),"全部")]',
    'msg': '选择全部'
}

end_time_settings = {
    'path': '//span[contains(text(),"执行前通知")]',
    'msg': '执行前通知勾选框'
}

round_robin = {
    'path': '//div[contains(text(),"周期执行")]',
    'msg': '周期执行'
}

crons_submit = {
    'path': '//span[contains(text(),"提交")]',
    'msg': '提交'
}

crons_save = {
    'path': '//span[contains(text(),"保存")]',
    'msg': '保存'
}

template_crons = {
    'path': '//div[@data-placeholder="选择作业模板"]',
    'msg': '定时任务》作业模板选择框'
}

plan_crons = {
    'path': '//div[@class="bk-select is-unselected is-default-trigger"]//div[@class="bk-tooltip-ref"]',
    'msg': '定时任务》执行方案选择'
}

create_button = {
    'path': '//button[@data-test-id="button_createCrontab"]',
    'msg': '新建定时任务按钮'
}

edit_crons = {
    'path': '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_editCrontab"]',
    'msg': '编辑定时任务按钮'
}

del_crons = {
    'path': '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_deleteCrontab"]',
    'msg': '删除定时任务按钮'
}

execrecord_crons = {
    'path': '//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_crontabExecRecord"]',
    'msg': '执行记录按钮'
}

toggle_crontab_status = {
    'path': '//div[@class="bk-table-fixed-body-wrapper"]//div[@data-test-id="button_toggleCrontabStatus"]',
    'msg': '启动按钮'
}


