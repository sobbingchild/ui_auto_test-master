# -*- coding: utf-8 -*-
# @Time : 2025/01/20 15:13
# @File : notify.py

# 尝试整合

def get_xpath(execution_method, notification_method, msg, row_index=None, label_index=None):
    base_xpath = f'//span[@class="trigger-title"][contains(text(),"{execution_method}")]/../../div[2]/div/div/form'

    # 如果 row_index 和 label_index 有值，动态生成路径
    if row_index is not None and label_index is not None:
        notification_method = f'/div[3]/div/table/tbody/tr[{row_index}]/td[2]/div/div/label[{label_index}]/span[1]'

    return {
        'path': f'{base_xpath}{notification_method}',
        'msg': msg
    }
#调用后的样例如下
# Web_Method_Failed_All = {
#     'path': '//span[@class="trigger-title"][contains(text(),"页面执行")]'
#             '/../../div[2]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/div/label/span[1]',
#     'msg': '页面执行=>通知方式=>执行失败=>全选'
# }

#页面执行
# 操作类型
Web_Type_QuickScript = get_xpath('页面执行', '/div[1]/div/div/label[1]/span[1]', '页面执行=>操作类型=>快速执行脚本')
Web_Type_QuickFile = get_xpath('页面执行', '/div[1]/div/div/label[2]/span[1]', '页面执行=>操作类型=>快速文件分发')
Web_Type_Plan = get_xpath('页面执行', '/div[1]/div/div/label[3]/span[1]', '页面执行=>操作类型=>执行方案')

# 通知方式 - 执行成功
Web_Method_Succeed_WeChat = get_xpath('页面执行', None, '页面执行=>通知方式=>执行成功=>微信', row_index=1, label_index=1)
Web_Method_Succeed_SMS = get_xpath('页面执行', None, '页面执行=>通知方式=>执行成功=>短信', row_index=1, label_index=3)
Web_Method_Succeed_Email = get_xpath('页面执行', None, '页面执行=>通知方式=>执行成功=>邮件', row_index=1, label_index=2)
Web_Method_Succeed_Voice = get_xpath('页面执行', None, '页面执行=>通知方式=>执行成功=>语音', row_index=1, label_index=4)

# 通知方式 - 执行失败
Web_Method_Failed_WeChat = get_xpath('页面执行', None, '页面执行=>通知方式=>执行失败=>微信', row_index=2, label_index=1)
Web_Method_Failed_SMS = get_xpath('页面执行', None, '页面执行=>通知方式=>执行失败=>短信', row_index=2, label_index=3)
Web_Method_Failed_Email = get_xpath('页面执行', None, '页面执行=>通知方式=>执行失败=>邮件', row_index=2, label_index=2)
Web_Method_Failed_Voice = get_xpath('页面执行', None, '页面执行=>通知方式=>执行失败=>语音', row_index=2, label_index=4)

#API 调用
# 操作类型
API_Type_QuickScript = get_xpath('API 调用', '/div[1]/div/div/label[1]/span[1]', 'API 调用=>操作类型=>快速执行脚本')
API_Type_QuickFile = get_xpath('API 调用', '/div[1]/div/div/label[2]/span[1]', 'API 调用=>操作类型=>快速文件分发')
API_Type_Plan = get_xpath('API 调用', '/div[1]/div/div/label[3]/span[1]', 'API 调用=>操作类型=>执行方案')

# 通知方式 - 执行成功
API_Method_Succeed_WeChat = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行成功=>微信', row_index=1, label_index=1)
API_Method_Succeed_SMS = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行成功=>短信', row_index=1, label_index=3)
API_Method_Succeed_Email = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行成功=>邮件', row_index=1, label_index=2)
API_Method_Succeed_Voice = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行成功=>语音', row_index=1, label_index=4)

# 通知方式 - 执行失败
API_Method_Failed_WeChat = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行失败=>微信', row_index=2, label_index=1)
API_Method_Failed_SMS = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行失败=>短信', row_index=2, label_index=3)
API_Method_Failed_Email = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行失败=>邮件', row_index=2, label_index=2)
API_Method_Failed_Voice = get_xpath('API 调用', None, 'API 调用=>通知方式=>执行失败=>语音', row_index=2, label_index=4)

#定时任务
# 操作类型
Cron_Type_QuickScript = get_xpath('定时任务', '/div[1]/div/div/label[1]/span[1]', '定时任务=>操作类型=>快速执行脚本')
Cron_Type_QuickFile = get_xpath('定时任务', '/div[1]/div/div/label[2]/span[1]', '定时任务=>操作类型=>快速文件分发')
Cron_Type_Plan = get_xpath('定时任务', '/div[1]/div/div/label[3]/span[1]', '定时任务=>操作类型=>执行方案')

