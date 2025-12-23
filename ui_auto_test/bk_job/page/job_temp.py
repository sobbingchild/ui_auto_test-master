# -*- coding: utf-8 -*-
# @Time : 2021/8/23 15:40
# @File : job_temp.py
# @Project : bk_job

from bk_job import settings

# 模板名称
TEST_UI_JOB_TEMP = settings.TEST_UI_JOB_TEMP
STR_VARIABLE_NAME = 'str_name'
NAME_SPACE_VARIABLE_NAME = 'name_space'
HOST_LIST_VARIABLE_NAME = 'host_list'
CIPHER_TEXT_VARIABLE_NAME = 'cipher_text'
ARRAY_VARIABLE_NAME = 'array'
# 脚本描述
SCRIPT_TEXT = 'echo UI_AUTO_TEST'
#API请求是否成功
API_STATUS = False

# 进入作业模板
job_temp_index = "//div[{}='navigation_taskManage']".format(settings.DATA_TEST_ID)
# 新建作业模板button
create_temp_button = "//button[{}='button_templateCreate']".format(settings.DATA_TEST_ID)
# 输入模板名称input
temp_name_input = '//input[@placeholder="输入作业模板名称"]'
# 点开全局变量button
button_create_global_variable = '//div[@data-test-id="button_create_global_variable"]'
# 字符串类型变量div
str_div = '//div[contains(text(),"字符串")]'
# 命名空间类型变量div
name_space = '//div[contains(text(),"命名空间")]'
# 密文类型变量div
cipher_text = '//div[contains(text(),"密文")]'
# 数组类型变量div
array_variable = '//div[contains(text(),"数组")]'
# 主机列表
host_list = '//div[contains(text(),"主机列表")]'
# 选择主机
select_host = '//span[contains(text(),"选择主机")]'
# 勾选主机
check_host = '//div[@class="host-list"]//thead//label'
# 点击主机列表页确定
host_list_submit = '//span[contains(text(),"确定")]'
# 变量名称input
variable_name = '//input[@placeholder="变量名仅支持大小写英文字母或下划线 [必填]"]'
# 初始值input
initial_value = '//input[@placeholder="请输入变量的初始值 [可选]"]'
# 赋值可变
assign_variable = '//span[contains(text(),"赋值可变")]'
# 变量提交button
variable_submit = '//div[@class="jb-sideslider-footer"]//span[contains(text(),"提交")]'

# 增加作业步骤
button_create_step = '//div[@data-test-id="button_create_step"]'
# 脚本内容
script_content = '//textarea[@class="ace_text-input"]'
# 下拉作业步骤页面js
js_script = "document.querySelectorAll('.bk-sideslider-content')[0].scrollTop=100"
# 保存作业步骤
step_submit_button = '//button//span[contains(text(),"提交")]'

# 保存作业模板
temp_submit_button = '//button//span[contains(text(),"保存")]'

# 编辑模板
# edit_temp_i = '//a[contains(text(),"{}")]/../../../..//div[@class="list-operation-extend"]'.format(TEST_UI_JOB_TEMP)
edit_temp_i = '//div[@class="bk-table-fixed-right"]//td//div//i'
edit_temp_button = '//div[@data-test-id="button_editTemplate"]'
# 步骤类型
script_execution = '//div[@title="执行脚本"]'
#confirmation = '//div[@title="人工确认"]'
confirmation = '//div[contains(text(),"人工确认")]'

# 克隆模板
clone_temp_button = '//div[contains(text(),"克隆")]'
# 确认密文
confirm_button = '//button[@name="confirm"]'
# 立即查看模板
check_temp = "//span[text()='立即查看']"
# 删除克隆模板button
delete_clone_temp_button = '//button[@class="delete-btn bk-default bk-button-normal bk-button"]'
confirm_delete_button = '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]'

# 调试模板
debug_button = '//div[@class="bk-table-fixed-right"]//a[@data-test-id="link_debugTemplate"]'
# 执行button
launch_button = '//span[contains(text(),"执行")]'
# 人工确认继续
continue_button = '//span[contains(text(),"确认继续")]'
# 弹窗确定执行
continue_confirm = '//div[@class="confirm-options"]//button'

# 搜索框
search_textarea = '//textarea[@class="input-box"]'
# 搜索结果
search_result = '//div[@class="task-name-box"]'

# 更多(三个点)
more = "//a[contains(.,'TEST_JOB_COMMON')]/../../../../td[6]//i"

# 删除模板
delete_button = '//div[contains(text(),"删除")]'

#关闭窗口
close_windows = '//div[@class="bk-dialog-content bk-dialog-content-drag"]/i'

#去作业模板页面
task_Manage = '//div[@data-test-id="navigation_taskManage"]'
