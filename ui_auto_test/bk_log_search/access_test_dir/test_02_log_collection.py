from time import sleep
import seldom

from bk_log_search.access_test_dir import test_01_login
from bk_log_search.page import management


from bk_job.page import file_transfer as page
from pre_data.job_api_demo import JobApi
from bk_job.bk_exception import ApiError
from pre_data.obtain_token import ObtainToken
from public_method.keyboard_operation import MyWebDriver
api = JobApi()


class Log_Collection_Create(seldom.TestCase):
    def test_01_create_log_collection(self):
        """新建采集项"""
        # 进入首页

        linux_ip_list = api.get_hosts_ip()
        if linux_ip_list and len(linux_ip_list) >= 2:
            page.centos_1, page.centos_2 = linux_ip_list[0], linux_ip_list[1]
            print(page.centos_1)
            print(page.centos_2)
        else:
            ApiError('获取IP数量不符合预期，分发文件失败')


        self.sleep(100)
        test_01_login.Login.test_login(self)
        # 点击管理
        self.click(xpath=management.management)
        # 点击新建采集项
        self.click(xpath=management.create_log_collection)
        # 新建采集配置名称
        self.is_visible(5, xpath=management.log_collection_name)
        self.type(xpath=management.log_collection_name, text=management.log_collection_name_Chinese)
        # 新建英文名
        self.type(xpath=management.log_collection_name_English,
                  text=management.log_collection_name_fillEnglishName + ObtainToken.random_data(self))
        # 点击数据分类
        self.click(xpath=management.selectDataClassification)
        # 选择主机设备
        self.click(xpath=management.host_devices)
        # 选择目标
        self.click(xpath=management.addCollectionTarget)
        sleep(3)
        # 点击手动输入
        self.click(xpath=management.selfdefined_input)
        # 点击输入框
        self.click(xpath=management.input_box)
        # 输入从job获取的IP
        linux_ip_list = api.get_hosts_ip()
        if linux_ip_list and len(linux_ip_list) >= 2:
            page.centos_1, page.centos_2 = linux_ip_list[0], linux_ip_list[1]
            print(page.centos_1)
            print(page.centos_2)
        else:
            ApiError('获取IP数量不符合预期，分发文件失败')
        self.type(xpath=management.input_box, text=page.centos_1)
        # 点击解析，判断Agent状态是否正常
        self.click(xpath=management.analysis)
        self.assertText(management.assert_status)
        sleep(3)
        # 确定
        self.click(xpath=management.confirm)
        # 填写日志路径
        self.type(xpath=management.logpath, text=management.logpath_name)
        # 下一步
        self.click(xpath=management.nextPage)
        # 下一步
        sleep(85)
        self.click(xpath=management.nextStep)
        # 点击分隔符
        self.click(xpath=management.separator)
        # 点击请选择
        self.click(xpath=management.please_select)
        # 点击竖线
        self.click(xpath=management.long_string)
        # 点击调试
        self.click(xpath=management.debug)
        # 分别点击隐藏
        self.click(xpath=management.conceal_first)
        self.click(xpath=management.conceal_second)
        self.click(xpath=management.conceal_thirdly)
        self.click(xpath=management.conceal_fourthly)
        # 字段名输入test
        self.type(xpath=management.field_name,text='test')
        # 下一步
        self.click(xpath=management.button_nextPage)
        # 默认选择第一个集群
        self.click(xpath=management.cluster)
        # 点击完成
        self.click(xpath=management.accomplish)
        # 断言是否创建采集项成功
        self.assertText(management.assert_create_success)

    def test_02_search(self):
        """判断检索功能是否有效"""
        # 防止无法采集到数据，添加等待时间
        sleep(120)
        # 点击管理
        self.click(xpath=management.management)
        # 搜索框搜索采集项名称
        self.type(xpath=management.search_name,text=management.log_collection_name_Chinese)
        MyWebDriver.Keys(xpath=management.search_name).enter()
        # 点击编辑
        self.click(xpath=management.edit)
        # 下一步
        self.click(xpath=management.nextPage)
        sleep(3)
        # 下一步
        self.click(xpath=management.nextStep)
        # 下一步
        self.click(xpath=management.button_nextPage)
        # 点击完成
        self.click(xpath=management.accomplish)
        # 点击返回列表
        self.click(xpath=management.button_backToList)
        sleep(60)
        # 点击检索
        self.click(xpath=management.search)
        sleep(5)
        # 点击原始
        self.click(xpath=management.original)
        # 断言
        self.assertText(management.assert_message)

    def test_03_delete_log_collection(self):
        """停用采集项、删除采集项"""
        # 点击管理
        self.click(xpath=management.management)
        # 点击更多停用
        self.click(xpath=management.more)
        self.move_to_element(xpath=management.block_up)
        self.click(xpath=management.block_up)
        # 跳转到停用界面
        sleep(5)
        self.click(xpath=management.sure_block_up)
        # 断言
        self.assertText(management.assert_block_up)
        # 点击管理
        self.click(xpath=management.management)
        # 删除
        sleep(45)
        self.click(xpath=management.more)
        self.move_to_element(xpath=management.delete_log_collection)
        self.click(xpath=management.delete_log_collection)
        # 确认删除
        self.click(xpath=management.sure_delete_log_collection)
