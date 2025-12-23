# -*- coding: utf-8 -*-
# @Time : 2025/01/13 15:59
# @File : 自定义指标

create_metrics = {
    'path': '//button/div//span[contains(.,"新建")]',
    'msg': '新建'
}

create_en_name = {
    'path': '//div/input[@placeholder="输入数据ID的英文名称"]',
    'msg': '新建》英文名称'
}

create_data_name = {
    'path': '//div/input[@placeholder="输入数据ID的名称"]',
    'msg': '新建》数据名称'
}

create_monitor_layer = {
    'path': '//div[@class="bk-tooltip bk-select-dropdown"]/div/div[@class="bk-select-name"]',
    'msg': '新建》监控对象'
}

create_monitor_layer_name = {
    'path': '//div/div[@title="业务应用"]',
    'msg': '新建》监控对象》业务应用'
}

create_protocol = {
    'path': '//div[@class="bk-button-group"]/button/div/span[contains(.,"JSON")]',
    'msg': '新建》上报协议'
}

create_submit = {
    'path': '//button[@class="mc-btn-add bk-primary bk-button-normal bk-button"]',
    'msg': '新建》提交'
}

metrics_data_id = {
    'path': '//div[@class="detail-information"]/div[2]/span[2]',
    'msg': '获取数据ID的值'
}

check_metrics = {
    'path': '//tr[@data-table-row="row-0"]/td[2]/div/span',
    'msg': '列表点击第一个'
}

metrics_search = {
    'path': '//div[@class="bk-input-text"]/input[@placeholder="搜索 ID / 名称"]',
    'msg': '自定义指标》查询'
}

metrics_del = {
    'path': '//button/div/span[contains(text(),"删除")]',
    'msg': '自定义指标》删除'
}

metrics_del_confirm = {
    'path': '//div[@class="footer-wrapper"]/button/div/span[contains(.,"确定")]',
    'msg': '自定义指标》删除》确定'
}

create_event_en_name = {
    'path': '//div/input[@placeholder="输入自定义事件英文名称"]',
    'msg': '新建》英文名称'
}

create_event_data_name = {
    'path': '//div/input[@placeholder="输入自定义事件名称"]',
    'msg': '新建》数据名称'
}