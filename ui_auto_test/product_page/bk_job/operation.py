# -*- coding: utf-8 -*-
# @Time : 2024/10/12 15:59
# @File : operation.py

template_create = {
    'path': '//button[@data-test-id="button_templateCreate"]',
    'msg': '新建作业模板按钮'
}

debug_temp = {
    'path': '//div[@class="bk-table-fixed-right"]//a[@data-test-id="link_debugTemplate"]',
    'msg': '调试'
}

launch_button = {
    'path': '//span[contains(text(),"去执行")]',
    'msg': '调试》去执行'
}

launch_global_button = {
    'path': '//span[contains(text(),"执行")]',
    'msg': '调试》执行'
}

continue_launch = {
    'path': '//span[contains(text(),"确认继续")]',
    'msg': '确认继续'
}

plandetail_temp = {
    'path': '//div[@class="bk-table-fixed-right"]//a[@data-test-id="link_planDetail"]',
    'msg': '执行方案'
}

tags_temp = {
    'path': '//div[contains(text(),"场景标签")]',
    'msg': '场景标签'
}

temp_more = {
    'path': '//div[@class="bk-table-fixed-right"]//div[@class="list-operation-extend"]',
    'msg': '更多按钮'
}

edit_temp = {
    'path': '//div[@data-test-id="button_editTemplate"]',
    'msg': '更多》编辑'
}

copy_temp = {
    'path': '//div[@data-test-id="button_cloneTemplate"]',
    'msg': '更多》克隆'
}

got_it = {
    'path': '//span[contains(text(),"我知道了")]',
    'msg': '我知道了'
}

del_temp = {
    'path': '//div[@data-test-id="button_deleteTemplate"]',
    'msg': '更多》删除'
}

check_temp = {
    'path': '//span[text()="立即查看"]',
    'msg': '立即查看'
}
check_del_temp = {
    'path': '//button[@data-test-id="button_deleteTemplate"]',
    'msg': '立即查看》删除'
}

confirm_button = {
    'path': '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]//span[contains(text(),"确定")]',
    'msg': '二次确认》确定'
}

temp_name_input = {
    'path': '//input[@placeholder="输入作业模板名称"]',
    'msg': '模板名称'
}

global_variables = {
    'path': '//div[@data-test-id="button_create_global_variable"]',
    'msg': '全局变量'
}

str_div = {
    'path': '//div[contains(text(),"字符串")]',
    'msg': '全局变量》字符串'
}

name_space = {
    'path': '//div[contains(text(),"命名空间")]',
    'msg': '全局变量》命名空间'
}

cipher_text = {
    'path': '//div[contains(text(),"密文")]',
    'msg': '全局变量》密文'
}

array_variable = {
    'path': '//div[contains(text(),"数组")]',
    'msg': '全局变量》数组'
}

host_list = {
    'path': '//div[contains(text(),"主机列表")]',
    'msg': '全局变量》主机列表'
}

select_host = {
    'path': '//span[contains(text(),"选择主机")]',
    'msg': '全局变量》主机列表》选择主机'
}

name_variables = {
    'path': '//input[@placeholder="变量名仅支持大小写英文字母或下划线 [必填]"]',
    'msg': '变量名称'
}

default_value = {
    'path': '//input[@placeholder="请输入变量的初始值 [可选]"]',
    'msg': '初始值'
}

steps_jobs = {
    'path': '//div[@data-test-id="button_create_step"]',
    'msg': '作业步骤'
}

assign_variable = {
    'path': '//span[contains(text(),"赋值可变")]',
    'msg': '赋值可变'
}

is_required = {
    'path': '//span[contains(text(),"执行时必填")]',
    'msg': '执行时必填'
}

variable_submit = {
    'path': '//div[@class="jb-sideslider-footer"]//span[contains(text(),"提交")]',
    'msg': '侧滑内提交'
}

submit = {
    'path': '//button[@data-test-id="button_operationTemplateSubmit"]',
    'msg': '提交'
}

edit_temp_confirmation = {
    'path': '//div[@class="bk-radio-button-text"]/span[contains(text(),"人工确认")]',
    'msg': '新增作业步骤》人工确认'
}

