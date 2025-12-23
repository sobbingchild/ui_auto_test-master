# -*- coding: utf-8 -*-
# @Time : 2024/9/02 15:59
# @File : home.py
from public_method.login import LoginBase
navigation_scriptManage = {
    'path': '//div[@data-test-id="navigation_scriptManage"]',
    'msg': '作业管理=>脚本'
}

navigation_planManage = {
    'path': '//div[@data-test-id="navigation_planManage"]',
    'msg': '作业管理=>执行方案'
}

navigation_cronJob = {
    'path': '//div[@data-test-id="navigation_cronJob"]',
    'msg': '作业管理=>定时'
}

navigation_quick_script_excute = {
    'path': '//div[@data-test-id="navigation_fastExecuteScript"]',
    'msg': '作业管理=>快速执行=>脚本执行'
}

navigation_quick_file_excute = {
    'path': '//div[@data-test-id="navigation_fastPushFile"]',
    'msg': '作业管理=>快速执行=>文件分发'
}

navigation_account = {
    'path': '//div[@data-test-id="navigation_accountManage"]',
    'msg': '作业管理=>账号'
}

navigation_ticket = {
    'path': '//div[@data-test-id="navigation_ticketManage"]',
    'msg': '作业管理=>凭证'
}

navigation_tag = {
    'path': '//div[@data-test-id="navigation_tagManage"]',
    'msg': '作业管理=>标签'
}

navigation_fileManage = {
    'path': '//div[@data-test-id="navigation_fileManage"]',
    'msg': '作业管理=>文件源'
}

navigation_notifyManage = {
    'path': '//div[@data-test-id="navigation_notifyManage"]',
    'msg': '作业管理=>消息通知'
}



navigation_close = {
    'path': '//div/i[@class="fixed-flag job-icon job-icon-expand-line"]',
    'msg': '导航栏》收起'
}

sideslip_close = {
    'path': '//div[@class="bk-sideslider-closer"]',
    'msg': '侧滑栏》收起'
}

navigation_histories = {
    'path': '//div[@data-test-id="navigation_executiveHistory"]',
    'msg': '执行历史'
}

navigation_publicScriptList = {
    'path': '//div[@data-test-id="navigation_publicScriptList"]',
    'msg': '导航栏=>平台管理'
}

navigation_publicScript = {
    'path': '//div[@data-test-id="navigation_publicScript"]',
    'msg': '平台管理=>公共脚本'
}

navigation_globalSetting = {
    'path': '//div[@data-test-id="navigation_globalSetting"]',
    'msg': '平台管理=>全局配置'
}

globalSetting_AccountRules = {
    'path': '//div[@class="bk-tab-label"][contains(text(),"账号命名规则")]',
    'msg': '平台管理=>全局配置=>账号命名规则'
}

globalSetting_FileUploadSettings = {
    'path': '//div[@class="bk-tab-label"][contains(text(),"文件上传设置")]',
    'msg': '平台管理=>全局配置=>文件上传设置'
}

navigation_whiteIp = {
    'path': '//div[@data-test-id="navigation_whiteIp"]',
    'msg': '平台管理=>IP 白名单'
}

navigation_dangerousRuleManage= {
    'path': '//div[@data-test-id="navigation_dangerousRuleManage"]',
    'msg': '平台管理=>高危语句规则'
}

scroll_bar_left = {
    'path': '//div[@class="side-wrapper"]//div[@class="scrollbar-vertical"]/div[@class="scrollbar-inner"]',
    'msg': '导航栏=>滚动条'
}


scroll_bar = {
    'path': '//div[@class="jb-resize-layout-left"]//div[@class="scroll-faker"]//div[@class="scrollbar-vertical"]/div[@class="scrollbar-inner"]',
    'msg': '滚动条'
}

back_home = {
    'path': '//div[@class="jb-navigation-body-header"]/svg[@class="jb-router-back job-svg-icon"]',
    'msg': '返回按钮'
}

search = {
    'path': '//textarea[@class="input-box"]',
    'msg': '搜索框'
}

search_name = {
    'path': '//span[text()="任务名称"]',
    'msg': '搜索框内点击任务名称'
}

jobs = {
    'path': '//div[@data-test-id="navigation_taskManage"]',
    'msg': '作业'
}
