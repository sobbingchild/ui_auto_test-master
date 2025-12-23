# -*- coding: utf-8 -*-
# @Time : 2021/7/22 17:08
# @File : create_shell_script_page.py
# @Project : bk_job

# 脚本名称
SCRIPT_NAME = 'ui_shell_script'
PYTHON_SCRIPT_NAME = 'ui_python_script'
# 脚本版本
SCRIPT_VERSION = '0.0.1'
# 脚本描述
SCRIPT_TEXT = 'echo UI_AUTO_TEST'

PYTHON_SCRIPT_TEXT = 'print UI_AUTO_TEST'
# 断言页面版本管理文字
PAGE_TEXT = '版本管理'
# 断言页面title
HTML_TITLE = '作业平台 | 腾讯蓝鲸智云 | 脚本管理'
# 上线提示文案
ONLINE_ALERT_TEXT = '确定上线该版本？'
# 脚本页面url
SCRIPT_MANAGE = 'http://job.ee207.bktencent.com/27/script_manage/'
# 资源-脚本元素
navigation_scriptManage = '//div[@data-test-id="navigation_scriptManage"]'
# 无脚本存在判断
scriptPage_title = '//div[@class="product_page-title"]'
# 无脚本新增按钮
scriptPage_button = '//div[@class="product_page-action"]/button'
# 已存在脚本新增按钮
append_button = '//div[@class="right-box"]/button'
# 脚本名称
input_script_name = '//input[@type="text"]'
# 脚本描述
script_description = '//textarea[@type="textarea"]'
# 脚本版本
script_version = '//input[@type="text"]'
# 脚本内容
script_content = '//textarea[@class="ace_text-input"]'
# 提交按钮
submit_button = '//div[@role="action"]//button[1]'
# 切换python脚本
python_click = '//div[contains(text(),"Python")]'
# ---------------------------------------------------------#

# 脚本状态
script_status = '//tbody//div[@class="cell"]/span'
# 调试Button
debug_button = '//div[@class="layout-footer"]/button[1]'
# 上线Button ,index=1
online_button = '//div[@class="layout-footer"]/div/button'
# 上线提示
online_alert_text = '//h2[@class="confirm-title"]'
# 确定上线button
online_alert_button = '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]'
