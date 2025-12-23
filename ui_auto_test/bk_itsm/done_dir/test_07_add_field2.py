# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_07_add_field2.py
   Description : 
   Author :       v_adanchen
   date：          2021/11/3
-------------------------------------------------
"""
import seldom
import bk_itsm.page.add_field as page


# 已完成

class AddField(seldom.TestCase):
    def test_01_add_field(self):
        """"添加字段初始化"""
        self.click(xpath=page.project)
        self.click(xpath=page.nav_field)

    def test_02_single_drop_box(self):
        """"单选下拉框"""
        custom_type = "Default"
        self.add_field(page.field_single_drop_box, custom_type)

    def test_03_enter_single_drop_box(self):
        """"可输入单选下拉框"""
        custom_type = "Default"
        self.add_field(page.field_enter_single_drop_box, custom_type)

    def test_04_multiple_drop_box(self):
        """"多选下拉框"""
        custom_type = "Default"
        self.add_field(page.field_multiple_drop_box, custom_type)

    def test_05_check_box(self):
        """"复选框"""
        custom_type = "Default"
        self.add_field(page.field_check_box, custom_type)

    def test_06_radio_button(self):
        """"单选框"""
        custom_type = "Default"
        self.add_field(page.field_radio_button, custom_type)

    def test_07_rich_textbox(self):
        """"富文本"""
        custom_type = "NONE"
        self.add_field(page.field_rich_textbox, custom_type)

    def test_08_attachment_upload(self):
        """"文件上传"""
        custom_type = "NONE"
        self.add_field(page.field_attachment_upload, custom_type)

    def test_09_customized_table(self):
        """"自定义表格"""
        custom_type = "Table"
        self.add_field(page.field_customized_table, custom_type)

    def test_10_tree_selection(self):
        """"树形选择"""
        custom_type = "Tree"
        self.add_field(page.field_tree_selection, custom_type)

    def test_11_customized_form(self):
        """"自定义表单"""
        custom_type = "NONE"
        self.add_field(page.field_customized_form, custom_type)

    def add_field(self, field_type, custom_type):
        self.click(xpath=page.add_field)
        self.wait(2)
        # 填写字段名
        self.type(xpath=page.field_name, index=0, text=field_type)
        self.click(xpath=page.field_type)
        self.wait(1)
        self.type(xpath=page.search_type, text=field_type)
        self.click(xpath=page.choose_field_type(field_type))
        if custom_type == "Table":
            self.type(xpath=page.custom_table, text=page.field_customized_table)
        elif custom_type == "Tree":
            self.click(xpath=page.source_data1, index=0)
            self.wait(1)
            self.click(xpath=page.source_choose_data1)
            self.click(xpath=page.source_data1, index=1)
            self.click(xpath=page.source_choose_data2)
        elif custom_type == "Default":
            self.click(xpath=page.custom_data_source)
            self.type(xpath=page.custom_data_name,text='a')
            # self.type(xpath=page.custome_field, index=0, text=field_type)
            self.click(xpath=page.custom_data_confirm)
        else:
            custom_type == ""
        # 提交
        self.click(xpath=page.commit_field)
        self.wait(2)
