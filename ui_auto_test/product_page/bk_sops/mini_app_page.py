# -*- coding: utf-8 -*-
# @Time : 2021/12/1 14:33
# @File : mini_app_page.py
from . import template_page

# 新建轻应用
mini_app_form_create_button = {
    'path': '//button[@data-test-id="appmaker_form_creatApp"]',
    'msg': '新建轻应用表单button'
}
# 表单中的div
template_select_div = {
    'path': '//div[@data-test-id="appmaker_list_flows"]',
    'msg': '选择流程模板'
}
# 模板名称
template_name = {
    'path': '//p[@title="{}"]'.format(template_page.TEMPLATE_NAME),
    'msg': '选择流程模板名称'
}
# 确认创建轻应用
form_confirm_button = {
    'path': '//button[@data-test-id="appmaker_form_confirmEditBtn"]',
    'msg': '确认创建轻应用button'
}


mini_app_content = {
    'path': '//div[@data-test-id="appmaker_form_appList"]//div[@class="card-content"]',
    'msg': '轻应用内容详情'
}
mini_app_operation = {
    'path': '//div[@data-test-id="appmaker_form_appList"]//span[@class="common-icon-circle-ellipsis operate-btn"]',
    'msg': '轻应用操作'
}


mini_app_delete_button = {
    'path': '//li[@class="opt-btn"]',
    'msg': '轻应用内容详情'
}  # index=2
