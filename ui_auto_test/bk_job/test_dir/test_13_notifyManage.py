from product_page.bk_job import home
from product_page import settings
from public_method.base_operate import BaseOperate
from bk_job.page.job_public_method import JobMethod
BaseOperate = BaseOperate()


class NotifyManage(JobMethod):
    '''消息通知页面'''
    def test_01_notifyManage(self):
        '''全部按钮都执行'''
        self.open(settings.JOB_URL)
        try:
            if self.my_get_elements(element=home.scroll_bar_left):
                self.my_drag_and_drop_by_offset(element=home.scroll_bar_left, x=0, y=200)
        except Exception as e:
            pass
        self.my_click(element=home.navigation_notifyManage)
        self.sleep(2)

        self.ManageNotify(Notify_Type='Web')
        #此处输入Web / API /Cron 分别执行"页面执行","API调用","定时任务"三种消息通知类型
        self.ManageNotify_Button(Button_Type='Save')
        #此处输入Save / Default 对应 "保存按钮" , "重置按钮"



