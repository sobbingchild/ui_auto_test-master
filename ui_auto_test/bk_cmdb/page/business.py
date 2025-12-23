from bk_cmdb import settings

# 点击业务
businessselector = '//div[1]/nav/div/div[1]/div[@data-test-id="businessHostAndService_comp_cmdbBusinessMixSelector"]'
# 搜索业务
select_search_input = '[placeholder="输入关键字搜索"]'
# 根据业务名选择业务
option_name = '//div/div/span[contains(text(),"{}")]'.format(settings.BUSINESS_NAME_CMDB)
# 根据业务名选择业务节点管理
option_name_nodeman = '//div/div/span[contains(text(),"{}")]'.format(settings.BUSINESS_NAME_NODEMAN)
# 根据业务名选择业务蓝鲸
option_name_blue_business = '//div/div/span[contains(text(),"{}")]'.format(settings.BLUE_BUSINESS)
# 点击服务分类
menu_name_service = '[title="服务分类"]'
# 点击服务模板
menu_name_template = '[title="服务模板"]'
# 点击集群模板
menu_name_cluster_template = '[title="集群模板"]'
# 点击主机自动应用
menu_name_host_automatic_application = '//a[@title="主机自动应用"]'
# 点击动态分组
menu_name_dynamic_grouping = '//a[@title="动态分组"]'
# 点击自定义字段
menu_name_custom_field = '//a[@title="自定义字段"]'

