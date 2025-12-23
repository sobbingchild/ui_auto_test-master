# -*- coding: utf-8 -*-

from public_method.login import LoginBase
from product_page.bk_job import navigation
from product_page.bk_job import whiteIp
from product_page.bk_job import notify
from product_page.bk_job import home
from product_page.public_components import ip_choose
from product_page.bk_job import quick_excute_scripts
from product_page.bk_job import ruleManage
from product_page.bk_job import globalSetting
class JobMethod(LoginBase):

    def CreateScript(self, Script_Type, Script_Usage_Scope):
        # 根据Script_Usage_Scope选择对应的元素
        if Script_Usage_Scope == "business":
            script_elements = {
                "python": navigation.python_click,
                "perl": navigation.perl_click,
                "powershell": navigation.powershell_click
            }
        elif Script_Usage_Scope == "public":
            script_elements = {
                "python": navigation.public_python_click,
                "perl": navigation.public_perl_click,
                "powershell": navigation.public_powershell_click
            }
        else:
            raise ValueError("Invalid Script_Usage_Scope")
        # 根据Script_Type选择对应的脚本内容
        script_texts = {
            "python": navigation.PYTHON_SCRIPT_TEXT,
            "perl": navigation.PERL_SCRIPT_TEXT,
            "powershell": navigation.POWERSHELL_SCRIPT_TEXT
        }
        # 获取对应的元素和脚本内容
        script_element = script_elements.get(Script_Type)
        script_text = script_texts.get(Script_Type)

        if script_element is None or script_text is None:
            raise ValueError("Invalid Script_Type")
        # 点击对应的脚本类型并输入脚本内容
        self.my_click(element=script_element)
        self.my_type(element=navigation.script_content, text=script_text)
        # 点击提交
        self.my_click(element=navigation.submit_button)
        # 断言是否跳转到版本管理
        self.assertText(navigation.PAGE_TEXT)
        # 断言新建脚本状态
        self.assertText("未上线")

    def AssertScriptText(self, Script_Type):
        # 使用字典映射 Script_Type 和对应的脚本文本
        script_texts = {
            "python": navigation.PYTHON_SCRIPT_TEXT,
            "perl": navigation.PERL_SCRIPT_TEXT,
            "powershell": navigation.POWERSHELL_SCRIPT_TEXT
        }
        # 获取对应的脚本文本
        script_text = script_texts.get(Script_Type)
        # 如果 Script_Type 无效，抛出异常
        if script_text is None:
            raise ValueError(f"Invalid Script_Type: {Script_Type}")
        # 断言脚本文本
        self.assertText(script_text)
    def AssertScriptOnline(self, Script_Type):
        # 使用字典映射 Script_Type 和对应的脚本文本
        script_texts = {
            "python": navigation.PYTHON_SCRIPT_TEXT,
            "perl": navigation.PERL_SCRIPT_TEXT,
            "powershell": navigation.POWERSHELL_SCRIPT_TEXT
        }
        # 获取对应的脚本文本
        script_text = script_texts.get(Script_Type)
        # 如果 Script_Type 无效，抛出异常
        if script_text is None:
            raise ValueError(f"Invalid Script_Type: {Script_Type}")
        # 断言脚本文本
        self.assertText(script_text)
        # 点击上线提示按钮
        self.my_click(element=navigation.online_alert_button)
        # 断言上线提示文案
        self._assert_online_alert_text()
        # 点击确定上线
        self.my_click(element=navigation.online_button)
        # 检查脚本状态
        self.assertText("已上线")
        self.close()
    def _assert_online_alert_text(self):
        """断言上线提示文案是否正确"""
        self.sleep(1)
        online_alert_text = self.my_get_text(element=navigation.online_alert_text)
        assert online_alert_text == navigation.ONLINE_ALERT_TEXT
    def ScriptDebug(self):
        try:
            if self.my_get_elements(element=home.scroll_bar):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=quick_excute_scripts.choose_hosts)
        self.assertText(navigation.PAGE_AGENT_STATE)
        self.my_click(element=ip_choose.choose_agent)
        self.my_click(element=ip_choose.choose_host_confirm)
        self.my_click(element=navigation.debug_run)
        self.sleep(3)
        self.assertText(navigation.RUN_STATE)
        # 关闭跳转的选项卡
        print('调试成功')

    def ManageNotify(self, Notify_Type):
        if Notify_Type == 'Web':
            for element in notify.web_notify_elements:
                self.my_click(element=element)
        if Notify_Type=='API':
            for element in notify.API_notify_elements:
                self.my_click(element=element)
        if Notify_Type=='Cron':
            for element in notify.Cron_notify_elements:
                self.my_click(element=element)
    def ManageNotify_Button(self, Button_Type):
        if Button_Type=='Save':
            self.my_click(element=notify.Save_Button)
        if Button_Type=='Default':
            self.my_click(element=notify.Default_Button)


    def CreateWhiteIPScope(self,White_Usage_Scope ):
        self.my_click(element=navigation.append_button)

        if White_Usage_Scope == "business":
            self.my_click(element=whiteIp.select_biz)
            self.my_click(element=whiteIp.input_biz)
        if White_Usage_Scope == "all":
            self.my_click(element=whiteIp.all_biz)
        self.my_click(element=navigation.append_button)
        #关闭下拉框
        self.my_click(element=whiteIp.whiteIp_choose_hosts)
        self.my_click(element=whiteIp.whiteIp_choose_agent)
        self.my_click(element=whiteIp.whiteIp_choose_host_confirm)
        self.my_type(element=whiteIp.input_remark, text=whiteIp.remark_text)

    def CreateWhiteIPScopeType(self,White_Usage_Scope_Type):
        if White_Usage_Scope_Type == 'execution':
            self.my_click(element=whiteIp.effective_range_execution)
        if White_Usage_Scope_Type == 'files':
            self.my_click(element=whiteIp.effective_range_files)
        if White_Usage_Scope_Type == 'all':
            self.my_click(element=whiteIp.effective_range_execution)
            self.my_click(element=whiteIp.effective_range_files)

    def EditRuleUsage(self, Rule_Script_Type):
        self.my_click(element=ruleManage.Script_type)
        if Rule_Script_Type == 'all':
            self.my_click(element=ruleManage.Type_all)
        if Rule_Script_Type == 'bat':
            self.my_click(element=ruleManage.Type_bat)
        if Rule_Script_Type == 'shell':
            self.my_click(element=ruleManage.Type_shell)
        self.my_click(element=ruleManage.Script_type)
        #关闭下拉框

    def EditActionUsage(self,Rule_Action_Type):
        self.my_click(element=ruleManage.Action)
        if Rule_Action_Type == 'scan':
            self.my_click(element=ruleManage.Action_Type_Scan)
        if Rule_Action_Type == 'intercept':
            self.my_click(element=ruleManage.Action_Type_Intercept)
        self.my_click(element=ruleManage.Action)
        # 关闭下拉框


    #全局配置
    def AssertChanelStatus(self, Chanel_Type):
        channel_mapping = {
            '微信': (globalSetting.chanel_wechat_false, globalSetting.chanel_wechat),
            '邮件': (globalSetting.chanel_mail_false, globalSetting.chanel_mail),
            '短信': (globalSetting.chanel_msg_false, globalSetting.chanel_msg),
            '语音': (globalSetting.chanel_voice_false, globalSetting.chanel_voice),
        }

        if Chanel_Type in channel_mapping:
            disabled_element, enable_element = channel_mapping[Chanel_Type]
            try:
                self.my_get_elements(element=disabled_element)
                # 判断通道是否被禁用, 若已经禁用则开启
                self.my_click(element=enable_element)
            except Exception as e:
                print(f"{Chanel_Type}通道已开启, 无需再开启")
        else:
            print(f"未知通道类型: {Chanel_Type}")

    def edit_template(self, template_type, channel_type):
        # 定义模板类型和通道类型的映射关系
        template_mapping = {
            "人工确认": {
                "微信": {
                    "unset": globalSetting.manual_wechat_unset,
                    "click": globalSetting.click_manual_wechat,
                    "set": globalSetting.manual_wechat_set
                },
                "邮件": {
                    "unset": globalSetting.manual_mail_unset,
                    "click": globalSetting.click_manual_mail,
                    "set": globalSetting.manual_mail_set
                },
                "短信": {
                    "unset": globalSetting.manual_msg_unset,
                    "click": globalSetting.click_manual_msg,
                    "set": globalSetting.manual_msg_set
                },
                "语音": {
                    "unset": globalSetting.manual_voice_unset,
                    "click": globalSetting.click_manual_voice,
                    "set": globalSetting.manual_voice_set
                }
            },
            "执行成功": {
                "微信": {
                    "unset": globalSetting.executed_success_wechat_unset,
                    "click": globalSetting.click_executed_success_wechat,
                    "set": globalSetting.executed_success_wechat_set
                },
                "邮件": {
                    "unset": globalSetting.executed_success_mail_unset,
                    "click": globalSetting.click_executed_success_mail,
                    "set": globalSetting.executed_success_mail_set
                }
            }
        }

        try:
            # 获取对应模板类型和通道类型的元素
            elements = template_mapping[template_type][channel_type]
            unset_element = elements["unset"]
            click_element = elements["click"]
            set_element = elements["set"]

            # 尝试处理未设置状态的模板
            if self.try_edit_template(unset_element, click_element):
                print("该模板已被设置")
            # 尝试处理已设置状态的模板
            elif self.try_edit_template(set_element, click_element):
                print("该模板未被设置")
            else:
                print("无法找到模板元素")

            # 输入模板内容并保存
            self.my_type(element=globalSetting.template_content, text=globalSetting.template_content_text)
            self.my_click(element=globalSetting.template_save_button)
        except KeyError as e:
            print(f"未找到该元素: {e}")

    def try_edit_template(self, element, click_element):
        try:
            # 默认选择未设置状态
            self.my_get_elements(element=element)
            # 鼠标悬置，显示编辑模板按钮
            self.my_move_to_element(element=element)
            # 点击编辑模板按钮
            self.my_click(element=click_element)
            return True
        except Exception as e:
            return False

    # 示例调用
    # self.edit_template(template_type="人工确认", channel_type="微信")
    # self.edit_template(template_type="执行成功", channel_type="邮件")
    def EditAccountRules(self, account_type):
        # 定义账户类型与对应元素的映射关系
        account_mapping = {
            'Linux': {
                'expression': globalSetting.Linux_expression,
                'expression_text': globalSetting.Linux_expression_text,
                'rule': globalSetting.Linux_rule,
                'rule_text': globalSetting.Linux_rule_text,
                'default_button': globalSetting.Linux_default_button
            },
            'Windows': {
                'expression': globalSetting.Windows_expression,
                'expression_text': globalSetting.Windows_expression_text,
                'rule': globalSetting.Windows_rule,
                'rule_text': globalSetting.Windows_rule_text,
                'default_button': globalSetting.Windows_default_button
            },
            'Database': {
                'expression': globalSetting.Database_expression,
                'expression_text': globalSetting.Database_expression_text,
                'rule': globalSetting.Database_rule,
                'rule_text': globalSetting.Database_rule_text,
                'default_button': globalSetting.Database_default_button
            }
        }

        # 获取对应账户类型的配置
        account_config = account_mapping.get(account_type)
        if not account_config:
            raise ValueError(f"未知的账户类型: {account_type}")

        # 输入表达式和规则，并点击默认按钮
        self._input_and_click(account_config['expression'], account_config['expression_text'])
        self._input_and_click(account_config['rule'], account_config['rule_text'])
        self.my_click(element=account_config['default_button'])

    def SubmitAccountRules(self, button_type):
        # 定义按钮类型与对应元素的映射关系
        button_mapping = {
            'save': globalSetting.save_button,
            'reset': globalSetting.reset_button
        }

        # 获取对应按钮类型的元素
        button_element = button_mapping.get(button_type)
        if not button_element:
            raise ValueError(f"未知的按钮类型: {button_type}")

        # 点击按钮
        self.my_click(element=button_element)

    def _input_and_click(self, element, text):
        """
        通用的输入文本并点击元素的方法
        """
        self.my_type(element=element, text=text)