# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_14_del_field.py
   Description : 
   Author :       v_adanchen
   date：          2021/12/27
-------------------------------------------------
"""
import time

import seldom
import bk_itsm.settings as settings
from bk_itsm.page import add_field as page


class DelField(seldom.TestCase):
    def test_01_del_customized_form(self):
        """"删除自定义表单字段"""
        self.click(xpath=page.project)
        self.click(xpath=page.nav_field)
        self.del_field(settings.ZIDINGYIBIAODAN)

    def test_02_del_tree_selection(self):
        """"删除树形选择字段"""
        self.del_field(settings.SHUXINGXUANZE)

    def test_03_del_customized_table(self):
        """"删除自定义表格字段"""
        self.del_field(settings.ZIDINGYIBIAOGE)

    def test_04_del_attachment_upload(self):
        """"删除上传文件字段"""
        self.del_field(settings.FUJIANSHANGCHUAN)

    def test_05_del_rich_textbox(self):
        """"删除富文本字段"""
        self.del_field(settings.FUWENBEN)

    def test_06_del_radio_button(self):
        """"删除单选框字段"""
        self.del_field(settings.DANXUANKUANG)

    def test_07_del_check_box(self):
        """"删除多选框字段"""
        self.del_field(settings.FUXUANKUANG)

    def test_08_del_multiple_drop_box(self):
        """"删除多选下拉款字段"""
        self.del_field(settings.DUOXUANXIALAKUANG)

    def test_09_del_enter_single_drop_box(self):
        """"删除可输入单选下拉狂=框字段"""
        self.del_field(settings.KESHURUDANXUANXIALAKUANG)

    def test_10_del_single_drop_box(self):
        """"删除单选下拉框字段"""
        self.del_field(settings.DANXUANXIALAKUANG)

    def test_11_del_time(self):
        """"删除时间字段"""
        self.del_field(settings.SHIJIAN)

    def test_12_del_date(self):
        """"删除日期字段"""
        self.del_field(settings.RIQI)

    def test_13_del_link(self):
        """"删除链接字段"""
        self.del_field(settings.LIANJIE)

    def test_14_del_multiple_person(self):
        """"删除多选人员字段"""
        self.del_field(settings.DUOXUANRENYUANXUANZE)

    def test_15_del_radio_person(self):
        """"删除单选人员字段"""
        self.del_field(settings.DANXUANRENYUANXUANZE)

    def test_16_del_number(self):
        """"删除数字字段"""
        self.del_field(settings.SHUZI)

    def test_17_del_multi_line(self):
        """"删除多行文本字段"""
        self.del_field(settings.DUOHANGWENBEN)

    def test_18_del_single_line(self):
        """"删除单行文本字段"""
        self.del_field(settings.DANHANGWENBEN)

    def del_field(self, name):
        time.sleep(3)

        self.click(xpath=page.del_first_field)
        # self.click(xpath=page.del_field(name))
        self.click(xpath=page.del_confirm)