# 新增一级服务分类
addmain = '[data-test-id="businessServiceCategory_button_addMain"]'
# 输入一级服务分类名称
placeholder_first = '[placeholder="请输入一级分类"]'
# 一级服务分类名称
first_service = 'Test2'
# 点击一级服务分类
# click_first_service = '[title="Test2"].main-name'
click_first_service="//*[@id='app']/div[1]/div[2]/div/div[1]/div[3]/div[5]/div[1]/div[1]/span/div/div/span[1]"
# 确认一、二级服务分类名称
button_confirm = '[data-test-id="businessServiceCategory_button_confirm"]'
# 添加二级服务分类
addmain_second='//button[@class="add-btn bk-primary bk-button-normal bk-button-text"]/div/span/div/i'
# 输入二级服务分类名称
placeholder_second = '[placeholder="请输入二级分类"]'
# 二级服务分类名称
second_service = 'test1'
# 悬浮一级服务分类
move_first_service = '//div[1]/div[2]/div/div[1]/div[3]/div[5]/div[1]/div[1]/span/div[@class="category-name-text"]'
# 悬浮二级服务分类
move_second_service = '//*[@id="app"]/div[1]/div[2]/div/div[1]/div[3]/div[5]/div[2]/div[1]/div'
# 点击铅笔，修改二级服务分类
edit_second_service = '//div[5]/div[2]/div[1]/div/div/span[1]/button/div/span/i[@class="icon-cc-edit-shape"]'
# 点击×，删除一级服务分类
delete_first_service = '//div[3]/div[5]/div[1]/div[2]/span[2]/button/div/span/i[@class="bk-cmdb-icon icon-cc-del"]'
# 点击×，删除二级服务分类
delete_second_service = '//div[3]/div[5]/div[2]/div[1]/div/div/span[2]/button/div/span/i'
# 确定删除一级服务分类
# sure_delete_firstservice = '/html/body/div[5]/div/div/div/div[4]/div/button[1]'
sure_delete_firstservice ='//div[@class="v-transfer-dom"][2]/div/div/div/div[4]/div/button[1]'
# 确定删除二级服务分类
sure_delete_secondservice = '//div/div[4]/div/button[1]'
###服务模板###
# 点击新建
template_create = '[data-test-id="businessServiceTemplate_button_create"]'
# 模板名称
templatename = '[placeholder="模板名称将作为实例化后的模块名"]'
# 添加属性字段
add_attribute = '//button[@class="bk-default bk-button-normal bk-button"]/div/span'
# 模块类型
# module_type = '//div[3]/dl/div[1]/dd/ul/li[1]/label/span[1]'
module_type = '//div[@class="property-group"]/dd/ul/li[1]/label/span[2]/div'
# 确认添加的字段
sure_add_attribute = '//div[4]/div/button[1]'
# 环境类型
environmental_type = '//div[3]/dl/div/dd/ul/li[2]/label/span[1]'
# 添加服务模板
add_servicetemplate = '//div[1]/div/div[3]/div/div[2]/div/div/div/ul/li/span'
# 第二次添加服务模板
second_add_servicetemplate = '//div[1]/div/div[3]/div/div[2]/div/div/div/ul/li[2]/span'
# 新建进程
process_create = '//div[2]/div/div/span[1]/button[@data-test-id="businessServiceTemplateCreate_button_createProcess"]'
# 进程名称
processname = '[placeholder="请输入进程名称"]'
# 进程别名
bk_process_name = '[placeholder="请输入进程别名"]'
# 进程启动参数
bk_start_param_regex = '[placeholder="请输入进程启动参数"]'
# 备注
description = '[placeholder="请输入备注"]'
# 监听信息里面的立即添加
bk_button_text = '//ul/li/div/div/div/div[3]/div/span/div/button/div/span'
# 新建进程，提交第一个进程信息
template_submit = '/html/body/article/section/div[2]/div/div[2]/div/span/button'
# 点击请输入ip
bk_select_dropdown = '[placeholder="请输入IP"]'
# 点击第一内网
bk_option_name = '[title="第一内网IP"]'
# 输入port
port = '[placeholder="请输入Port"]'
# 点击protocol
protocol = '//ul/li/div/div/div/div[3]/table/tbody/tr/td[3]/div/div/div'
# 点击tcp
tcp = '//div[2]/div/div/div/ul/li[1]/div/div'
# 点击进程管理
process_manage = '//section/div[2]/div/div[1]/div[1]/div[3]/div/div[1]/span[2]'
# 输入工作路径
work_path = '[placeholder="请输入工作路径"]'
# 输入pid文件路径
pid_file = '[placeholder="请输入PID文件路径"]'
# 提交
operationaltemplate_button_submit = '//div[1]/div[2]/div/div[1]/div[2]/div/span/button'
# 编辑模板
edit_template = '//div[2]/table/tbody/tr/td[8]/div/span/span[1]/button/div/span'
# 克隆模板
clone_template = '//div[2]/table/tbody/tr/td[8]/div/span/span[2]/button/div/span'
# 克隆的名称
clone = '_clone'
# 修改模板名称
edit_templatename = '//input[@name="templateName"]'
# 保存修改的模板名称
save_edit_templatename = '//div[1]/div[2]/div/div[1]/div[2]/div/span/button[@type="button"]'
# 确认修改的模板名称
sure_templatename = '//div/div[4]/div/button[1]'
# 搜索模板名称
search_templatename = '[placeholder="请输入模板名称"]'
# 模板名称
test = '测试用'
# 删除进程
delete_process = '[data-test-id="businessServiceTemplateEdit_button_delProcess"]'
# 确认删除模板
sure_delte_process = '//div[@class="v-transfer-dom"]//div[@class="bk-dialog-wrapper"]/div/div/div[4]/div/button[@class="bk-primary bk-button-normal bk-button"]/div/span'
# 删除模板
delete_template = '//div[2]/table/tbody/tr[1]/td[8]/div/span/span[3]/button/div/span'
# 确认删除模板
sure_delete_template = '//div[4]/div/button[1]'
# 在快速搜索中搜索
filterfastsearch = '[placeholder="请输入IP或固资编号"]'
# 勾选主机
checkbox_host = '//section[1]/div/div[2]/div[4]/div[1]/table/thead/tr/th[1]/div/div'
second_checkbox_host = '//table/thead/tr/th[1]/div/div/label/span'
# 转移至
transfer = '//button[@data-test-id="businessHostAndService_button_transfer"]'
# 业务模块
transferbusiness = '//li[@data-test-id="businessHostAndService_li_transferBusiness"]'
# 空闲机池
spare_module = '//li[@data-test-id="businessHostAndService_li_transferIdle"]'
# 主机池
host_pool = '//li[@data-test-id="businessHostAndService_li_transferResource"]'
# 其他业务
other_business = '//li[@data-test-id="businessHostAndService_li_transferAcrossBusiness"]'
# 归还至目录
return_host = '//div[2]/div/div[1]/div/div/div[@tabindex="-1"]'
# 空闲机
idle_machine = '//div/div[1]/div[1]/div[1]/div[2]/div[3]'
# 点击集群
node_content = '//div/div[2]/div[2]/div[2]/span'
# 点击模块
bk_big_tree_node = '//html/body/div[6]/div/div[1]/div[2]/div/div[1]/div[1]/div[1]/div[2]/div[3]'
# 点击下一步
next_step = '//body/div[6]/div/div[1]/div[2]/div/div[2]/span/button/div/span'
second_next_step = '//div[1]/div[2]/div/div[2]/span/button/div/span'
# 展开服务实例1
click_service_instance = '//div[1]/div[3]/div[1]/section/div[3]/div'
# 确认转移
sure_transfer = '//div/div[1]/div[1]/div[4]/button[1]/div'
# 点击集群UI
click_cluster = '[title="Ui_Cluster"]'
# 点击模块UI
click_module = '[title="Ui_Module"]'
# 节点信息
node_information = '//div/div[1]/div[2]/div/div[1]/div[2]/ul/li[3]/div'
# 编辑集群
edit_cluster = '//span[1]/button[@data-test-id="businessHostAndService_button_edit"]'
# 编辑模块
edit_module = '//span[1]/button[@data-test-id="businessHostAndService_button_edit"]'
# 删除模块
delete_module = '//span[2]/button[@data-test-id="businessHostAndService_button_del"]'
# 确认删除模块
sure_confirm = '//button[@name="confirm"]/div/span'
# 集群描述
cluster_description = '//input[@placeholder="请输入集群描述"]'
# 模块类型
click_module_type = '//div[@title="普通"]'
# 数据库
click_db = '//div[@title="数据库"]'
# 保存编辑的信息
save_edit_cluster = '//button[@class="button-save bk-primary bk-button-normal bk-button"]'
# 备注
comment = '//li[10]/span[3]'
# 点击铅笔（备注）
click_edit_comment= '//*[@id="property-item-32"]/span[3]/button/div/span/i'
# 备注信息
comment_message = '//textarea[@placeholder="请输入备注"]'
# 点击sla级别
click_sla_level = '//*[@id="property-item-34"]/span[3]/button/div/span/i'
# 勾选sla级别
sure_sla_level = '//*[@id="property-item-34"]/div/i[1]'

