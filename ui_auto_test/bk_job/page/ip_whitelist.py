# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     ip_whitelist.py
   Description : 
   Author :       v_adanchen
   date：          2021/9/17
-------------------------------------------------
"""

#平台管理
navigation_publicScriptList="//div[@data-test-id='navigation_publicScriptList']"
#IP白名单
navigation_whiteIp="//div[@data-test-id='navigation_whiteIp']"
#新建
new_ip="//div[@class='list-action-layout']//button"
#业务
bz_blueking="//div[@class='bk-select-name']"
#选择业务
bz_selected="//ul[@class='bk-options']/li/div/div[@title='蓝鲸']"
#取消选择业务
bz_unselected="//ul[@class='bk-options']/li/div/div[@title='{}']"
#输入IP
input_ip="//div[@class='bk-textarea-wrapper']/textarea[@placeholder='输入IP，以“回车”分隔']"
#输入备注
input_notes="//div[@class='bk-textarea-wrapper']/textarea[@placeholder='请输入']"
#生效范围
action_on="//div[@class='bk-form-control']/label/span[contains(.,'脚本执行')]"
#c侧滑
slider_title="//div[@class='bk-sideslider-header']"
#提交
commit="//div[@class='jb-sideslider-footer']/button/div/span[contains(.,'提交')]"
#编辑白名单
edit_ipwhite='//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_createWhiteIP"]'
#保存
save_ip="//div[@class='jb-sideslider-footer']/button/div/span[contains(.,'保存')]"
#搜索
search_ip="//div[@class='search-input-box']/textarea"
#ip
ip_num="//tbody/tr/td[1]/div/span"
#删除
del_ip='//div[@class="bk-table-fixed-right"]//button[@data-test-id="button_deleteWhiteIP"]'
#确定删除
del_comfirm="//div[@class='confirm-options']/button/div/span[contains(.,'确定')]"


