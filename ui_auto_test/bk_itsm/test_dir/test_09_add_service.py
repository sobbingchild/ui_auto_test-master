# -*- coding: utf-8 -*-
# @Time : 2021/1/10 11:11
# @File : test_09_add_service.py
# @Project : ITSM_257

import time
import seldom
from bk_itsm.page import add_service as page
import bk_itsm.settings as settings


# sys.path.append("../")
#
#
# node_name = 'case_2'

# 添加手动节点和添加字段，未完成

class AddService(seldom.TestCase):
    def test_01_add_service(self):
        """"添加服务"""
        # 点击项目
        self.click(xpath=page.project)
        # 点击服务
        self.click(xpath=page.nav_service)
        # 点击添加服务
        self.click(xpath=page.add_service)
        # 点击服务名输入框
        self.click(xpath=page.service_name)
        # 输入服务名称
        self.type(xpath=page.service_name, text=settings.SERVICENAME_CIRCLE_FLOW)
        # 点击服务目录
        self.click(xpath=page.service_dir)
        # 选择服务目录
        self.click(xpath=page.choose_service_dir)
        # 点击服务类型
        self.click(xpath=page.service_type)
        # 选择服务类型
        self.click(xpath=page.choose_service_type)
        # 确定添加
        self.click(xpath=page.service_comfirm)
        time.sleep(1)
        # 点击服务模板
        self.click(xpath=page.service_temp)
        # 选择服务模板
        self.click(xpath=page.choose_service_temp)
        # 点击下一步
        self.click(xpath=page.service_next)

    def test_02_add_node1(self):
        """"添加节点1"""
        # 点击默认的连接线
        self.click(xpath=page.line_default)
        time.sleep(1)
        # 删除默认的连接线
        self.click(xpath=page.del_line_default)
        time.sleep(1)
        # 右击提单节点
        self.right_click(xpath=page.node_comit_ticket)
        # 点击节点面板
        self.click(xpath=page.panel_comit_ticket)
        # 双击手动节点
        self.double_click(xpath=page.new_node1)
        # 输入手动节点的名称
        self.type(xpath=page.node1_name, text=settings.TEST_NODE1)
        # 点击处理场景
        self.click(xpath=page.node1_scenes)
        # 选择处理场景
        self.click(xpath=page.node1_scenes_choose)
        # 点击派单人
        self.click(xpath=page.node1_dispatch)
        # 选择派单人
        self.click(xpath=page.node1_dispatch_choose)
        # 点击处理人
        self.click(xpath=page.node1_handler)
        # 选择处理人
        self.click(xpath=page.node1_handler_choose)
        # 是否转单
        self.click(xpath=page.node1_is_transfer)
        # 选择是
        self.click(xpath=page.node1_transfer_click)
        # 选择转单人1级目录
        self.click(xpath=page.node1_transfer_choose)
        # 点击转单人2级目录
        self.click(xpath=page.node1_transfer_click2)
        # 选择转单人
        self.click(xpath=page.node1_transfer_choose2)
        ###### 添加字段  ######
        # 单行文本
        self.add_field(page.field_single_line, "")
        # 多行文本
        self.add_field(page.field_multi_line, "")
        # 数字
        self.add_field(page.field_add_number, "")
        # 单选人员选择
        self.add_field(page.field_add_radio_person, "")
        # 多选人员选择
        self.add_field(page.field_add_multiple_person, "")
        # 链接
        self.add_field(page.field_add_link, "")
        # 日期
        self.add_field(page.field_add_date, "")
        # 时间
        self.add_field(page.field_add_time, "")
        # 高级设置
        self.click(xpath=page.node1_high_setting)
        # 添加触发器
        self.click(xpath=page.node1_add_trigger)
        # 选择公共触发器
        self.click(xpath=page.node1_pub_trigger)
        # 选择触发器
        self.click(xpath=page.node1_choose_trigger)
        # 提交触发器
        self.click(xpath=page.node1_pub_trigger_comfirm)
        # 提交节点1
        self.click(xpath=page.node1_comfirm)

    def test_03_add_API(self):
        """"添加API节点"""
        # 右击节点1
        self.right_click(xpath=page.panel_node1)
        self.click(xpath=page.parallel_gateway_choose, index=1)
        self.right_click(xpath=page.panel_parallel)
        self.click(xpath=page.node_li_api)
        self.right_click(xpath=page.panel_parallel)
        self.click(xpath=page.node_li_sops)
        self.double_click(xpath=page.node_api)
        self.type(xpath=page.node_api_name, text=settings.API_NODE_FLOW_NAME)
        self.click(xpath=page.node_api_interface)
        self.click(xpath=page.node_api_interface_choose)
        self.click(xpath=page.node_api_interface2)
        self.click(xpath=page.node_api_interface_choose2)
        self.click(xpath=page.node_api_handler)
        self.click(xpath=page.node_api_handler_choose)
        self.click(xpath=page.node_api_handler2)
        self.type(xpath=page.node_api_handler_input, text=settings.INPUT_USER1)
        time.sleep(2)
        self.type_enter(xpath=page.node_api_handler_input)
        self.click(xpath=page.node_api_comfirm)

    def test_04_add_sops(self):
        """"添加标准运维节点"""
        self.double_click(xpath=page.node_sops)
        self.type(xpath=page.node_sops_name, text=settings.SOPS_NODE_FLOW_NAME)
        self.click(xpath=page.node_sops_type)
        self.click(xpath=page.node_sops_type_choose)
        self.click(xpath=page.node_sops_bz)
        self.click(xpath=page.node_sops_bz_choose)
        self.click(xpath=page.node_sops_temp)
        self.click(xpath=page.node_sops_temp_choose)
        # 高级设置
        self.click(xpath=page.node_sops_high_setting)
        self.click(xpath=page.node_sops_add_trigger)
        self.click(xpath=page.node_sops_pub_trigger)
        self.click(xpath=page.node_sops_choose_trigger)
        self.click(xpath=page.node_sops_pub_trigger_comfirm)
        self.click(xpath=page.node_sops_comfirm)

    def test_05_add_node2(self):
        """"添加节点2"""
        # 右击标准运维
        self.right_click(xpath=page.panel_sops)
        # 选择汇聚网关
        self.click(xpath=page.convergence_gateway_choose)
        # 右击汇聚网关
        self.right_click(xpath=page.panel_convergence_gateway)
        self.click(xpath=page.node2_choose, index=1)
        time.sleep(1)
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        self.double_click(xpath=page.node2_click)
        self.type(xpath=page.node2_name, text=settings.TEST_NODE2)
        self.click(xpath=page.node2_handler)
        self.click(xpath=page.node2_handler_choose)
        self.click(xpath=page.node2_comfirm)
        # 分支判断
        # 第一个分支
        self.branch_info("用于触发器=1", "1")

    def test_06_add_countersign_node(self):
        """"添加会签节点"""
        self.right_click(xpath=page.panel_convergence_gateway)
        self.click(xpath=page.node_countersign_choose, index=1)
        self.double_click(xpath=page.node_countersign_click)
        self.type(xpath=page.node_countersign_name, text=settings.COUNTERSIGN_NODE_FLOW_NAME)
        self.click(xpath=page.node_countersign_method)
        self.click(xpath=page.node_countersign_handler)
        self.type(xpath=page.node_countersign_handler1, text=settings.INPUT_USER1)
        time.sleep(1)
        self.type_enter(xpath=page.node_countersign_handler1)
        self.type(xpath=page.node_countersign_handler2, text=settings.INPUT_USER2)
        time.sleep(1)
        self.type_enter(xpath=page.node_countersign_handler2)
        self.type(xpath=page.node_countersign_handler3, text=settings.INPUT_USER3)
        self.type_enter(xpath=page.node_countersign_handler3)
        self.click(xpath=page.node_countersign_number)
        self.type(xpath=page.node_countersign_number, text="3")
        self.click(xpath=page.node_countersign_comfirm)
        # 第二个分支
        self.branch_info("用于触发器≠1", "0")

    def test_07_add_node3(self):
        """"添加节点3"""
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        self.right_click(xpath=page.panel_node_countersign)
        self.click(xpath=page.node3_choose)
        self.double_click(xpath=page.node3_click)
        self.click(xpath=page.node3_name)
        self.type(xpath=page.node3_name, text=settings.TEST_NODE3)
        self.click(xpath=page.node3_scenes)
        self.click(xpath=page.node3_scenes_choose)
        self.click(xpath=page.node3_handler)
        self.click(xpath=page.node3_handler_choose)
        self.click(xpath=page.node3_handler2)
        self.click(xpath=page.node3_handler_choose2)
        self.click(xpath=page.node3_handler2)
        self.add_field(page.field_single_drop_box, "Default")
        self.add_field(page.field_enter_single_drop_box, "Default")
        self.add_field(page.field_multiple_drop_box, "Default")
        self.add_field(page.field_check_box, "Default")
        self.add_field(page.field_radio_button, "Default")
        self.add_field(page.field_rich_textbox, "NONE")
        self.add_field(page.field_attachment_upload, "NONE")
        self.add_field(page.field_customized_form, "NONE")
        self.add_field(page.field_customized_table, "Table")
        self.add_field(page.field_tree_selection, "Tree")
        self.click(xpath=page.node3_high_setting)
        self.click(xpath=page.node3_add_trigger)
        self.click(xpath=page.node3_pub_trigger)
        self.click(xpath=page.node3_pub_trigger_choose)
        self.click(xpath=page.node3_pub_trigger_comfirm)
        self.click(xpath=page.node3_comfirm)

    def test_08_add_approve(self):
        """"审批节点"""
        time.sleep(1)
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        self.right_click(xpath=page.node3_panel)
        self.click(xpath=page.node_approve_choose, index=3)
        self.double_click(xpath=page.node_approve_click)
        self.type(xpath=page.node_approve_name, text=settings.APPROVE_NODE_FLOW_NAME)
        self.click(xpath=page.node_approve_handler)
        time.sleep(1)
        self.click(xpath=page.node_approve_handler_choose)
        self.click(xpath=page.node_approve_handler2)
        time.sleep(1)
        self.click(xpath=page.node_approve_handler_choose2)
        self.click(xpath=page.node_approve_high_setting)
        time.sleep(2)
        self.click(xpath=page.node_approve_add_trigger)
        self.click(xpath=page.node_approve_new_trigger)
        self.type(xpath=page.node_approve_newtriger_name, text=settings.TRIGGER_NAME)
        self.click(xpath=page.node_approve_newtriger_event)
        time.sleep(1)
        self.click(xpath=page.choose_triger_event_inotes)
        self.click(xpath=page.event_name)
        time.sleep(1)
        self.click(xpath=page.choose_event_name)
        time.sleep(2)
        self.click(xpath=page.event_id, index=0)
        time.sleep(1)
        self.click(xpath=page.choose_event_id)
        time.sleep(1)
        self.click(xpath=page.event_id, index=1)
        time.sleep(1)
        self.click(xpath=page.choose_event_id2)
        time.sleep(1)
        self.click(xpath=page.node_approve_new_trigger_comfirm)
        time.sleep(1)
        self.click(xpath=page.node_approve_comfirm)

    def test_09_add_node4(self):
        """"添加节点4"""
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        self.right_click(xpath=page.panel_approve)
        self.click(xpath=page.node_4)
        self.double_click(xpath=page.node4_click)
        self.type(xpath=page.node4_name, text=settings.TEST_NODE4)
        self.click(xpath=page.node4_scenes)
        self.click(xpath=page.node4_scenes_choose)
        self.click(xpath=page.node4_dispatch, index=0)
        self.click(xpath=page.node4_dispatch_choose)
        self.click(xpath=page.node4_handler, index=1)
        self.click(xpath=page.node4_handler_choose)
        self.click(xpath=page.node4_high_setting)
        self.click(xpath=page.node4_add_trigger)
        self.click(xpath=page.node4_pub_trigger)
        self.click(xpath=page.node4_choose_trigger_hang)
        self.click(xpath=page.node4_choose_trigger_recover)
        self.click(xpath=page.node4_pub_trigger_comfirm)
        self.click(xpath=page.node4_comfirm)

    def test_10_add_con_line(self):
        """"添加连接线"""
        # API节点连接汇聚节点
        self.click_and_hold(xpath=page.dot_api_right)
        self.move_to_element(xpath=page.dot_converge_top)
        # 用于释放连线
        self.click(xpath=page.panel_convergence_gateway)
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        # 节点2连接节点3
        self.click_and_hold(xpath=page.dot_node2_right)
        self.move_to_element(xpath=page.dot_node3_top)
        time.sleep(1)
        self.click(xpath=page.test_ui_node3)
        time.sleep(1)
        self.click(xpath=page.node3_cancel)
        time.sleep(2)
        # self.click(xpath=page.dot_node3_top)
        ##缩小画布
        self.double_click(xpath=page.canvas_tools_reduc)
        # 节点4连接结束节点
        self.click_and_hold(xpath=page.dot_node4_right)
        self.move_to_element(xpath=page.dot_end)
        self.click(xpath=page.dot_end)

    def test_11_flow_settings(self):
        """"设置流程"""
        self.click(xpath=page.flow_next)
        self.click(xpath=page.flow_high_settings)
        self.click(xpath=page.flow_add_trigger)
        self.click(xpath=page.flow_pub_trigger)
        self.click(xpath=page.flow_pub_create)
        self.click(xpath=page.flow_trigger_confirm)
        self.click(xpath=page.flow_temp_on)
        self.click(xpath=page.flow_temp)
        self.click(xpath=page.flow_temp_choose)
        time.sleep(1)
        self.click(xpath=page.flow_create_node)
        self.click(xpath=page.flow_create_node_choose)
        time.sleep(1)
        self.click(xpath=page.flow_deal_node)
        self.click(xpath=page.flow_deal_choose)
        self.click(xpath=page.flow_commit)

    # 添加自定义字段
    def add_field(self, field_type, custom_type):
        self.click(xpath=page.node1_add_field)
        self.wait(2)
        # 填写字段名
        self.type(xpath=page.node1_field_name, index=0, text=field_type)
        self.click(xpath=page.node1_field_type)
        self.wait(1)
        self.type(xpath=page.node1_search_type, text=field_type)
        self.click(xpath=page.choose_field_type(field_type))
        if custom_type == "Table":
            self.type(xpath=page.node3_field_custom_table, text=page.field_customized_table)
        elif custom_type == "Tree":
            self.click(xpath=page.node3_source_data, index=0)
            self.wait(1)
            self.click(xpath=page.node3_source_data_choose1)
            self.click(xpath=page.node3_source_data, index=1)
            self.click(xpath=page.node3_source_data_choose2)
        elif custom_type == "Default":
            self.type(xpath=page.node3_field_multi_field, index=0, text=field_type)
        else:
            custom_type == ""
        # 提交
        self.click(xpath=page.node1_commit_field)
        self.wait(1)

    def branch_info(self, name, valus):
        self.click(xpath=page.node2_default2, index=5)
        self.click(xpath=page.node2_branch_name)
        self.type(xpath=page.node2_branch_name, text=name)
        if valus == "0":
            self.click(xpath=page.node2_branch_condi)
            self.click(xpath=page.node2_branch_condi_choose)
            self.click(xpath=page.node2_branch_condi_1)
            self.click(xpath=page.node2_branch_condi_1_choose)
            self.click(xpath=page.node2_branch_condi_2)
            self.click(xpath=page.node2_branch_condi_2_choose)
            self.click(xpath=page.node2_branch_condi_3)
            self.type(xpath=page.node2_branch_condi_3, text=valus)
            self.click(xpath=page.node2_branch_trigger)
            self.click(xpath=page.node2_branch_pub_trigger)
            self.click(xpath=page.node2_branch_triger_choose)
            self.click(xpath=page.node2_branch_triger_confirm)
        self.click(xpath=page.node2_branch_condi_comfirm)