# 勾选（主机备注信息）
# sure_edit_comment = '//li[10]/div/i[1]'
sure_edit_comment ='//*[@id="property-item-32"]/div/i[1]'


# 点击服务模板配置
click_service_config = '//div[1]/div[2]/div/div[1]/div/div[1]/div[2]/ul/li[1]'
# 编辑进程
edit_nginx = '//tr[1]/td[5]/div/span[1]/button[@data-test-id="businessServiceTemplateEdit_button_editProcess"]/div/span'
# 编辑进程启动信息
edit_process_start = '[placeholder="请输入进程启动参数"]'
# 输入的进程启动信息
process_message = './test'
# 保存
save = '/html/body/article/section/div[2]/div/div[2]/div/span/button/div'
# 保存、确定、下一步
confirm = '//button[@class="bk-primary bk-button-normal bk-button"]/div/span'


# 新建集群模板
create_cluster_template = '[data-test-id="businessSetTemplate_button_create"]'
# 集群模板名称
cluster_template_name = '测试集群模板'
# 搜索服务模板名称
search_service_template = '[placeholder="请输入模板名称搜索"]'
# 勾选单个服务模板
check_service_template = '//div/div[3]/section/ul/li[1]/i'
second_check_service_template = '//div/div[3]/section/ul/li[2]/i'
# 确定选择的服务模板
sure_service_template = '//div/div[4]/div/div[2]/button[1]'
# 提交集群模板
submit_cluster_template = '[data-test-id="setTemplateConfig_button_submit"]'
# 点击集群模板
click_cluster_template = '//div/div[1]/div[3]/div[3]/table/tbody/tr'
# 编辑集群模板
edit_cluster_template = '//div[3]/table/tbody/tr/td[6]/div/span[1]/button/div/span'
# 关闭窗口
close_window='//div[@class="v-transfer-dom"]/div/div/div/div[2]/div/div/button[@class="bk-default bk-button-normal bk-button"]'
# 关闭窗口（创建服务模板成功时）
close_window_servicetemplate = "//div[@class='v-transfer-dom']/div/div/div/div[2]/div/div/button[@class='btn bk-default bk-button-normal bk-button']"
# 返回列表
return_list='//div[@class="v-transfer-dom"]/div/div/div/div[5]/div/button[@class="bk-default bk-button-normal bk-button"]'

