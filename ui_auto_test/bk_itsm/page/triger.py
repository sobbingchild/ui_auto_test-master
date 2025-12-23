# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     triger.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/22
-------------------------------------------------
"""
project = "//a[@data-test-id='navigation-router-navRouter-project']"
nav_triger = "//a[@data-test-id='navigation-menu-projectTrigger']"

add_triger_permis = "//button[@data-test-id='triggers_button_create_permission']"

add_triger = "//button[@data-test-id='triggers_button_create']"

triger_name = "//div[@data-test-id='trigger-input-name']//input"

triger_event = "//div[@data-test-id='triggers_select_choiceEvent']"
# 选择创建单据
choose_triger_event_create = "//ul[@class='bk-options bk-options-single']/li[1]/ul/li[1]"
# 认领单据
choose_triger_event_claim = "//ul[@class='bk-options bk-options-single']/li[2]/ul/li[4]"
# 分派单据
choose_triger_event_dis = "//ul[@class='bk-options bk-options-single']/li[2]/ul/li[3]"

# 选择进入节点
choose_triger_event_inotes = "//ul[@class='bk-options bk-options-single']/li[2]/ul/li[1]"
# 选择离开节点
choose_triger_event_onotes = "//ul[@class='bk-options bk-options-single']/li[2]/ul/li[2]"
# 选择进入分支
choose_triger_event_branch_line = "//ul[@class='bk-options bk-options-single']/li[3]/ul/li[1]"
# 选择创建任务
choose_triger_event_branch_task = "//ul[@class='bk-options bk-options-single']/li[3]/ul/li[1]"

# 点击动作名称
event_name = "//div[@data-test-id='trigger-div-triggerRules']//div[@class='bk-response-way']/div[1]/div"
# 选择API执行
choose_event_name = "//div[@class='bk-select-dropdown-content']//ul/li[1]"
# 选择API ID,定位到两个，1级和2级分别取第一个和第二个
event_id = "//span[contains(.,'API接口ID')]/../../div[@class='bk-form-content']/div"
# 选择配置平台
choose_event_id = "//div[@class='bk-select-dropdown-content']/div/ul/li[1]"

# 选择查询业务
choose_event_id2 = "//div[@class='bk-options-wrapper']/ul/li[2]"

triger_commit = "//button[@data-test-id='trigger_button_submitTrigger'][contains(.,'确认')]"

# 断言
assert_create_successful = '创建成功'

# 删除触发器

def trigger_name(triger_name):
    trigger = "//ul[@class='bk-trigger-content']/li/span[@title='{}']".format(triger_name)
    return trigger


def del_trigger(triger_name):
    trigger_del = "//span[@title='{}']/../span[@class='bk-trigger-delete']".format(triger_name)
    return trigger_del


del_confirm = "//div[@class='footer-wrapper']/button[@name='confirm']"
