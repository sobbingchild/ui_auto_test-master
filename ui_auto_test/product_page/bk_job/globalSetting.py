#实例
sample_chanel_wechat = {
    'path': '//p[@class="channel-name"][contains(text(),"微信")]/../../label',
    'msg': '微信渠道'
}


sample_chanel_wechat_false = {
    'path': '//p[@class="channel-name"][contains(text(),"微信")]/../../label/input[@value="false"]',
    'msg': '微信渠道=>禁用状态'
}

sample_chanel_wechat_true = {
    'path': '//p[@class="channel-name"][contains(text(),"微信")]/../../label/input[@value="true"]',
    'msg': '微信渠道=>启用状态'
}

"""封装消息通道类型"""
def create_channel_config(channel_type):
    """
    创建渠道基础配置
    :param channel_type: 渠道类型，如 '微信', '邮件', '短信', '语音'
    :return: 返回基础配置字典
    """
    return {
        'path': f'//p[@class="channel-name"][contains(text(),"{channel_type}")]/../../label',
        'msg': f'{channel_type}渠道'
    }

def create_channel_status_config(channel_type, status):
    """
    创建渠道状态配置
    :param channel_type: 渠道类型，如 '微信', '邮件', '短信', '语音'
    :param status: 渠道状态，如 'true', 'false'
    :return: 返回状态配置字典
    """
    status_text = '启用' if status == 'true' else '禁用'
    return {
        'path': f'//p[@class="channel-name"][contains(text(),"{channel_type}")]/../../label/input[@value="{status}"]',
        'msg': f'{channel_type}渠道=>{status_text}状态'
    }

# 渠道类型列表
channels = ['微信', '邮件', '短信', '语音']

# 生成基础配置
channel_configs = {f'chanel_{channel}': create_channel_config(channel) for channel in channels}

# 生成状态配置
status_configs = {}
for channel in channels:
    status_configs[f'chanel_{channel}_true'] = create_channel_status_config(channel, 'true')
    status_configs[f'chanel_{channel}_false'] = create_channel_status_config(channel, 'false')

# 合并所有配置
all_configs = {**channel_configs, **status_configs}

# 使用生成的配置
chanel_wechat = all_configs['chanel_微信']
chanel_mail = all_configs['chanel_邮件']
chanel_msg = all_configs['chanel_短信']
chanel_voice = all_configs['chanel_语音']

chanel_wechat_false = all_configs['chanel_微信_false']
chanel_wechat_true = all_configs['chanel_微信_true']
chanel_mail_false = all_configs['chanel_邮件_false']
chanel_mail_true = all_configs['chanel_邮件_true']
chanel_msg_false = all_configs['chanel_短信_false']
chanel_msg_true = all_configs['chanel_短信_true']
chanel_voice_false = all_configs['chanel_语音_false']
chanel_voice_true = all_configs['chanel_语音_true']



reset_button = {
    'path': '//span[contains(text(),"重置")]/../..',
    'msg': '重置按钮'
}

save_button = {
    'path': '//span[contains(text(),"保存")]/../..',
    'msg': '保存按钮'
}


wechat_manual = {
    'path': '//td[contains(text(),"人工确认")]/../td[2]/div/i',
    'msg': '微信=>人工确认'
}


"""微信示例"""
sample_manual_wechat_set = {
    'path': '//td[contains(text(),"人工确认")]/../td[2]/div/i[@class="setting-flag job-icon job-icon-check"]',
    'msg': '微信=>人工确认=>已设置'
}



template_content = {
    'path': '//textarea[@class="bk-form-textarea"]',
    'msg': '消息模板编辑=>模板内容'
}

template_content_text="Task Details: {{task.detail.url}}"

"""封装消息模板的操作按钮"""
def create_button_config(index, description):
    return {
        'path': f'//div[@class="jb-sideslider-footer"]/button[{index}]/div',
        'msg': f'消息模板编辑=>{description}按钮'
    }

# 使用函数生成按钮配置
template_save_button = create_button_config(1, '保存')
template_reset_button = create_button_config(2, '重置')
template_default_button = create_button_config(3, '默认')


class NotificationSettings:
    def __init__(self, notification_type, column_index):
        self.notification_type = notification_type
        self.column_index = column_index

    def get_set_path(self, label):
        return f'//td[contains(text(),"{label}")]/../td[{self.column_index}]/div/i[@class="setting-flag job-icon job-icon-check"]'

    def get_unset_path(self, label):
        return f'//td[contains(text(),"{label}")]/../td[{self.column_index}]/div/span[@class="un-set-up"]'

    def get_click_path(self, label):
        return f'//td[contains(text(),"{label}")]/../td[{self.column_index}]/div/span[@class="edit-btn"]'

    def get_set_msg(self, label):
        return f'{self.notification_type}=>{label}=>已设置'

    def get_unset_msg(self, label):
        return f'{self.notification_type}=>{label}=>未设置'

    def get_click_msg(self, label):
        return f'{self.notification_type}=>{label}=>编辑模板'

    def create_setting(self, label):
        return {
            'path': self.get_set_path(label),
            'msg': self.get_set_msg(label)
        }

    def create_unset(self, label):
        return {
            'path': self.get_unset_path(label),
            'msg': self.get_unset_msg(label)
        }

    def create_click(self, label):
        return {
            'path': self.get_click_path(label),
            'msg': self.get_click_msg(label)
        }


# 定义所有通知类型和对应的列索引
NOTIFICATION_CONFIG = {
    '微信': 2,
    '邮件': 3,
    '短信': 4,
    '语音': 5
}

# 定义所有操作标签
LABELS = [
    '人工确认', '执行成功', '执行失败', '定时执行前', '定时结束前', '定时启动失败'
]

