# -*- coding: utf-8 -*-
# @Time : 2021/1/26 16:29
# @File : test_40_del_process_design.py
# @Project : ITSM_257

import seldom
import sys
import time

sys.path.append("../")
import settings
import test_dir.test_0_login


# 创建默认流程
class DeleteFlowVersion(seldom.TestCase):
    def test_del_all(self):
        test_dir.test_0_login.Login.test_login(self)

        # 跳转到后台管理
        self.click(xpath="//li/a[@href='#/serviceEntry']")
        self.click(xpath="//div[@class='nav-slider-list']/div/div/div/span[contains(.,'流程管理')]")
        self.click(xpath="//div[@class='nav-slider-list']//span[contains(.,'流程版本')]")
        self.wait(3)
        self.click(xpath="//tr/th//span")
        self.click(xpath="//div[@class='bk-only-btn']//button[@title='批量删除']")
        self.click(xpath="//div[@class='bk-dialog-wrapper']//div/button[@name='confirm']")



#     # 点击删除处理场景流程
#     def test_delete_scene_flow_version(self):
#         self.delete_flow_version(settings.PROCESSING_SCENE)
#
#     # 删除处理人流程
#     def test_delete_processor_flow_version(self):
#         self.delete_flow_version(settings.PROCESSOR)
#
#     # 删除条件流程
#     def test_delete_conditions_flow_version(self):
#         self.delete_flow_version(settings.CONDITIONS_FLOW_NAME)
#
#     # 删除并行流程
#     def test_delete_parallel_flow_version(self):
#         self.delete_flow_version(settings.PARALLEL_FLOW_NAME)
#
#     # 删除ui触发器
#     def test_delete_ui_trigger_version(self):
#         self.delete_flow_version(settings.TRIGGER_FLOW)
#
#     # 删除审批节点流程
#     def test_delete_approve_node_flow_version(self):
#         self.delete_flow_version(settings.APPROVE_NODE_FLOW_NAME)
#
#     # 删除会签节点流程
#     def test_delete_countersign_node_flow_version(self):
#         self.delete_flow_version(settings.COUNTERSIGN_NODE_FLOW_NAME)
#
#     # 删除标准运维节点流程
#     def test_delete_sops_node_flow_version(self):
#         self.delete_flow_version(settings.SOPS_NODE_FLOW_NAME)
#
#     # 删除API节点流程
#     def test_delete_api_node_flow_version(self):
#         self.delete_flow_version(settings.API_NODE_FLOW_NAME)
#
#     # 删除默认节点流程
#     def test_delete_default_flow_version(self):
#         self.delete_flow_version(settings.CHANGE_DEFAULT_FLOW_NAME)
#
#     def delete_flow_version(self, version_name):
#         self.click(xpath="//span[@title='{}']/../../../td//button[@title='删除']".format(version_name))
#         self.wait(1)
#         self.assertText('流程版本删除确认')
#         self.click(xpath="//div[@class='bk-dialog-footer']/div/button[@name='confirm']")
#         self.assertText('删除成功')
#         self.wait(1)
#
#
# if __name__ == "__main__":
#     seldom.main(debug=True)