# 通知方式 - 执行成功
Cron_Method_Succeed_WeChat = get_xpath('定时任务', None, '定时任务=>通知方式=>执行成功=>微信', row_index=1, label_index=1)
Cron_Method_Succeed_SMS = get_xpath('定时任务', None, '定时任务=>通知方式=>执行成功=>短信', row_index=1, label_index=3)
Cron_Method_Succeed_Email = get_xpath('定时任务', None, '定时任务=>通知方式=>执行成功=>邮件', row_index=1, label_index=2)
Cron_Method_Succeed_Voice = get_xpath('定时任务', None, '定时任务=>通知方式=>执行成功=>语音', row_index=1, label_index=4)

# 通知方式 - 执行失败
Cron_Method_Failed_WeChat = get_xpath('定时任务', None, '定时任务=>通知方式=>执行失败=>微信', row_index=2, label_index=1)
Cron_Method_Failed_SMS = get_xpath('定时任务', None, '定时任务=>通知方式=>执行失败=>短信', row_index=2, label_index=3)
Cron_Method_Failed_Email = get_xpath('定时任务', None, '定时任务=>通知方式=>执行失败=>邮件', row_index=2, label_index=2)
Cron_Method_Failed_Voice = get_xpath('定时任务', None, '定时任务=>通知方式=>执行失败=>语音', row_index=2, label_index=4)

# 定义需要点击的元素列表
web_notify_elements = [
    Web_Type_QuickScript,
    Web_Type_QuickFile,
    Web_Type_Plan,
    Web_Method_Succeed_WeChat,
    Web_Method_Succeed_SMS,
    Web_Method_Succeed_Email,
    Web_Method_Succeed_Voice,
    Web_Method_Failed_WeChat,
    Web_Method_Failed_SMS,
    Web_Method_Failed_Email,
    Web_Method_Failed_Voice
]

API_notify_elements = [
    API_Type_QuickScript,
    API_Type_QuickFile,
    API_Type_Plan,
    API_Method_Succeed_WeChat,
    API_Method_Succeed_SMS,
    API_Method_Succeed_Email,
    API_Method_Succeed_Voice,
    API_Method_Failed_WeChat,
    API_Method_Failed_SMS,
    API_Method_Failed_Email,
    API_Method_Failed_Voice
]

Cron_notify_elements = [
    Cron_Type_QuickScript,
    Cron_Type_QuickFile,
    Cron_Type_Plan,
    Cron_Method_Succeed_WeChat,
    Cron_Method_Succeed_SMS,
    Cron_Method_Succeed_Email,
    Cron_Method_Succeed_Voice,
    Cron_Method_Failed_WeChat,
    Cron_Method_Failed_SMS,
    Cron_Method_Failed_Email,
    Cron_Method_Failed_Voice
]

# 页面执行

Web_Method_Failed_All = {
    'path': '//span[@class="trigger-title"][contains(text(),"页面执行")]'
            '/../../div[2]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/div/label/span[1]',
    'msg': '页面执行=>通知方式=>执行失败=>全选'
}


# API 调用

API_Method_Failed_All = {
    'path': '//span[@class="trigger-title"][contains(text(),"API 调用")]'
            '/../../div[2]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/div/label/span[1]',
    'msg': 'API 调用=>通知方式=>执行失败=>全选'
}


# 定时任务

Cron_Method_Succeed_All = {
    'path': '//span[@class="trigger-title"][contains(text(),"定时任务")]'
            '/../../div[2]/div/div/form/div[3]/div/table/tbody/tr[1]/td[2]/div/label/span[1]',
    'msg': '定时任务=>通知方式=>执行成功=>全选'
}


Cron_Method_Failed_All = {
    'path': '//span[@class="trigger-title"][contains(text(),"定时任务")]'
            '/../../div[2]/div/div/form/div[3]/div/table/tbody/tr[2]/td[2]/div/label/span[1]',
    'msg': '定时任务=>通知方式=>执行失败=>全选'
}



#按钮

Save_Button = {
    'path': '//button[@class="w120 mr10 bk-primary bk-button-normal bk-button"]',
    'msg': '消息通知=>保存按钮'
}

Default_Button = {
    'path': '//button[@class="bk-default bk-button-normal bk-button"]',
    'msg': '消息通知=>重置按钮'
}