# -*- coding: utf-8 -*-
# @Time : 2021/7/28 15:18
# @File : script_version_page.py
# @Project : bk_job

# 版本号
version = '//a'
# 提交按钮
submit_button = '//div[@class="layout-footer"]//button[1]'

script_page = '//div[@data-test-id="navigation_scriptManage"]'
# 版本控制按钮
def version_button(script_name):
    # 3.4.0 修改table
    # button = "//td//span[contains(text(),'{}')]/../../../../../..//button".format(script_name)
    button = '//div[@class="bk-table-fixed-right"]//table//td//button//span[contains(text(),"版本管理")]'
    return button


# 复用并新建按钮
def create_new_version(script_version):
    button = "//a[text()='{}']/../../..//button".format(script_version)
    return button
