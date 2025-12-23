# -*- coding: utf-8 -*-
# @Time : 2025/01/09 15:59
# @File : alert_team.py

alert_team = {
    'path': '//div[@class="bk-navigation-menu-group"]//span[@class="nav-menu-item"][contains(text(),"告警组")]',
    'msg': '侧边导航》告警组'
}

alert_team_new = {
    'path': '//button[@class="bk-primary bk-button-normal bk-button tool-btn mc-btn-add"]',
    'msg': '告警组》新建'
}

alert_team_new_name = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="请输入"]',
    'msg': '告警组》新建》告警名称'
}

alert_team_new_recipients = {
    'path': '//div[@class="user-selector-layout"]/div[@class="user-selector-container placeholder is-fast-clear"]',
    'msg': '告警组》新建》告警组'
}

alert_team_check_name = {
    'path': '//tr[@data-table-row="row-0"]/td[1]/div/span',
    'msg': '告警组》点击第一个告警组名称'
}