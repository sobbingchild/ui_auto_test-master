# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     quick_excute_scripts.py
   Description : 
   Author :       v_adanchen
   date：          2021/7/23
-------------------------------------------------
快速脚本执行中各种脚本以后都在这个文件中添加
"""
#选择业务
job_app_select = '//div[@class="job-app-select"]/div/input'
#搜索业务
app_search = '//div[@class="app-search"]/input'
#业务名称
app_name = '蓝鲸'
#业务选择第一条
app_search_select = '//div[@class="app-panel"]/div[2]/div[1]'

#添加服务器
# execute_target = '//button[@class="mr10 bk-default bk-button-normal bk-button"]/div/span/i'
# execute_target = '//div[@class="task-step-execute-target only-host"]/div/div/div/div/button[1]'
execute_target = '//*[@type="button"]//span[normalize-space(text())="添加服务器"]'
#服务器搜索
host_search = '//div[@class="mult-input host-search"]/div[1]'
#服务器搜索类型
host_search_input = 'linux'
filter_agent = '//div[@class="server-panel-dropdown-menu"]/I'
select_normal_agent = '//div[@class="tippy-popper"]/div/div/div/div/div[3]'
#选择筛选出来的第一台机器
select_first_agent = '//div[@class="talbe-content not-empty"]/table/tbody/tr[1]/td[1]/span/label/span'
first_agent_ip = '//div[@class="talbe-content not-empty"]/table/tbody/tr[1]/td[2]/div/span/span[1]'
#确定选择服务器
confirm_agent = '//div[@class="bk-dialog-footer"]/div/span/button[1]/div'


# 侧边导航栏，快速执行脚本
navigation_quick_script_excute = "//div[@data-test-id='navigation_fastExecuteScript']"
# 快速执行脚本，脚本名称
name_quick_script = "//div[@class='jb-input form-item-content']//div[@class='bk-input-text']/input"
# 快速脚本执行，脚本内容输入框，默认shell
input_script_content = "//textarea[@class='ace_text-input']"
# 选择账户
select_account = "//div[@class='bk-form-content']//div[@class='form-item-content']//div[@class='bk-select-name']"
# 选择root
select_root = "//ul/li/div[contains(.,'root')]"
# 滚动条
scroll_bar = "//div[@class='scroll-faker']//div[@class='scrollbar-vertical']//div[@class='scrollbar-inner']"

# 添加服务器按钮
button_add_ip = "//div[@class='jb-form-item-content']//button//span"


# 选择服务器
checkbox_choose_ip = "//div[@class='host-list']//div[@class='choose-ip-host-table']//th[1]//span"
# 确定添加服务器按钮
button_confirm_ip = "//div[@class='bk-dialog-footer']//button[1]"
######################################
# 动态拓扑
button_dynamic_top = "//div[@class='choose-ip-container']//div[@class='tab-container']/div[2]"
# 动态拓扑-选择业务
select_bussiss = "//div[@class='bk-big-tree']/div[1]/div/span[@class='node-checkbox']"
#确定添加动态拓扑
confirm_ip_dy="//div[@class='bk-dialog-footer']//span[contains(.,'确定')]"
########################################
#动态分组
button_dynamic_package="//div[@class='choose-ip-container']//div[@class='tab-container']/div[3]"
#动态分组-选择机器
select_dy_package="//tr/th/div[@class='head-cell']/label/span[@class='bk-checkbox']"
#添加动态分组
confirm_ip_package="//div[@class='bk-dialog-footer']/button//span[contains(.,'确定')]"
##########################################
#手动输入
button_manmul_input = "//div[@class='choose-ip-container']//div[@class='tab-container']/div[4]"
#输入框
input_ip="//div[@class='bk-textarea-wrapper']/textarea"
#添加
add_ip="//div[@class='input-action']/button"
#确定添加
confirm_ip_input="//div[@class='bk-dialog-footer']/button//span[contains(.,'确定')]"
#######################################

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
excute_exception = "正在执行中"
# bat
# perl
# python
select_python = "//div[@class='jb-ace-title']/div[contains(.,'Python')]"
# powershell
# sql

# 切换脚本引用按钮
script_reference = '//div[text()="脚本引用"]'
# 点击选择引用脚本
script_select = '//div[@data-placeholder="选择引用脚本"]'


# 选择引用脚本
def choice_script(script_name):
    script = '//div[contains(text(),"{}")]'.format(script_name)
    return script
