import seldom
from product_page.bk_job import home
from product_page.bk_job import navigation
from product_page import settings
from public_method.base_operate import BaseOperate
from ..page.job_public_method import JobMethod


BaseOperate = BaseOperate()


# IP 白名单
class CreatewhiteIp(JobMethod):
    '''创建IP白名单'''
    def test_01_createwhiteIp(self):
        '''创建IP白名单'''
        self._test_login(target_url=settings.JOB_URL, index_title=settings.INDEX_TITLE)
        self.max_window()
        # 登录态验证
        self.switch_to_window(0)
        self.my_click(element=home.navigation_publicScriptList)
        self.my_click(element=home.navigation_whiteIp)
        #进入IP白名单界面
        self.sleep(2)
        self.my_click(element=navigation.append_button)
        self.CreateWhiteIPScope(White_Usage_Scope='business')
        #business为单个业务,all为全业务
        self.CreateWhiteIPScopeType(White_Usage_Scope_Type='all')
        #execution为脚本执行,files为文件分发,all为两个都勾选
        self.my_click(element=navigation.submit_button)


