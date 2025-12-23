# -*- coding: utf-8 -*-
# @Time : 2021/8/20 15:41
# @File : file_transfer.py
# @Project : bk_job
FILE_PATH = '/var/log/gse/agent-err.log'
DST_PATH = '/tmp/'
centos_1 = ''
centos_2 = ''

# 文件分发页面入口
file_transfer = '//div[@data-test-id="navigation_fastPushFile"]'

# 本地文件分发页面title
local_file_button = '//button//span[contains(text(),"添加本地文件")]'
# 服务器文件
server_file_button = '//button//span[contains(text(),"添加服务器文件")]'


# 文件路径
file_path = '//div[@class="job-smart-input-area"]'
# file_path = '//div[@class="job-form push-file-form"]/form/div[3]/div[2]/div[1]/div/div/div/div/div/input'

# 添加服务器
add_host = '//div[@class="server-add-only-host-btn"]'

# 搜索主机
search_host = '//div[@class="input-text-area"]'
# 选择主机
choice_host = '//div[@class="choose-ip-host-table"]//label'
#选择主机
select_host = '//div[@class="talbe-content not-empty"]/table/tbody/tr[3]/td[1]/span/label/span'
select_host_ip = '//div[@class="talbe-content not-empty"]/table/tbody/tr[3]/td[2]/div/span/span[1]'

# 确定主机
confirm_button = '//span[contains(text(),"确定")]'
# 保存表单按钮
save_button = '//span[contains(text(),"保存")]'
# 分发路径
dst_path = '//input[@placeholder="请填写分发路径"]'
# 下拉页面js
js_script = "document.querySelectorAll('.scroll-faker-content')[1].scrollTop=300"
# 执行按钮
execute_button = '//div[@role="action"]//span[contains(text(),"执行")]'

#添加服务器
# execute_target = '//div[@class="task-step-execute-target only-host"]/div/div/div/div/button[1]'
execute_target = '//*[@type="button"]//span[normalize-space(text())="添加服务器"]'
#服务器搜索
host_search = '//div[@class="mult-input host-search"]/div[1]'
#服务器搜索类型
host_search_input = 'linux'
filter_agent = '//div[@class="server-panel-dropdown-menu"]/I'
select_normal_agent = '//div[@class="tippy-popper"]/div/div/div/div/div[3]'
#选择筛选出来的第一台机器
select_first_agent = '//span[contains(text(),"结果预览")]/../../../../../../../div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[1]/span'
first_agent_ip = '//span[contains(text(),"结果预览")]/../../../../../../../div[2]/div/div/div[1]/div[2]/div/div[1]/div/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td[2]/div/span/span[1]'
#确定选择服务器
confirm_agent = '//span[contains(text(),"结果预览")]/../../../../../../../div[3]/div/span/button'


# 执行按钮
button_excute_script = '//div[@role="action"]//span[contains(text(),"执行")]'
# button_excute_script = '//div[@class="smart"]/div/button[1]/div'
# 执行状态
status_excute = "//div[@class='status']/span[2]"
# 执行成功
excute_suss = "执行成功"
# 执行失败
excute_fail = "执行失败"
# 页面异常
excute_exception = "页面异常"

# 切换脚本引用按钮
script_reference = '//div[text()="脚本引用"]'
# 点击选择引用脚本
script_select = '//div[@data-placeholder="选择引用脚本"]'


# 选择引用脚本
def choice_script(script_name):
    script = '//div[contains(text(),"{}")]'.format(script_name)
    return script

scroll_bar = "//div[@class='scroll-faker']/div[@class='scrollbar-vertical']/div[@class='scrollbar-inner']"