# -*- coding: utf-8 -*-
# @Time : 2021/11/30 15:21
# @File : clocked_task_page.py

from . import template_page

# 新建计划任务button
clocked_form_create_button = {
    'path': '//button[@data-test-id="clockedList_form_createTask"]',
    'msg': '新建计划任务侧滑框button'
}
# 计划任务选择流程模板下拉框
clocked_template_select = {
    'path': '//div[@data-test-id="clockedEdit_form_selectTemplate"]',
    'msg': '计划任务选择流程模板下拉框'
}
# 计划任务名称
clocked_task_name = {
    'path': '//div[@data-test-id="clockedEdit_form_taskName"]//input',
    'msg': '输入计划任务名称'
}
# 启动时间input
start_time_input = {
    'path': '//div[@data-test-id="clockedList_form_startTime"]//input',
    'msg': '输入启动时间'
}
# 创建计划任务button
clocked_create_button = {
    'path': '//button[@data-test-id="clockedEdit_form_saveBtn"]',
    'msg': '创建计划任务button'
}
# 任务状态
task_instance = {
    'path': '//span[@title="{}_计划执行"]/../../../td[8]'.format(template_page.TEMPLATE_NAME),
    'msg': '计划任务执行状态'
}
delete_clocked_task_button = {
    'path': '//span[@title="{}_计划执行"]/../../..//a[@data-test-id="clockedList_table_deleteBtn"]'.format(
        template_page.TEMPLATE_NAME),
    'msg': '计划任务执行状态'
}

# 执行方案下拉框
execution_scheme = {
    'path': '//div[@data-test-id="clockedEdit_form_selectScheme"]/div/div/div',
    'msg': '计划任务执行方案下拉框'
}
