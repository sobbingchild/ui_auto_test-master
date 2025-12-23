# 点击全部业务
click_business = '[data-test-id="common_select_biz"]'
# 搜索框搜索业务
search_business = '.bk-select-search-input'
# 点击节点管理测试用
plugin_business = '//div/div[2]/div/div/div[2]/ul/li/div/div/span'
business_click = ".select-item"
# 点击搜索框
plugin_select_search = '//div[@class="search-input-input"]'
#搜索框搜索IP
search_host = '//div[@class="search-input-input"]/div[@data-placeholder="搜索IP、「管控区域」、操作系统、Agent状态"]'
# 点击操作系统
click_system = "div.search-menu-wrap > ul > li:nth-child(5) > div"
# 选择系统为windows
select_system_windows = "ul.bk-search-list-menu > li:nth-child(2) > div"
# 选择系统为linux
select_system_linux = "ul.bk-search-list-menu > li:nth-child(1) > div"
# 确认系统
sure_system = "div.bk-search-list-footer > span.footer-btn"
# 勾选全部主机（windwos/linux）
common_checkbox_tableCheckAll = '[data-test-id="common_checkbox_tableCheckAll"]'
#点击安装/更新
plugin_btn_install = '[data-test-id="plugin_btn_install"]'
# 点击批量操作
plugin_btn_operatePlugin = '[data-test-id="plugin_btn_operatePlugin"]'
# 点击插件选择框
plugin_select_pluginName = '[data-test-id="plugin_select_pluginName"]'
# 选择插件
select_plugin_basereport = '//li/div/div[@title="basereport(基础性能采集器)"]'
select_plugin_processbeat = '//li/div/div[@title="processbeat(主机进程信息采集器)"]'
select_plugin_bkunifylogbeat = '//li/div/div[@title="bkunifylogbeat(高性能日志采集)"]'
select_plugin_bkmonitorbeat = '//li/div/div[@title="bkmonitorbeat(蓝鲸监控指标采集器)"]'
select_plugin_exceptionbeat = '//li/div/div[@title="exceptionbeat(系统事件采集器)"]'
select_plugin_bkmonitorproxy = '//li/div/div[@title="bkmonitorproxy(自定义上报服务)"]'
select_plugin_gsecmdline = '//li/div/div[@title="gsecmdline(自定义上报命令行工具)"]'
# 停止插件
plugin_btn_stop = '[data-test-id="plugin_btn_stop"]'
# 启动插件
plugin_btn_start = '[data-test-id="plugin_btn_start"]'
# 选择完插件后进入下一步或立即执行
common_btn_commit = '[data-test-id="common_btn_commit"]'
# 下一步
common_btn_stepNext = '[data-test-id="common_btn_stepNext"]'
# 下一步
step = "div:nth-child(1) > section > div > button:nth-child(1) > div"

##########部署策略##############
#搜索框搜索
search_strategy = '//input[@placeholder="搜索 部署策略、插件名称"]'
# 点击部署策略
strategy = "//div[2]/div[1]/div/div[1]/section/div/div[2]/a[2]"
# 点击去新建策略
addpolicy = "[data-test-id='pluginRule_btn_addPolicy']"
#点击新建策略
go_addpolicy = '//div/form/div[2]/div/ul/li[2]'
# 编辑部署策略
editpolicy = "//section/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/div/button[1]"
#搜索框搜索IP（节点列表）
search_hostip = '//div[@data-placeholder="搜索IP、云区域、操作系统、Agent状态"]'
# 停用部署策略
stoppolicy = "//section/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/div/button[2]"
# 停用策略并停用插件
stopplugin = "[data-test-id='pluginRule_radio_stopPlugin']"
# 删除部署策略
deletepolicy = "//section/div[1]/div[5]/div[2]/table/tbody/tr/td[12]/div/div/button[2]"
# 确定删除部署策略
sure_delete = "//div/div[2]/div/div/div[2]/button[1]"
# 输入策略名称
input_policyname = "[data-test-id='policy_input_policyName'] > div > div > div > input"
# 策略名称
policyname = "linux_basereport"
# 点击自定义输入
custom_input = "[data-test-id='policy_select_ipSelect'] > div > div:nth-child(1) > ul > li:nth-child(3)"
# 输入linux ip
input_ip = ".bk-form-textarea"
# 点击解析
analysis = "button[type='button'] > div"
# 下一步，下一步
next_step = "//form[2]/div[3]/div/button[1]"
next_step_second = "//div[1]/section/div/button[1]"

# 立即执行
execute = "//div[2]/div[3]/div/div/button"
asserttext_stop_success = "停用策略成功"
asserttext_delete = "删除策略成功"

#判断执行成功的元素是否在界面上
execute_successfully_install = '//div[3]/table/tbody//tr/td[8]/div/div/span[2]'

