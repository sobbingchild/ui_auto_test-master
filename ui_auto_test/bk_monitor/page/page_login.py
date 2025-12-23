

#Language
Switch_Language = '//*[@id="language-form"]/a'

# 切换中英文按钮
switch_language_ee = '//*[@id="language-form"]/a'
switch_language_ce = '//span[@id="ch"]'

# login页面图片
Login_photo = '//div[@class="logo-title"]/img'




#关闭提示框
close_hover = '//i[@class="icon-monitor icon-mc-close"]'

#导航栏各个

#锁定侧边栏
footer_lock = '//*[@class="footer-icon"]'

#侧边栏展开
footer_expand = '//span[@class="footer-icon-svg"]'

#配置
strategy_config='//a[@id="head-nav-strategy-config"]'
#集成
plugin_manager='//a[@id="head-nav-plugin-manager"]'

#切换项目
biz_select = '//div[@class="biz-select"]'


#配置
#告警组

#告警策略
alert_group = '//span[@class="nav-menu-item"][contains(text(),"告警组")]'
alert_event = '//span[@class="nav-menu-item"][contains(text(),"告警策略")]'

#告警组操作
create_group = '//button[@class="bk-primary bk-button-normal bk-button tool-btn mc-btn-add"]/div'
group_name = '//*[@class="bk-form"]/div[2]/div/div/div/div[1]/input'
group_name_input = 'UITEST'
group_to_user_select = '//*[@class="bk-form"]/div[4]/div/div/div[1]/div/div/div'
user_name = 'admin'
#开启微信通知--提醒类型
open_wechat_1 = '//*[@class="level-title-3"]/../../../td[2]/div/label'
open_wechat_2 = '//*[@class="level-title-2"]/../../../td[2]/div/label'
open_wechat_3 = '//*[@class="level-title-1"]/../../../td[2]/div/label'

#执行状态微信
status_wechat_1 = '//*[@class="bottom-title"][contains(text(),"每个执行阶段至少选择一种通知方式")]/../div/div/table/tbody/tr[1]/td[2]/div/label'
status_wechat_2 = '//*[@class="bottom-title"][contains(text(),"每个执行阶段至少选择一种通知方式")]/../div/div/table/tbody/tr[2]/td[2]/div/label'
status_wechat_3 = '//*[@class="bottom-title"][contains(text(),"每个执行阶段至少选择一种通知方式")]/../div/div/table/tbody/tr[3]/td[2]/div/label'


create_group_submit = '//*[@class="alarm-group-add-wrap page-wrapper"]/div[1]/button[1]'
delete_group_button = '//*[@class="notice-group-name"][contains(text(),"UITEST")]/../../../td[8]/div/button[2]/div/span'
delete_group_confirm = '//*[@class="header"][contains(text(),"确认要删除？")]/../../div[4]/div/button[1]'

#告警策略
create_alert_event = '//*[@class="bk-primary bk-button-normal bk-button header-btn mc-btn-add"]'
alert_name = '//*[@class="set-content-left"]/div[1]/div[2]/div/div[3]/div/div/div/div/input'
alert_name_input = 'testEVENT'
#指标
item_common = '//*[@id="set-panel-item-time_series"]'
common_select = '//*[@class="form-content monitor-input metric-wrap"]'
# common_input_pluginname = 'testplugin'
common_input_pluginname = 'script_autotest1plugin.disk_usage'
common_search = '//*[@class="built-in-item"][contains(text(),"常用")]/../../../../../../div[1]/div/div/input'
first_common = '//*[@class="built-in-item"][contains(text(),"常用")]/../../../../../../div[2]/div[2]/div[1]/div[1]'

#检测规则
new_algorithm = '//*[@class="select-type-panel"]/div[3]/div/div[1]'
new_rule = '//*[@class="rule-add"]'
high_rule = '//*[@class="item-text"][contains(text(),"致命")]'
##静态阈值
rule_select = '//*[@class="bk-option-name"][contains(text(),"静态阈值")]'
##添加告警组
group_select = '//*[@class="add-tag-text"][contains(text(),"添加告警组")]'
group_select_input = 'UITEST'
group_select_name = '//*[@class="item-name"][contains(text(),"UITEST")]'

#tijiao
alert_event_submit = '//*[@class="bk-primary bk-button-normal bk-button save-btn"]'
alert_event_option = '//*[@class="name-text-link"][contains(text(),"testEVENT")]/../../../../../../td[9]/div/div/span[3]/i'
alert_delete_button = '//*[@class="operator-group-btn"][contains(text(),"删除")]'
alert_delete_confirm = '//*[@class="header"][contains(text(),"你确认么？")]/../../div[5]/div/button[1]'
