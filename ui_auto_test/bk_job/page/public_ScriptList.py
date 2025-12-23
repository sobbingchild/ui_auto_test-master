# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     public_ScriptList.py
   Description :
   Author :       v_jingdhe
   date：          2021/09/14
-------------------------------------------------
平台管理
"""
#导航栏-平台管理
navigation_publicScriptList = '//div[@data-test-id="navigation_publicScriptList"]'

#侧边栏-高危语句规则
navigation_dangerousRuleManage = '//div[@data-test-id="navigation_dangerousRuleManage"]'

#新的规则
new_dangerousRuleManage = '//table[@class="rule-table"]/tbody[1]/tr/td/button'

#语法表达式
Syntax_expression = '//div[@class="dangerous-rule-manage-product_page"]/table/tbody[1]/tr/td[1]/div/div/input'
#用于断言,tbody[2]为第一条规则的语法表达式,如需第二条自己改tbody[2]为[3]
Syntax_expression_text = '//table[@class="rule-table"]/tbody[2]/tr/td[1]/div/div/div[1]/span'

#规则说明
Rules_specification = '//div[@class="dangerous-rule-manage-product_page"]/table/tbody[1]/tr/td[2]/div/div/input'

#脚本类型
Script_type =   '//div[@class="dangerous-rule-manage-product_page"]/table/tbody[1]/tr/td[3]/div'
Type_all = '//ul[@class="bk-options"]/li[1]'
Type_Shell = '//ul[@class="bk-options"]/li[2]'
Type_Bat = '//ul[@class="bk-options"]/li[3]'
Type_Perl = '//ul[@class="bk-options"]/li[4]'
Type_Python = '//ul[@class="bk-options"]/li[5]'
Type_Powershell = '//ul[@class="bk-options"]/li[6]'
Type_SQL = '//ul[@class="bk-options"]/li[7]'

#动作
Rules_action =  '//div[@class="dangerous-rule-manage-product_page"]/table/tbody[1]/tr/td[4]/div'

Action_scan = '//ul[@class="bk-options bk-options-single"]/li[1]'
Action_intercept = '//ul[@class="bk-options bk-options-single"]/li[2]'

#规则操作-保存规则
Rules_save = '//table[@class="rule-table"]/tbody[1]/tr/td[5]/button[1]'
#规则操作-删除第一条规则,tbody[2]为第一条,如需第二条自己单独copy把[2]改成[3]
# Rules_delete = '//table[@class="rule-table"]/tbody[2]/tr/td[5]/div/div[2]'
Rules_delete = "//span[contains(text(),'testtext')]/../../../../../td[5]/div/div[2]/button/div/span"
#规则删除-确认删除
Delete_confirm = '//button[@class="confirm-option-button bk-primary bk-button-small bk-button"]'
