# -*- coding: utf-8 -*-
# @Time : 2022/1/14 14:58
# @File : index_page.py

# 项目流程
#PROJECT_FLOW = '//a[@data-test-id="navigation_list_process1"]'
PROJECT_FLOW = {
    'path': '//a[@data-test-id="navigation_list_processHome"]',
    'msg': '进入流程页面'
}
# 周期任务
PERIODIC_TASKS = {
    'path': '//a[@data-test-id="navigation_list_periodicTemplate"]',
    'msg': '进入周期任务页面'
}
# 计划任务
CLOCKED_TASK = {
    'path': '//a[@data-test-id="navigation_list_clockedTemplate"]',
    'msg': '进入计划任务页面'
}
# 轻应用
MINI_APP = {
    'path': '//a[@data-test-id="navigation_list_appMakerList"]',
    'msg': '进入轻应用页面'
}
