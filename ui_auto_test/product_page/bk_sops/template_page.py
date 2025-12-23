# -*- coding: utf-8 -*-
# @Time : 2021/11/11 16:33
# @File : template_page.py
from bk_sops import settings

TEMPLATE_NAME = 'UI自动化测试模板'
JOB_TEMPLATE_NAME = 'JOB_UI自动化测试模板'
# 模板节点名称
NODE_NAME = ''
# 业务选择框
select_biz_name = {
    'path': '//div[@class="container-header"]//div[@class="bk-select-name"]',
    'msg': '选择业务框'
}
# 业务输入框
biz_input = {
    'path': '//div[@class="bk-tooltip-content"]//input',
    'msg': '输入业务名称'
}
# 选择业务
select_biz = {'path': '//div/span[contains(text(),"{}")]'.format(settings.BIZ_NAME),
              'msg': '选择业务'
              }
# 新建项目流程button
create_template_button = {
    'path': '//button[@data-test-id="process_form_creatProcess"]',
    'msg': '新建项目流程button'}
# create_template_button = "document.querySelector('button').click()"
# 流程节点
flow_node = {
    'path': '//div[@class="node-name"]',
    'msg': '流程节点'}
# 蓝鲸通知系列插件
list_bk = {
    'path': '//div[@data-test-id="templateEdit_list_BK"]',
    'msg': '蓝鲸服务系列插件'}
# 定时插件
sleep_timer = {
    'path': '//li[@data-test-id="templateEdit_list_sleepTimer"]',
    'msg': '定时插件'}
# 定时插件输入框
timer_input = {
    #'path': '//section[@data-test-id="templateEdit_form_inputParamsInfo"]//div[@class="tag-input rf-tag-form"]/div',
    'path': '//section[@data-test-id="templateEdit_form_inputParamsInfo"]//div[@data-test-name="formTag_input_divInput"]',
    'msg': '定时插件输入框'}
# 插件节点保存
node_save_button = {
    'path': '//button[@data-test-id="templateEdit_form_saveNodeConfig"]',
    'msg': '插件节点保存'}
# 模板基础信息补充
template_base_message = {
    'path': '//i[@class="common-icon-square-attribute"]',
    'msg': '模板基础信息'}
# 流程模板名称
template_name = {
    'path': '//input[@placeholder="请输入流程模板名称"]',
    'msg': '流程模板名称'}
# 流程模板基础信息保存
template_base_message_save_button = {
    'path': '//div[@class="btn-wrap"]//span[contains(text(),"确定")]',
    'msg': '流程模板基础信息保存'}
# 流程模板保存
template_save_button = {
    'path': '//button[@data-test-id="templateEdit_form_saveCanvas"]',
    'msg': '流程模板保存'}
# 模板名称
template_flow_name = {
    'path': '//a[@title="{}"]'.format(TEMPLATE_NAME),
    'msg': '模板名称'}
# 新建任务button
create_task_button = {
    'path': '//button[@data-test-id="templateEdit_form_createTask"]',
    'msg': '新建任务button'}
# 新建任务下一步
task_next_step_button = {
    'path': '//button[@data-test-id="createTask_form_nextStep"]',
    'msg': '新建任务下一步'}
# 填写参数下一步
form_create_task_button = {
    'path': '//button[@data-test-id="createTask_form_createTask"]',
    'msg': '填写参数下一步'}
# 创建任务button
task_execute_button = {
    'path': '//button[@data-test-id="taskExecute_form_executeBtn"]',
    'msg': ' 创建任务button'}
# 勾选label

form_checkbox = {
    'path': '//tbody//td//label',
    'msg': ' 勾选流程模板'}
# 批量操作
batch_operation = {
    'path': '//div[@class="export-tpl-btn"]',
    'msg': ' 点击批量操作'}
# batch_operation = '//div[@class="bk-dropdown-trigger"]'
# 模板删除
list_delete_process = '//li[@data-test-id="process_list_deleteProcess"]'
# 删除按钮
delete_button = {
    'path': '//button[@data-test-id="process_form_deleteProcess"]',
    'msg': ' 流程页面删除button'}
# 搜索流程模板input
search_temp_name = {
    'path': '//div[@contenteditable="plaintext-only"]',
    'msg': ' 搜索流程模板'}
# 流程模板列表名称
template_list_name = {
    'path': '//tbody//td[3]//a',
    'msg': ' 流程模板名称'}

job_plugin_list = {
    'path': '//div[@data-test-id="templateEdit_list_JOB"]',
    'msg': 'JOB插件列表'
}
job_fast_execute_script = {
    'path': '//li[@data-test-id="templateEdit_list_jobFastExecuteScript"]',
    'msg': '快速执行脚本插件'
}
node_detail_scrollTop = {
    'path': "document.querySelectorAll('.config-form')[0].scrollTop=600",
    'msg': '节点详情滚动条'
}
job_execute_script_textarea_scrollTop = {
    'path': '//section[@class="code-editor"]//div[@class="slider"]',
    'msg':'脚本内容textarea滚动'
}
job_execute_script_textarea = {
    'path':'//section[@class="code-editor"]',
    'msg':'脚本内容输入框'
}
job_execute_script_content={
    'path':'//section[@class="code-editor"]//textarea',
    'msg':'脚本内容'
}
job_execute_script_ip_list = {
    'path':'//div[@class="el-textarea"]/textarea',
    'msg':'输入IP'
}
job_execute_script_system_name = {
    'path':'//input[@placeholder="请输入在蓝鲸作业平台上注册的账户名"]',
    'msg':'输入系统名称'
}