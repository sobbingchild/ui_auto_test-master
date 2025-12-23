# -*- coding: utf-8 -*-
# @Time : 2021/11/29 11:56
# @File : periodic_task_page.py
from . import template_page

# 新建周期任务button
periodiclist_form_create_button = {
    'path': '//button[@data-test-id="periodicList_form_createTask"]',
    'msg': '新建周期任务button'
}
# 选择项目流程
select_template = {
    'path': '//div[@data-test-id="periodicEdit_form_selectTemplate"]',
    'msg': '选择项目流程'
}
# 项目流程模板名称
template_name = {
    'path': '//li//p[@title="{}"]'.format(template_page.TEMPLATE_NAME),
    'msg': '选择流程名称'
}
# 周期任务名称
periodic_task_name = {
    'path': '//div[@data-test-id="periodicEdit_form_taskName"]//input',
    'msg': '填写周期任务名称'
}
# 创建周期任务button
create_periodic_task_button = {
    'path': '//button[@data-test-id="periodicEdit_form_saveBtn"]',
    'msg': '创建周期任务button'
}
# 清空span
crontab_span = {
    'path': '//div[@class="time-input"]/input',
    'msg': '清空周期表达式span'
}
# 运行次数
running_time = {
    'path': '//span[@title="{}_周期执行"]/../../../../td[9]'.format(template_page.TEMPLATE_NAME),
    'msg': '检查运行次数'
}
# 删除
delete_periodic_task_button = {
    'path': '//div[@periodic-task-name="{}_周期执行"]//a[@data-test-id="periodicList_table_deleteBtn"]'.format(
        template_page.TEMPLATE_NAME),
    'msg': '删除周期任务button'
}
# 确认删除button
confirm_button = {
    'path': '//button[@name="confirm"]',
    'msg': '确定删除button'
}
# 执行方案下拉框
execution_scheme = {
    'path': '//div[@data-test-id="periodicEdit_form_selectScheme"]/div/div/div',
    'msg': '周期任务执行方案下拉框'
}
