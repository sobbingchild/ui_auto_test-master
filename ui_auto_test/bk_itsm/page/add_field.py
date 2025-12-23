# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     add_field.py
   Description : 
   Author :       v_adanchen
   date：          2021/10/21
-------------------------------------------------
"""

# 参考添加流程字段，流程字段调好后再写

project = "//a[@data-test-id='navigation-router-navRouter-project']"
# 这个定位需要修改
nav_field = "//a[@data-test-id='navigation-menu-projectFields']"
add_field = "//button[@data-test-id='field_button_addField']"
field_name = "//div[@data-test-id='field-input-fieldName']//input"
field_type = "//div[@data-test-id='field-select-fieldType']//div[@title='单行文本']"
search_type = "//div[@class='bk-select-dropdown-content']/div/input"

commit_field = "//button[@data-test-id='field_button_submit']"
search_field = "//div[@data-test-id='field_input_searchField']/div/input"
search_result = "//tr/td[1]/div/span[@title='{}']"
source_data1 = "//div[@class='bk-data-source']//div[@class='bk-select-name']"
source_choose_data1 = "//ul[@class='bk-options bk-options-single']/li[1]"
source_choose_data2 = "//ul[@class='bk-options bk-options-single']/li[1]"


custom_data_source = '//*[@title="配置数据源"]'
custom_data_name = '//*[@placeholder="请输入选项名"]'
custome_field = "//section//form//div[@class='bk-data-content']//input"
custom_data_confirm = '//*[@class="footer-wrapper"]/button[1]'
custom_table = "//div[@class='bk-custom-line']//div[@class='bk-input-text']/input"

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


def choose_field_type(field_type):
    choose_field_type = "//div[@class='bk-select-dropdown-content']//ul/li/div/div[@title='{}']".format(field_type)
    return choose_field_type


# 删除字段
del_totle_number = "//div[@class='bk-table-pagination-wrapper']//div[@class='bk-select-name']"

del_totle_li = "//div[@class='bk-select-dropdown-content']//ul/li[3]"


def del_field(field_name):
    field_del = "//span[@title='{}']/../../../td[8]//button[@data-test-id='field_button_deletefield']".format(field_name)
    return field_del


del_confirm="//div[@class='bk-dialog-footer']/div/button[@name='confirm']"
del_first_field = '//*[@class="bk-table-fixed-right"]/div[2]/table/tbody/tr[1]/td[8]/div/button[2]/div'
