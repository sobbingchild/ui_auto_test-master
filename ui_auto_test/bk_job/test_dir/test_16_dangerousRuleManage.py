import seldom
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page import settings
from public_method.base_operate import BaseOperate
from ..page.job_public_method import JobMethod
from product_page.bk_job import ruleManage

BaseOperate = BaseOperate()


# 新增高危语句规则
class CreatedangerousRuleManage(JobMethod):
    '''创建IP白名单'''
    def test_01_createdangerousRuleManage(self):
        '''创建IP白名单'''
        self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        self.max_window()
        # 登录态验证
        self.switch_to_window(0)
        self.my_click(element=home.navigation_publicScriptList)
        self.my_click(element=home.navigation_dangerousRuleManage)
        #进入高危语句规则界面
        self.sleep(2)
        self.my_click(element=navigation.append_button)
        self.my_type(element=ruleManage.Syntax_detection_expression, text=ruleManage.Rule_text)
        self.my_type(element=ruleManage.Rule_description, text=ruleManage.Description_text)
        self.EditRuleUsage(Rule_Script_Type="all")
        #输入 all为全选, bat为bat类型, shell为shell类型
        self.EditActionUsage(Rule_Action_Type="scan")
        #输入 scan为扫描, intercept为拦截
        self.my_click(element=ruleManage.Save_button)

