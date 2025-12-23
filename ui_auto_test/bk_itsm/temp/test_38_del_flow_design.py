# -*- coding: utf-8 -*-
# @Time : 2021/1/26 16:29
# @File : test_38_del_flow_design.py
# @Project : ITSM_257

import seldom
import sys
import time

sys.path.append("../")
import settings


# 创建默认流程
class DeleteFlowDesign(seldom.TestCase):
    def test_01_del_flow(self):
        try:
            self.get(settings.ITSM_URL)
            self.set_window(1920, 1080)
            self.wait(3)
            if self.get_title == settings.LOGIN_TITLE_ENGLISH:
                self.click(xpath='//*[@id="language-form"]/a')
                time.sleep(3)
            if self.get_title == settings.LOGIN_TITLE:
                # 输入账号
                self.type(xpath='//input[@id="user"]', text=settings.USER_NAME)
                # 输入密码
                self.type(xpath="//input[@id='password']", text=settings.PASSWORD)
                self.click(xpath='//button[@id="login-btn"]')
                self.wait(3)
                self.assertTitle(settings.INDEX_TITLE)
            else:
                self.get(settings.ITSM_URL)
                self.assertTitle(settings.INDEX_TITLE)
        except Exception as e:
            return print("登录失败")
            # 跳转到后台管理
        # 跳转到后台管理
        self.click(xpath='//ul[@class="nav-list"]/li[3]')
        self.wait(3)
        assert self.get_text(xpath='//p[@class="bk-come-back"]') == '服务'
        time.sleep(1)
        self.click(xpath='//div[@class="navigation-sbmenu-title"]/span[2]', index=1)
        self.wait(3)
        self.click(xpath='//div/a[1]', index=1)
        self.wait(3)
        time.sleep(1)

    # 点击删除处理流程
    def test_02_delete_processing_scene_flow(self):
        self.delete_flow(settings.PROCESSING_SCENE)

    # 删除处理人流程
    def test_03_delete_processing_flow(self):
        self.delete_flow(settings.PROCESSOR)

    # 删除条件流程
    def test_04_delete_conditions_flow(self):
        self.delete_flow(settings.CONDITIONS_FLOW_NAME)

    # 删除并行流程
    def test_05_delete_parallel_flow(self):
        self.delete_flow(settings.PARALLEL_FLOW_NAME)

    # 删除ui触发器
    def test_06_delete_ui_trigger(self):
        self.delete_flow(settings.TRIGGER_FLOW)

    # 删除审批节点流程
    def test_07_delete_approve_node_flow(self):
        self.delete_flow(settings.APPROVE_NODE_FLOW_NAME)

    # 删除会签节点流程
    def test_08_delete_countersign_node_flow(self):
        self.delete_flow(settings.COUNTERSIGN_NODE_FLOW_NAME)

    # 删除标准运维节点流程
    def test_09_delete_sops_node_flow(self):
        self.delete_flow(settings.SOPS_NODE_FLOW_NAME)

    # 删除API节点流程
    def test_10_delete_api_node_flow(self):
        self.delete_flow(settings.API_NODE_FLOW_NAME)

    # 删除默认节点流程
    def test_11_delete_default_flow(self):
        self.delete_flow(settings.CHANGE_DEFAULT_FLOW_NAME)
    #删除闭环流程
    def test_12_delete_circle_flow(self):
        self.delete_flow(settings.FLOWNAME_CIRCLE_FLOW)

    # 删除还原回来的流程
    def test_13_del_re_flow(self):
        self.click(xpath="//div[@class='bk-input-text']/input")
        self.type(xpath="//div[@class='bk-input-text']/input", text=settings.PROCESSING_SCENE)
        self.Keys(xpath="//div[@class='bk-input-text']/input").enter()
        self.click(xpath="//tr[1]/td[9]//span[contains(.,'删除')]")
        self.wait(1)
        self.assertText('确认删除此流程？')
        self.click(xpath='//button[@name="confirm"]')
        self.assertText('删除成功')
        self.wait(1)

    def delete_flow(self, flow_name):
        assert self.get_text(
            xpath='//span[@title="{}"]/../../..//span[@style="margin-left: 5px;"]'.format(flow_name)) == '启用'
        self.click(xpath='//span[@title="{}"]/../../../td//button[5]'.format(flow_name))
        self.wait(1)
        self.assertText('确认删除此流程？')
        self.click(xpath='//button[@name="confirm"]')
        self.assertText('删除成功')
        self.wait(1)


if __name__ == "__main__":
    seldom.main(debug=True)
