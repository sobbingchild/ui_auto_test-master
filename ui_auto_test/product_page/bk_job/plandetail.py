# -*- coding: utf-8 -*-
# @Time : 2024/10/23 15:59
# @File : plandetail.py

plan_create = {
    'path': '//button[@data-test-id="button_createPlan"]',
    'msg': '新建执行方案按钮'
}

mine = {
    'path': '//span[contains(text(),"我的方案")]',
    'msg': '我的方案'
}

select_template = {
    'path': '//div[@class="bk-select is-unselected is-default-trigger"]//div[@class="bk-select-name"]',
    'msg': '选择作业模板下拉'
}

search_template = {
    'path': '//input[@class="bk-select-search-input"]',
    'msg': '模板选择框》搜索'
}

select_template_submit = {
    'path': '//button[@class="mr10 bk-primary bk-button-normal bk-button"]//span[contains(text(),"确定")]',
    'msg': '模板选择框》确定'
}

plan_create_name = {
    'path': '//div[@class="bk-input-text"]/input[@class="bk-form-input only-bottom-border"]',
    'msg': '执行方案名称'
}

last_modified_by = {
    'path': '//div[contains(text(),"更新人")]',
    'msg': '执行方案列表》更新人'
}

link_createCrontab = {
    'path': '//div[@data-test-id="link_createCrontab"]',
    'msg': '更多》定时执行'
}

button_editPlan = {
    'path': '//div[@data-test-id="button_editPlan"]',
    'msg': '更多》编辑'
}

editPlan_task = {
    'path': '//div[@class="task-step-container"]/div[2]//div[@class="select-flag"]',
    'msg': '编辑执行方案》取消第二个执行步骤'
}

button_editPlanSave = {
    'path': '//button[@data-test-id="button_editPlanSave"]',
    'msg': '编辑执行方案》保存'
}

button_deletePlan = {
    'path': '//div[@data-test-id="button_deletePlan"]',
    'msg': '更多》删除'
}

plan_create_submit = {
    'path': '//button[@data-test-id="button_createPlanSubmit"]',
    'msg': '创建执行方案》提交'
}

to_execplan = {
    'path': '//button[@data-test-id="button_execPlan"]',
    'msg': '执行执行方案'
}

plan_create_reset = {
    'path': '//button[@data-test-id="button_createPlanReset"]',
    'msg': '创建执行方案》重置'
}

lanunch_button = {
    'path': '//button[@class="w120 bk-primary bk-button-normal bk-button"]//span[contains(text(),"执行")]',
    'msg': '创建执行方案》执行'
}