# 生成所有通知类型的配置
notification_settings = {}
for notification_type, column_index in NOTIFICATION_CONFIG.items():
    settings = NotificationSettings(notification_type, column_index)
    notification_settings[notification_type] = {
        label: {
            'set': settings.create_setting(label),
            'unset': settings.create_unset(label),
            'click': settings.create_click(label)
        }
        for label in LABELS
    }

# 示例：获取微信的
# “人工确认”设置
manual_wechat_set = notification_settings['微信']['人工确认']['set']
manual_wechat_unset = notification_settings['微信']['人工确认']['unset']
click_manual_wechat = notification_settings['微信']['人工确认']['click']
#“执行成功”设置
executed_success_wechat_set = notification_settings['微信']['执行成功']['set']
executed_success_wechat_unset = notification_settings['微信']['执行成功']['unset']
click_executed_success_wechat = notification_settings['微信']['执行成功']['click']
#“执行失败”设置
executed_failed_wechat_set = notification_settings['微信']['执行失败']['set']
executed_failed_wechat_unset = notification_settings['微信']['执行失败']['unset']
click_executed_failed_wechat = notification_settings['微信']['执行失败']['click']
#“定时执行前”设置
before_cron_execute_wechat_set = notification_settings['微信']['定时执行前']['set']
before_cron_execute_wechat_unset = notification_settings['微信']['定时执行前']['unset']
click_before_cron_execute_wechat = notification_settings['微信']['定时执行前']['click']
#“定时结束前”设置
before_cron_end_wechat_set = notification_settings['微信']['定时结束前']['set']
before_cron_end_wechat_unset = notification_settings['微信']['定时结束前']['unset']
click_before_cron_end_wechat = notification_settings['微信']['定时结束前']['click']
#“定时启动失败”设置
cron_start_failed_wechat_set = notification_settings['微信']['定时启动失败']['set']
cron_start_failed_wechat_unset = notification_settings['微信']['定时启动失败']['unset']
click_cron_start_failed_wechat = notification_settings['微信']['定时启动失败']['click']



# 示例：获取邮件的
#“执行成功”设置
executed_success_mail_set = notification_settings['邮件']['执行成功']['set']
executed_success_mail_unset = notification_settings['邮件']['执行成功']['unset']
click_executed_success_mail = notification_settings['邮件']['执行成功']['click']
#“人工确认”设置
manual_mail_set = notification_settings['邮件']['人工确认']['set']
manual_mail_unset = notification_settings['邮件']['人工确认']['unset']
click_manual_mail = notification_settings['邮件']['人工确认']['click']

# 示例：获取短信的
#“定时执行前”设置
before_cron_execute_msg_set = notification_settings['短信']['定时执行前']['set']
before_cron_execute_msg_unset = notification_settings['短信']['定时执行前']['unset']
click_before_cron_execute_msg = notification_settings['短信']['定时执行前']['click']
#“人工确认”设置
manual_msg_set = notification_settings['短信']['人工确认']['set']
manual_msg_unset = notification_settings['短信']['人工确认']['unset']
click_manual_msg = notification_settings['短信']['人工确认']['click']

# 示例：获取语音的
#“定时启动失败”设置
cron_start_failed_voice_set = notification_settings['语音']['定时启动失败']['set']
cron_start_failed_voice_unset = notification_settings['语音']['定时启动失败']['unset']
click_cron_start_failed_voice = notification_settings['语音']['定时启动失败']['click']
#“人工确认”设置
manual_voice_set = notification_settings['语音']['人工确认']['set']
manual_voice_unset = notification_settings['语音']['人工确认']['unset']
click_manual_voice = notification_settings['语音']['人工确认']['click']




#账号命名规则
Linux_expression = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Linux 账号")]/../../div/div/div[1]/div/div[1]/input',
    'msg': 'Linux账号规则'
}

Linux_rule = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Linux 账号")]/../../div/div/div[2]/div/div[1]/input',
    'msg': 'Linux账号描述'
}

Linux_default_button = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Linux 账号")]/../../div/div/button',
    'msg': 'Linux账号恢复默认按钮'
}

Windows_expression = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Windows 账号")]/../../div/div/div[1]/div/div[1]/input',
    'msg': 'Windows账号规则'
}

Windows_rule = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Windows 账号")]/../../div/div/div[2]/div/div[1]/input',
    'msg': 'Windows账号描述'
}

Windows_default_button = {
    'path': '//span[@class="bk-label-text"][contains(text(),"Windows 账号")]/../../div/div/button',
    'msg': 'Windows账号恢复默认按钮'
}

Database_expression = {
    'path': '//span[@class="bk-label-text"][contains(text(),"数据库账号")]/../../div/div/div[1]/div/div[1]/input',
    'msg': '数据库账号规则'
}

Database_rule = {
    'path': '//span[@class="bk-label-text"][contains(text(),"数据库账号")]/../../div/div/div[2]/div/div[1]/input',
    'msg': '数据库账号描述'
}

Database_default_button = {
    'path': '//span[@class="bk-label-text"][contains(text(),"数据库账号")]/../../div/div/button',
    'msg': '数据库账号恢复默认按钮'
}

Linux_expression_text = '^[a-z_][a-z0-9_-]{1,31}$'
Linux_rule_text = '使用小写字母或 _ 开头，由 2-32 个英文字母、数字、_ 或 - 组成的字符'

Windows_expression_text = '^[a-æA-Æ0-9-]{1,32}$'
Windows_rule_text = '由1~32个大小写字母、数字或-组成的字符'

Database_expression_text = '^[a-zA-Z0-9\.\-\_]{1,16}$'
Database_rule_text = '由1~16个大小写字母 / 数字 / . / - / _ 组成的字符'