### 主机自动应用
# 立即启用
immediately_to_enable ='//div/div[2]/span/button[@class="bk-primary bk-button-normal bk-button is-outline"]'
# 选择字段
select_field = '//button[@class="bk-default bk-button-normal bk-button"]/div/i'
# SLA级别
sla_level = '//div[2]/ul/li[3]/label/span[1]'
# 点击SLA级别
click_sla = '//div/div/div/div[@class="bk-select-name medium-font"]'
# 选择级别L1
select_sla = '//li[1]/div/div[@title="L1"]'
# 选择级别L2
select_sla_second = '//li[2]/div/div[@class="bk-option-content-default"]'
# 返回列表
return_list_host = '//button[@class="mr10 bk-primary bk-button-normal bk-button"]/div/span'
# 编辑
edit_host_automatic_application = '//div[2]/span[1]/button'
# 关闭自动应用
delete_host_automatic_application= '//div[2]/span[3]/button'
# 不保留当前自动应用策略
click_save_host_automatic_application = '//div[3]/div/label/span[1]'
# 点击按服务模板
click_service_template = '//div[1]/div/label[2]/div[@class="bk-radio-button-text"]'

###动态分组
# 输入动态分组名称
grouping_name = '//input[@placeholder="请输入分组名称"]'
# 继续添加
continue_add = '//i[@class="bk-icon left-icon icon-plus-circle"]'
# 点击sla级别
check_sla_level = '//label[@title="SLA级别"]/span'
#点击内网IP
check_intranet_ip='//label[@title="内网IP"]/span'
# 选择sla级别
select_sla_level = '//div/div[@placeholder="请选择SLA级别"]'
# 选择级别L1
select_level_L1 = '//div/div[@title="L1"]'
# 预览
preview = '//div[2]/table/tbody/tr/td[8]/div/button[@class="mr10 bk-primary bk-button-normal bk-button-text"]'
# 新建
new = '//div[1]/div[2]/div/div[1]/div[2]/span/button'
# 删除
# delete = '//div[5]/div[2]/table/tbody/tr/td[8]/div/span[2]/button'
delete ='//div[@class="bk-table-fixed-right"]/div[2]/table/tbody/tr/td[8]/div/span[2]/button/div/span'
# 点击搜索框
click_grouping_search = '//div[@placeholder="请输入内网IP"]'
# 关闭动态分组窗口
close_dynamic_grouping_window='//div[@class="bk-sideslider-closer"]'

###自定义字段
# 点击主机
click_host_grouping = '//div/div[1]/div[2]/div[1]/div[2]/ul/li[3]/div'
# 点击模块
click_module_field = '//div/div[1]/div[2]/div[1]/div[2]/ul/li[2]/div'
# 新建分组
add_grouping = '//button[@class="add-group-trigger bk-primary bk-button-normal bk-button-text"]'
# 模块 新建分组
add_module_group = '//section/div/div[1]/span[2]/button/div/span'
# 分组名称
group_name = '//input[@name="groupName"]'
# 输入的分组名称
groupname = 'test'
groupname_new = 'demo'
new_price = '888'
#点击业务字段
new_field_name = '//span[@title="测试专用123"]'
#点击编辑
click_edit ='/html/body/article/section/div[2]/div[1]/div[2]/div/button[1]/div/span'

#点击删除字段
new_delete_field = "/html/body/article/section/div[2]/div[1]/div[2]/div/button[2]/div/span"
#确定删除
notarize_delete_field = "/html/body/div[8]/div/div/div/div[4]/div/button[1]/div/span"

#点击分组旁的3个点icon[last()-1]默认定位倒数第一个分组
group_icon = "//section/div/div[2]/div/div[last()-1]/div/div/div[2]/div[1]/div/i"


# 提交
# commit = '/html/body/div[6]/div/div/div/div[3]/div/button[1]'
commit = '//div[@class="bk-dialog-no-padding group-dialog v-transfer-dom"]/div/div/div/div[3]/div/button[1]'
# 新建字段
add_field='//div[@class="field-group model-detail-wrapper has-tips"]/div[1]/span[1]/button'
# 点击字段分组
click_field_group = '/html/body/article/section/div[2]/div[1]/div[1]/div[1]/div[1]/div/div/div/div/div'
# 选择新建的分组
new_group = '//div[@title="demo"]'
new_host_group = '//div[@title="test"]'
# 唯一标识
unique_identification = '//input[@name="fieldId"]'
# 字段名称
field_name = '//input[@name="fieldName"]'
fieldname = '测试专用123'



