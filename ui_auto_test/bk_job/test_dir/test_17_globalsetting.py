import seldom
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page.bk_job import globalSetting
from product_page import settings
from public_method.base_operate import BaseOperate
from ..page.job_public_method import JobMethod
from ..page.job_public_method import TemplateEditor
BaseOperate = BaseOperate()


# 全局配置=>通道判断是否开启,模板编辑
class EditGlobalSetting(JobMethod):
    '''全局配置'''
    def test_01_AssertChanelStatus(self):
        '''判断并开启全局配置通道'''
        self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        self.max_window()
        # 登录态验证
        self.switch_to_window(0)
        self.my_click(element=home.navigation_publicScriptList)
        self.my_click(element=home.navigation_globalSetting)
        self.AssertChanelStatus(Chanel_Type="微信")
        self.my_click(element=globalSetting.save_button)

    def test_02_EditTemplate(self):
        '''编辑消息通知模板'''
        self.edit_template(template_type="人工确认",channel_type="微信")
        # self.my_click(element=globalSetting.wechat_manual)

        # self.my_click(element=globalSetting.template_reset_button)
        # self.my_click(element=globalSetting.template_save_button)

    def test_03_EditAccountRules(self):
        '''账号命名规则'''
        self.EditAccountRules(account_type="Linux")
        self.SubmitAccountRules(button_type="reset")

