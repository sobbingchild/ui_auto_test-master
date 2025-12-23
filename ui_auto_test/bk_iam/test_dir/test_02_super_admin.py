import seldom
from bk_iam.page import super_admin as page
from bk_iam import settings as settings
import time


class superAdmin(seldom.TestCase):

    def test_00_init(self):
        self.click(xpath=page.right_username)
        self.click(xpath=page.iam_login_out)
        time.sleep(3)
        self.login(settings.USER_NAME, settings.PASSWORD)
        self.click(xpath=page.right_username)
        self.click(xpath=page.search_id)
        self.type(xpath=page.search_id, text=page.super_admin)
        self.click(xpath=page.search_admin)

    def test_01_add_model(self):
        """"添加模板"""
        self.click(xpath=page.nav_permi_temp)
        time.sleep(2)
        self.click(xpath=page.new_perm_temp)
        time.sleep(2)
        self.type(xpath=page.temp_name_input, text=page.temp_name)
        self.click(xpath=page.check_dev)
        self.click(xpath=page.temp_commit)
        time.sleep(2)

    def test_02_add_usermg(self):
        """"添加用户组-组织架构"""
        self.click(xpath=page.nav_usermg)
        time.sleep(2)
        self.click(xpath=page.new_usermg)
        time.sleep(2)
        self.type(xpath=page.usermg_name_input, text=page.user_name)
        self.type(xpath=page.usermg_desc_input, text=page.user_desc)
        # 添加组权限
        self.wait(2)
        self.click(xpath=page.add_perm_g)
        self.click(xpath=page.check_temp_name)
        self.click(xpath=page.user_perm_commit)
        # 添加组成员
        self.wait(2)
        self.click(xpath=page.add_user_g)
        self.click(xpath=page.def_dir)
        self.click(xpath=page.user_g_check, index=1)
        self.click(xpath=page.user_g_confirm)
        self.wait(2)
        # 用户组提交
        self.click(xpath=page.usermg_commit)
        self.wait(2)

    def test_03_add_usermg(self):
        """"添加用户组-单用户"""
        self.click(xpath=page.nav_usermg)
        time.sleep(2)
        self.click(xpath=page.new_usermg)
        time.sleep(2)
        self.type(xpath=page.usermg_name_input, text=page.single_user_gname)
        self.type(xpath=page.usermg_desc_input, text=page.user_desc)
        # 添加组权限
        self.wait(2)
        self.click(xpath=page.add_perm_g)
        self.click(xpath=page.check_temp_name)
        self.click(xpath=page.user_perm_commit)
        # 添加组成员
        self.wait(2)
        self.click(xpath=page.add_user_g)
        self.click(xpath=page.button_input_menber)
        self.click(xpath=page.input_erea)
        self.type(xpath=page.input_erea, text=page.admin)
        self.click(xpath=page.button_add_menber)
        self.wait(2)
        # 用户组提交
        self.click(xpath=page.button_comfirm)
        self.wait(2)

        '''
        分级管理员创建了之后无法删除，不建议加入自动化，先注释
        '''

    # def test_04_add_rating_man(self):
    #     """"添加分级管理员"""
    #     self.click(xpath=page.nav_rating_manager)
    #     self.click(xpath=page.new_rating_manager)
    #     self.click(xpath=page.name_rating_manager)
    #     ranting_name= page.rating_man_name(page.test_ui_rating_name)
    #     print("分级管理员名称--",ranting_name)
    #     self.type(xpath=page.name_rating_manager, text=ranting_name)
    #     self.click(xpath=page.range_action)
    #     self.click(xpath=page.select_visit)
    #     self.click(xpath=page.select_dev)
    #     self.click(xpath=page.select_manager)
    #     self.click(xpath=page.action_man)
    #     self.click(xpath=page.man_app)
    #     self.click(xpath=page.no_limit)
    #     self.click(xpath=page.save_source)
    #     self.click(xpath=page.button_commit)

    '''需要优化，当前的逻辑适合在已经有系统管理员的情况下用'''

    # def test_05_add_sys_admin(self):
    #     """添加系统管理员"""
    #     self.click(xpath=page.nav_admin)
    #     self.click(xpath=page.sys_man)
    #     self.move_to_element(xpath=page.paas_menber)
    #     text = self.get_text(xpath=page.paas_menber)
    #     print("系统管理员获取到了啥", text)
    #     self.click(xpath=page.paas_menber_hover)
    #     text2 = self.get_text(xpath=page.paas_menber_hover)
    #     print("系统管理员点击之后获取到了啥", text2)
    #
    #     if self.assertIsNone(text):
    #         self.type(xpath=page.paas_menber_selector_span, text=page.admin)
    #         time.sleep(2)
    #         self.Keys(xpath=page.paas_menber_selector_span).enter()
    #         self.type(xpath=page.paas_menber_selector_span2, text=settings.NEW_USER)
    #         time.sleep(2)
    #         self.Keys(xpath=page.paas_menber_selector_span2).enter()
    #     else:
    #         self.type(xpath=page.paas_menber_selector_span2, text=settings.NEW_USER)
    #         time.sleep(2)
    #         self.Keys(xpath=page.paas_menber_selector_span2).enter()
    #
    #     self.type(xpath=page.paas_menber_selector_span2, text=settings.NEW_USER)
    #     time.sleep(2)
    #     self.Keys(xpath=page.paas_menber_selector_span2).enter()


    def login(self, username, pwd):
        try:
            # 输入账号
            self.type(xpath=page.account, text=username)
            # 输入密码
            self.type(xpath=page.password, text=pwd)
            self.click(xpath=page.login_btn)
            time.sleep(3)
            print("登录成功")
        except BaseException as e:
            print("登录失败", e)
