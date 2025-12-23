# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_service.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/25
-------------------------------------------------
"""
import settings

# 前提条件：
# 人员：admin,adan,user1,user2,user3,user4
# 用户组中配置测试人员为：adan
# 触发器：创建单据，挂起单据，恢复单据，
#       进入节点（API节点），离开节点（sops节点），分派单据（节点4），认领单据（节点3），转单（节点1），
#       进入分支（进入会签节点前配置）
#       创建任务之后，删除任务，执行任务之前，执行任务之后，完成任务之后

# 任务模板：新建一个任务模板

# 节点1：处理场景：先派单，后处理；派单人：提单人上级 （所有上级都提前设置为了admin）,处理人：提单人；转单人：通用角色列表-测试，触发器：转单；添加字段到表格
# API节点：处理人-个人-user1,触发器：进入节点
# 标准运维节点：提前准备标准运维公共流程，触发器：离开节点
# 节点2：没啥覆盖点，处理场景：直接处理
# 会签节点：多人依次会签：user2,user3,user4,处理人数大于3
# 节点3：处理场景：先认领，后处理；处理人：组织架构-UI测试用；从单选下拉框添加字段到多选人员选择，触发器：认领单据
# 审批节点：审批方式：或签；处理人：引用变量-单选人员选择；触发器：新建
# 节点4：处理场景：先派单，后认领；触发器：分派单据，包含字段：富文本，自定义表格，树形选择，链接，自定义表单，触发器：挂起单据，恢复单据
# 服务设置：撤回方式：任何节点，提单人都可撤回；高级配置：触发器：创建单据；任务配置：选择内置好的模板，可创建任务节点和可处理节点都选最近的节点


project = "//a[@data-test-id='navigation-router-navRouter-project']"
# 取第一个
nav_service = "//a[@data-test-id='navigation-menu-projectServiceList']"
add_service = "//button[@data-test-id='service_button_createService']"
service_name = "//div[@data-test-id='service-input-serviceName']//input"
service_dir = "//div[@data-test-id='service-select-serviceDirectory']//div[@class='bk-search-tree-wrapper']"
choose_service_dir = "//div[@class='bk-search-tree-content']/ul/li[4]"
service_type = "//div[@data-test-id='service-select-serviceType']//div[@class='bk-tooltip bk-select-dropdown']"
choose_service_type = "//div[@class='bk-options-wrapper']/ul/li[1]"
service_comfirm = '//div[@class="footer-wrapper"]/button[1]'
service_temp = '//div[@class="service-template"]/div[1]'
choose_service_temp = "//ul[@class='template-list']/li/p[contains(.,'默认')]"
service_next = "//button[@data-test-id='service_button_nextStepAndSave']"
# 流程设计中线条的默认按钮
line_default = "//div[@data-test-id='service_jsflow_serviceProcess']//div[@style='position: absolute; transform: translate(-50%, -50%); left: 526px; top: 169.5px;']"

#服务更多-悬停
service_more = '//span[@title="fdsafdsa"]/../../../../../td[12]/div/div'


del_line_default = "//div[@class='mt20']/button[3]"
# 提单节点
node_comit_ticket = "//div[@class='common-node']/span[2]"
# 添加节点1的面板，index=1
panel_comit_ticket = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate0']"

#######################################################
# 节点1

new_node1 = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='新增节点']"

node1_name = "//div[@data-test-id='basicInfo-input-nodeName']//input"

node1_scenes = "//div[@data-test-id='basicInfo-select-ProcessingScenarios']//div[@class='bk-tooltip bk-select-dropdown']"

node1_scenes_choose = "//div[@class='bk-option-content']/div[@title='先派单，后处理']"
# 派单人，index=0
node1_dispatch = "//div[@class='first-level']/div[@data-test-id='dealPerson-select-firstHandler']"
# 选择提单人上级
node1_dispatch_choose = "//ul[@class='bk-options bk-options-single']/li//div[@title='提单人上级']"

node1_handler = "//div[@data-test-id='basicInfo-component-processor']//div[@data-test-id='dealPerson-select-firstHandler']"

node1_handler_choose = "//ul/li//div[@title='提单人']"
# 是否可转单
node1_is_transfer = "//div[@data-test-id='basicInfo-radio-canDeliver']//label[1]/div[@class='bk-radio-text']"

# 选择通用角色列表-测试
node1_transfer_click = "//div[@data-test-id='basicInfo-radio-delivers']//div[@data-test-id='dealPerson-select-firstHandler']//div[@class='bk-tooltip-ref']"

node1_transfer_choose = "//ul/li[@data-test-id='dealPerson-select-first-GENERAL']"

node1_transfer_click2 = "//div[@data-test-id='dealPerson-select-secondHandler']"

node1_transfer_choose2 = '//*[@class="bk-options"]/li[2]'

# 添加字段

node1_add_field = "//button[@data-test-id='fieldConfig-button-addField']"

node1_field_name = "//div[@data-test-id='field-input-fieldName']//input"
node1_field_type = "//div[@data-test-id='field-select-fieldType']//div[@title='单行文本']"
node1_search_type = "//div[@class='bk-select-dropdown-content']/div/input"


def choose_field_type(field_type):
    choose_field_type = "//div[@class='bk-select-dropdown-content']//ul/li/div/div[@title='{}']".format(field_type)
    return choose_field_type


node1_commit_field = "//button[@data-test-id='field_button_submit']"

# 高级设置

node1_high_setting = "//div[@data-test-id='trigger-div-showMoreConfig']"

node1_add_trigger = "//ul[@class='bk-trigger-content']//div[@class='bk-dropdown-trigger']"

node1_pub_trigger = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node1_pub_trigger_choose = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node1_choose_trigger = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(settings.TRIGGER_INTO_NODES)

node1_pub_trigger_comfirm = '//*[@class="bk-form-checkbox checkbox"]/../button[1]'

# 完成节点1 提交
node1_comfirm = "//button[@data-test-id='basicNode-button-submit']"

# 右击节点1弹出的面板
panel_node1 = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='{}']".format(settings.TEST_NODE1)
# 选择并行网关，index取0
parallel_gateway_choose = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/..//li[@data-test-id='nodeTemplate-li-addNodeTemplate7']"
# 右击平行网关的面板
panel_parallel = "//div[@class='bk-flow-location']/div[@class='common-branch']/i[@class='bk-itsm-icon icon-flow-convergence']"

# 选择API节点

node_li_api = "//div[@class='common-branch']/..//li[@data-test-id='nodeTemplate-li-addNodeTemplate1']"

node_li_sops = "//div[@class='common-branch']/..//li[@data-test-id='nodeTemplate-li-addNodeTemplate2']"

# 点击API节点
node_api = "//div[@data-test-id='nodeTemplate-common-node-2-TASK']"

node_api_name = "//div[@data-test-id='autoNode-input-nodeName']//input"
# index=0,index=1
node_api_interface = "//div[@data-test-id='autoNode-select-apiInterface']//div[@class='bk-tooltip bk-select-dropdown']"

node_api_interface2 = "//div[@class='bk-form-content']/div[@data-placeholder='请选择']"

node_api_interface_choose = "//div[@class='bk-select-dropdown-content']//ul/li[1]"

node_api_interface_choose2 = "//div[@class='bk-select-dropdown-content']//ul/li[2]"

node_api_handler = "//div[@data-test-id='dealPerson-select-firstHandler']"

node_api_handler_choose = "//div[@class='bk-options-wrapper']/ul/li[2]"
node_api_handler2 = "//div[@data-test-id='dealPerson-select-personSecondHandler']//div[@data-placeholder='请选择']"
# 输入user1
node_api_handler_input = "//div[@data-test-id='dealPerson-select-personSecondHandler']/div[@class='user-selector ui-user-selector']//div/span"

node_api_comfirm = "//button[@data-test-id='autoNode-button-submit']"

# 标准运维节点设置

# 点击标准运维节点
node_sops = "//div[@data-test-id='nodeTemplate-common-node-3-TASK-SOPS']"

node_sops_name = "//div[@data-test-id='sopsNode-select-nodeName']//input"

node_sops_type = "//div[@data-test-id='sopsNode-select-processType']/div"
node_sops_type_choose = "//div[@class='bk-select-dropdown-content']//ul/li[2]"

node_sops_bz = "//div[@data-test-id='sopsNode-select-business']//div[@class='bk-tooltip bk-select-dropdown']"

node_sops_bz_choose = "//div[@class='bk-options-wrapper']/ul/li//div[@title='锦华测试专用']"

node_sops_temp = "//div[@data-test-id='sopsNode-select-processTemplate']//div[@class='bk-tooltip bk-select-dropdown']"

node_sops_temp_choose = "//ul/li//div[@title='test_sops_node_flow']"

# 高级设置

node_sops_high_setting = "//div[@data-test-id='trigger-div-showMoreConfig']"

node_sops_add_trigger = "//ul[@class='bk-trigger-content']//div[@class='bk-dropdown-trigger']"

node_sops_pub_trigger = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node_sops_choose_trigger = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(settings.TRIGGER_OUT_NODES)

node_sops_pub_trigger_comfirm = "//div[@class='bk-dialog-footer']/div/button[1]"

node_sops_comfirm = "//button[@data-test-id='sopsNode-button-submit']"

# 汇聚网关,右击标准运维

panel_sops = "//div[@data-test-id='nodeTemplate-common-node-3-TASK-SOPS']"

convergence_gateway_choose = "//div[@data-test-id='nodeTemplate-common-node-3-TASK-SOPS']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate5']"
# 右击汇聚网关
panel_convergence_gateway = "//div[@class='bk-flow-location']/div[@class='common-branch']/i[@class='bk-itsm-icon icon-flow-branch']"
########################################
# index 取第二个
node2_choose = "//div[@class='common-branch']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate0']"

node2_click = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='新增节点']"

# 缩小画布
canvas_tools_reduc = "//div[@data-test-id='service_jsflow_serviceProcess']//div[@class='tool-panel']/div[2]"

# 节点2信息配置
node2_name = "//div[@data-test-id='basicInfo-input-nodeName']//input"

node2_handler = "//div[@data-test-id='dealPerson-select-firstHandler']"

node2_handler_choose = "//ul/li//div[@title='提单人']"

# 完成节点2 提交
node2_comfirm = "//button[@data-test-id='basicNode-button-submit']"

#分支判断

node2_default="//div[@style='position: absolute; transform: translate(-50%, -50%); left: 1441.5px; top: 199px;']/span"

node2_branch_name="//div[@data-test-id='lineConfig-select-relation']//input"

node2_branch_condi="//div[@data-test-id='lineConfig-select-condition']//div[@data-placeholder='请选择']/div"

node2_branch_condi_choose="//div[@class='bk-options-wrapper']/ul/li[2]"

node2_branch_condi_1="//div[@data-test-id='lineConfig-select-fieldList']//div[@data-placeholder='请选择']"

node2_branch_condi_1_choose="//ul[@class='bk-options bk-options-single']/li//span[contains(.,'数字')]"

node2_branch_condi_2="//div[@data-test-id='lineConfig-select-betweenList']//div[@data-placeholder='请选择']"


node2_branch_condi_2_choose="//div[@class='bk-options-wrapper']/ul/li//div[@title='等于']"

node2_branch_condi_3="//div[@data-test-id='lineConfig-select-choiceList']//input"

node2_branch_condi_comfirm="//button[@data-test-id='lineConfig-button-submit']"
#用index区分
node2_default2="//span[contains(.,'默认')]"
##分支触发器
node2_branch_trigger="//ul[@class='bk-trigger-content']//i[@class='bk-icon icon-plus']"

node2_branch_pub_trigger="//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node2_branch_triger_choose="//ul[@class='bk-trigger-content']/li/span[@title='test_ui_into_branch']"

node2_branch_triger_confirm="//button[@data-test-id='common-trigger-confirm']"



# 会签节点信息
# 会签节点：多人依次会签：user2,user3,user4,处理人数大于3

node_countersign_choose = "//div[@class='common-branch']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate3']"

node_countersign_click = "//div[@data-test-id='nodeTemplate-common-node-5-SIGN']/span[@title='新增节点']"

node_countersign_name = "//div[@data-test-id='signNode-input-name']//input"
# 多人依次会签
node_countersign_method = "//form[@class='bk-form']/div[@class='bk-form-item is-required']//label[2]"

node_countersign_handler = "//div[@data-test-id='signNode-radio-processors ']//div[@class='user-selector-layout']/div"

node_countersign_handler1="//div[@data-test-id='signNode-radio-processors ']//div[@class='user-selector-layout']/div/span"

node_countersign_handler2 = "//div[@data-test-id='signNode-radio-processors ']//div[@class='user-selector-layout']/div/span[2]"

node_countersign_handler3 = "//div[@data-test-id='signNode-radio-processors ']//div[@class='user-selector-layout']/div/span[3]"

node_countersign_number = "//div[@data-test-id='signNode-input-conditionValue']//input"

node_countersign_comfirm = "//button[@data-test-id='signNode-button-submit']"

# 右击会签节点panel_node_countersign=""
####################################

panel_node_countersign = "//div[@data-test-id='nodeTemplate-common-node-5-SIGN']"

node3_choose = "//div[@data-test-id='nodeTemplate-common-node-5-SIGN']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate0']"

node3_click = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='新增节点']"

test_ui_node3="//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='test_ui_node3']"
#取消按钮
node3_cancel="//div[@class='bk-node-btn mt20']/button[2]"

# 节点3信息配置
# 节点3：处理场景：先认领，后处理；处理人：组织架构-UI测试用；从单选下拉框添加字段到多选人员选择，触发器：认领单据
node3_name = "//div[@data-test-id='basicInfo-input-nodeName']//input"

node3_scenes = "//div[@data-test-id='basicInfo-select-ProcessingScenarios']//div[@title='直接处理']"

node3_scenes_choose = "//div[@class='bk-options-wrapper']//ul/li[3]"

node3_handler = "//div[@data-test-id='dealPerson-select-firstHandler']"

node3_handler_choose = "//div[@class='bk-options-wrapper']/ul/li//div[@title='组织架构']"

node3_handler2 = "//div[@class='second-level']//div[@class='bk-search-tree-wrapper']"

node3_handler_choose2 = "//div[@class='tree-node set-frist-pLeft']/span[@title='UI测试用']"

# 添加字段，复用节点1的定位
# 自定义表格
node3_field_custom_table = "//div[@class='bk-custom-line']//div[@class='bk-input-text']/input"
# index=0,index=1
node3_source_data = "//div[@class='bk-data-source']//div[@class='bk-select-name']"

node3_source_data_choose1 = "//ul[@class='bk-options bk-options-single']/li[1]"

node3_source_data_choose2 = "//ul[@class='bk-options bk-options-single']/li[1]"
# 单选，多选，复选，checkbox,radio等，index=0,index=1
node3_field_multi_field = "//section//form//div[@class='bk-data-content']//input"

# 高级设置

node3_high_setting = "//div[@data-test-id='trigger-div-showMoreConfig']"

node3_add_trigger = "//ul[@class='bk-trigger-content']//div[@class='bk-dropdown-trigger']"

node3_pub_trigger = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node3_pub_trigger_choose = "//div[@class='trigger-dialog-box']/ul/li/span[@title='{}']".format(settings.TRIGGER_CLAIM_TICKETS)

node3_pub_trigger_comfirm = "//div[@class='bk-dialog-footer']/div/button[1]"

# 完成节点3 提交
node3_comfirm = "//button[@data-test-id='basicNode-button-submit']"

# 审批节点

node3_panel = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='{}']".format(settings.TEST_NODE3)

node_approve_choose = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate4']"

node_approve_click = "//div[@data-test-id='nodeTemplate-common-node-4-APPROVAL']/span[@title='新增节点']"

node_approve_name = "//div[@data-test-id='approveNode-input-nodeName']//input"

node_approve_handler = "//div[@data-test-id='dealPerson-select-firstHandler']"

node_approve_handler_choose = "//ul/li//div[@title='引用变量']"

node_approve_handler2 = "//div[@class='second-level']//div[@class='bk-tooltip bk-select-dropdown']"

node_approve_handler_choose2 = "//div[@class='bk-options-wrapper']/ul/li[2]"

node_approve_comfirm = "//button[@data-test-id='approve-button-submit']"

# 高级设置

node_approve_high_setting = "//div[@data-test-id='trigger-div-showMoreConfig']//span"

node_approve_add_trigger = "//ul[@class='bk-trigger-content']//div[@class='bk-dropdown-trigger']"

node_approve_new_trigger = "//a[@data-test-id='taskTemplate-li-addTrigger']"

node_approve_newtriger_name = "//div[@data-test-id='trigger-input-name']//input"

node_approve_newtriger_event = "//div[@data-test-id='triggers_select_choiceEvent']"

# 选择进入节点
choose_triger_event_inotes = "//ul[@class='bk-group-options']/li[1]"
# 点击动作名称
event_name = "//div[@data-test-id='trigger-div-triggerRules']//div[@class='bk-response-way']/div"
# 选择API执行
choose_event_name = "//div[@class='bk-select-dropdown-content']//ul/li[1]"
# 选择API ID,定位到两个，1级和2级分别取第一个和第二个
event_id = "//span[contains(.,'API接口ID')]/../../div[@class='bk-form-content']/div"
# 选择配置平台
choose_event_id = "//div[@class='bk-select-dropdown-content']/div/ul/li[1]"

#选择查询业务

choose_event_id2="//ul/li/div/div[@title='查询业务']"

node_approve_new_trigger_comfirm = "//button[@data-test-id='trigger_button_submitTrigger'][1]"

# 节点4

panel_approve = "//div[@data-test-id='nodeTemplate-common-node-4-APPROVAL']"

node_4 = "//div[@data-test-id='nodeTemplate-common-node-4-APPROVAL']/..//ul/li[@data-test-id='nodeTemplate-li-addNodeTemplate0']"

node4_click = "//div[@data-test-id='nodeTemplate-common-node-0-NORMAL']/span[@title='新增节点']"

node4_name = "//div[@data-test-id='basicInfo-input-nodeName']//input"

node4_scenes = "//div[@data-test-id='basicInfo-select-ProcessingScenarios']//div[@title='直接处理']"

node4_scenes_choose = "//div[@class='bk-options-wrapper']//ul/li[4]"
# 取index=0,index=1
node4_dispatch = "//div[@data-test-id='dealPerson-select-firstHandler']"

# 选择提单人
node4_dispatch_choose = "//div[@class='bk-options-wrapper']/ul/li//div[@title='提单人']"

node4_handler = "//div[@data-test-id='dealPerson-select-firstHandler']"

node4_handler_choose = "//li[@data-test-id='dealPerson-select-first-STARTER']"

# 调用 添加字段的case  test_07_add_field2.py

# 高级设置-派单触发器,挂起，恢复

node4_high_setting = "//div[@data-test-id='trigger-div-showMoreConfig']"

node4_add_trigger = "//ul[@class='bk-trigger-content']//div[@class='bk-dropdown-trigger']"

node4_pub_trigger = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

node4_choose_triggerd = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(settings.TRIGGER_DISTRIBUTION)

node4_choose_trigger_hang = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(settings.TRIGGER_HANG)

node4_choose_trigger_recover = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(settings.TRIGGER_RECOVER)

node4_pub_trigger_comfirm = "//div[@class='bk-dialog-footer']/div/button[1]"

node4_comfirm = "//button[@data-test-id='basicNode-button-submit']"

flow_next = "//button[@data-test-id='service_button_nextStepAndSave']"

flow_high_settings = "//div[@data-test-id='editService-div-showMoreConfig']"

flow_add_trigger = "//ul[@class='bk-trigger-content']//i[@class='bk-icon icon-plus']"

flow_pub_trigger = "//a[@data-test-id='taskTemplate-li-quoteCommonTrigger']"

flow_trigger_confirm = "//div[@class='trigger-dialog-footer']/button[1]"

flow_pub_create = "//ul[@class='bk-trigger-content']//span[@title='test_ui_create_ticket']"

flow_temp_on = "//div[@data-test-id='taskConfig-switcher-isUse']"

flow_temp = "//div[@data-test-id='taskConfig-select-taskTemplate']//div[@class='bk-select-name']"

flow_temp_choose = "//div[@class='bk-option-content']/div[@title='test_tickets_task_name']"

flow_create_node = "//div[@data-test-id='taskConfig-select-createdTaskNode']//div[@class='bk-select-name']"

flow_create_node_choose = "//ul/li[1]//span[contains(.,'{}')]".format(settings.TEST_NODE1)

flow_deal_node = "//div[@data-test-id='taskConfig-select-processTaskNode']//div[@class='bk-select-name']"

flow_deal_choose = "//ul/li[1]//span[contains(.,'{}')]".format(settings.TEST_NODE2)

flow_commit = "//button[@data-test-id='service_button_nextStepAndSave']"

# 节点4：处理场景：先派单，后认领；触发器：分派单据，包含字段：富文本，自定义表格，树形选择，链接，自定义表单，触发器：挂起单据，恢复单据
# 服务设置：撤回方式：任何节点，提单人都可撤回；高级配置：触发器：创建单据；任务配置：选择内置好的模板，可创建任务节点和可处理节点都选最近的节点

dot_create = "//div[@style='position: absolute; height: 16px; width: 16px; left: 427px; top: 162px;']"
dot_node1_right = "//div[@style='position: absolute; height: 16px; width: 16px; left: 737px; top: 162px;']"

dot_api_right = "//div[@style='position: absolute; height: 16px; width: 16px; left: 1257px; top: 162px;']"
# dot_sops_right = "//div[@style='position: absolute; height: 16px; width: 16px; left: 1257px; top: 242px;']"
# 汇聚网关点
dot_converge_top = "//div[@style='position: absolute; height: 16px; width: 16px; left: 1337px; top: 222px;']"

dot_node2_right = "//div[@style='position: absolute; height: 16px; width: 16px; left: 1677px; top: 242px;']"

dot_node3_top = "//div[@style='position: absolute; height: 16px; width: 16px; left: 1812px; top: 302px;']"

dot_node4_right = "//div[@style='position: absolute; height: 16px; width: 16px; left: 2407px; top: 322px;']"
dot_end = "//div[@data-test-id='endNode']"

# 字段定义，类型一
field_single_line = '单行文本'
field_multi_line = '多行文本'
field_add_number = "数字"
field_add_radio_person = "单选人员选择"
field_add_multiple_person = "多选人员选择"
field_add_link = "链接"
field_add_date = "日期"
field_add_time = "时间"

# 字段定义，类型二
field_single_drop_box = "单选下拉框"
field_enter_single_drop_box = "可输入单选下拉框"
field_multiple_drop_box = "多选下拉框"
field_check_box = "复选框"
field_radio_button = "单选框"
field_rich_textbox = "富文本"
field_attachment_upload = "附件上传"
field_customized_table = "自定义表格"
field_tree_selection = "树形选择"
field_customized_form = "自定义表单"


#删除服务
service_del_button = '//span[@title="fdsafdsa"]/../../../../../td[12]/div/div'
# service_del_coreflow="//span[@title='{}']/../../..//button[@data-test-id='service_button_deleteService3']".format(settings.SERVICENAME_CIRCLE_FLOW)
# service_del_defflow="//span[@title='{}']/../../..//button[@data-test-id='service_button_deleteService3']".format(settings.SERVICE_NAME_DEFAULT_FLOW_CHANGE)

service_del_confirm= '//div[@class="bk-dialog-wrapper"]/div/div/div[5]/div/button[1]'

#搜索服务
search_service = '//input[@placeholder="请输入服务名"]'
service_input = 'service_name_default_flow_change'

#全部服务勾选
all_service = '//thead[@class="has-gutter"]/tr/th[1]/div/div/label/span'

#批量删除服务
all_service_del = '//button[@title="批量删除"]'
all_service_del_confirm = '//div[@class="bk-dialog-wrapper"]/div/div/div[5]/div/button[1]'