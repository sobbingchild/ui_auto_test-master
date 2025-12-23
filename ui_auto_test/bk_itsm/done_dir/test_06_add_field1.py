# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     test_06_add_field1.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/25
-------------------------------------------------
"""
import seldom
import bk_itsm.page.add_field as page
import time


# 已完成

class AddField(seldom.TestCase):

    def test_01_add_field_single_line(self):
        """"添加单行文本"""
        self.click(xpath=page.project)
        time.sleep(1)
        self.click(xpath=page.nav_field)
        self.add_field(page.field_single_line)

    def test_02_add_multi_line(self):
        """"添加多行文本"""
        self.add_field(page.field_multi_line)

    def test_03_add_number(self):  # 数字字段 case
        """"添加数字"""
        self.add_field(page.field_add_number)

    def test_04_add_radio_person(self):  # 单选人员选择 case
        """"添加单选人员"""
        self.add_field(page.field_add_radio_person)

    def test_05_add_multiple_person(self):  # 多选人员选择 case
        """"添加多选人员"""
        self.add_field(page.field_add_multiple_person)

    def test_06_add_link(self):  # 链接 case
        """"添加链接"""
        self.add_field(page.field_add_link)

    def test_07_add_date(self):  # 日期 case
        """"添加日期"""
        self.add_field(page.field_add_date)

    def test_08_add_time(self):  # 时间 case
        """"添加时间"""
        self.add_field(page.field_add_time)

    def add_field(self, field_type):
        self.click(xpath=page.add_field)
        self.wait(1)
        # 填写字段名
        self.type(xpath=page.field_name, index=0, text=field_type)
        self.click(xpath=page.field_type)
        self.wait(1)
        self.type(xpath=page.search_type, text=field_type)
        self.click(xpath=page.choose_field_type(field_type))
        # 提交
        self.click(xpath=page.commit_field)
        self.wait(1)