# 点击新建业务字段
new_business_field = "//section/div/div[2]/div/div[last()-1]/ul/li/div/button/div/span/i"
# 模块新建业务字段
module_new_field ="//section[@class='bk-tab-content']/div/div[1]/span[1]/button/div/span"
# 字段类型
field_type = '/html/body/article/section/div[2]/div[1]/div[1]/div[1]/div[2]/div/div/div/div/div'
# 字段类型选择枚举（多选）
type_enumeration = '//div[@class="tippy-tooltip light-theme bk-select-dropdown-theme"]/div[2]/div/div/div[2]/ul/li[5]/div/div/span'
# 输 入枚举ID
iput_id='[placeholder="请输入ID"]'
# 输入枚举值
input_price='[placeholder="请输入值"]'
# 提交
commit_field = '//section/div[2]/div/div[2]/div/button[1]/div/span'

click_field_backlog = '[title ="测试专用123"]'
# 点击字段
click_field = '[title="测试专用123测试用"]'
# 删除字段
delete_field = '//button[@class="delete-btn bk-default bk-button-normal bk-button"]/div/span'
# 确认删除字段
sure_delete_field ='//div[@class="v-transfer-dom"]/div/div/div/div[4]/div/button[1]'
# 修改名称
user_prompts='[placeholder="请输入字段名称"]'
# 点击更多
more = '//section/div/div[2]/div/div[last()-1]/div/div/div[2]'
# 删除分组，必须加到div[3]，否则无法点击删除分组
delete_grouping = '//div[@class="group-wrapper"]/div/div[last()-1]/div/div/div[2]/div[3]/ul/li[2]/span/div'
# 返回主机
return_grouping = '/html/body/article/section/div[1]/div[1]/i'

# 断言
assert_success = "保存成功"
assert_delete = "删除成功"
assert_create_success = '创建成功'
assert_templatename = '测试用模板'
assert_delete_process = '成功更新模板进程'
first_process = 'unlock'
second_process = 'lock'
first_transfer = '转移成功'
process_start_message = 'test'
synchronization_message = '同步成功'
edit_success = "修改成功"
assert_transfer = '转移成功'
assert_application_successfully = '应用成功'
assert_close_success = '关闭成功'

###准入用例###
# 悬浮至业务名
business_title = "//span[@title='配置平台自动化测试']"
# 新建集群
# creat_cluster = '//button[@data-test-id="businessHostAndService_button_createNode"]/div/span'
creat_cluster = '//button[@class="node-button bk-primary bk-button-normal bk-button"]/div/span'
# 点击直接新建
new_direct = '//div/div[2]/div[1]/label[2]/div'
# 输入集群名
cluster_name = '[placeholder="请输入集群名称，需批量创建多个可使用换行分隔"]'
cluster_name_text = "Ui_Cluster"
# 提交新建的集群
# commit_cluster = 'button[data-test-id="businessHostAndService_button_createSetSave"] > div > span'
commit_cluster='//button[@class="mr10 bk-primary bk-button-normal bk-button"]/div/span'
# 断言
asserttext = "新建成功"
# 立即新建
# immediately_the_new = '//section[1]/div[1]/div[2]/span/span/button/div/span'
# #定位新建按钮
immediately_the_new = '//div[@class="bk-big-tree-node clearfix is-leaf is-expand is-selected"]/div[2]/div/div/span[1]/button/div/span'
# 点击直接新建
new_direct_second = '//div/div[2]/div[1]/div[2]/input'
# 输入模块名
module_name = '[placeholder="请输入模块名称"]'
module_name_text = "Ui_Module"
# 提交新建的模块
commit_module = 'button[data-test-id="businessHostAndService_button_createModuleSave"] > div >span'
# 快速搜索框搜索IP
fast_search = '//div[@data-test-id="businessHostAndService_comp_filterFastSearch"]/div[@class="bk-input-text"]/input[@type="text"]'
# 勾选主机
checkbox_blue_whale_host = '//th/div/div/label[@class="bk-form-checkbox"]/span'
# 搜索框搜索空闲机池
search_idle_pool = '//input[@type="text"][@placeholder="输入关键字搜索"]'
# 点击空闲机
click_idle_pool = '//span[@title="空闲机"]'
# 确定转移主机至空闲机池
sure_transfer_idle_pool = '/html/body/div[6]/div/div[1]/div[2]/div/div[2]/button[1]/div/span'
# 点击Paas平台
pass_platform = '//span[@title="PaaS平台"]'
# 点击apigw模块
apigw = '//span[@title="apigw"]'
# 点击公共组件
common_components = '//span[@title="公共组件"]'
# 获取IP
get_host = '//tr[1]/td[3]/div/span'
# 第二次获取IP
get_host_second = '//tr[2]/td[3]/div/span'
# 点击主机
click_host = '//div[4]/div[2]/table/tbody/tr/td[2]/div/span'
