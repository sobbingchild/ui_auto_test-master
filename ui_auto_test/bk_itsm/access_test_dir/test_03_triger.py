
import seldom
import bk_itsm.page.triger as page
from bk_itsm.access_test_dir import test_01_login as login
import bk_itsm.settings as settings
from time import sleep
#触发器：创建单据，关闭单据，终止单据，挂起单据，恢复单据，
#       进入节点，离开节点，分派单据，认领单据，转单，
#       进入分支
#       创建任务之后，删除任务，执行任务之前，执行任务之后，完成任务之后
#部分完成
class Tirger(seldom.TestCase):
    def test_01_add_create_ticket_triger(self):
        '''新增触发器'''
        # 创建单据（单据信号），test_ui_create_ticket
        # login.Login.test_login(self)

        sleep(3)
        self.click(xpath=page.project)
        self.click(xpath=page.nav_triger)

        # self.click(xpath=page.add_triger_permis)
        try:
            self.click(xpath=page.add_triger_permis)
        except Exception as e:
            print('已经存在触发器')
        try:
            self.click(xpath=page.add_triger)
        except Exception as e:
            print('新增失败')
        self.type(xpath=page.triger_name,text=settings.TRIGGER_CREATE_TICKET)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_create)
        sleep(5)
        # self.Keys().space()
        # self.execute_script("arguments[0].scrollIntoView();", page.event_name)

        self.trigger_event()

    def test_02_into_node_triger(self):
        # 进入节点（节点信号），test_ui_into_nodes
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_INTO_NODES)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_inotes)
        self.trigger_event()

    def test_03_branch_line_triger(self):
        # 进入分支（线条信号），test_ui_into_branch
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_INTO_BRANCH)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_branch_line)
        self.trigger_event()

    def test_04_branch_task_triger(self):
        # 进入分支(线条信号)，test_ui_into_branch_task
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_BRANCH_TASK)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_branch_task)
        self.trigger_event()

    def test_05_out_node_triger(self):
        # 离开节点（节点信号），test_ui_out_nodes
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_OUT_NODES)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_onotes)
        self.trigger_event()

    def test_06_claim_ticket_triger(self):
        # 认领单据（节点信号），test_ui_claim_tickets
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_CLAIM_TICKETS)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_claim)
        self.trigger_event()

    def test_07_distribution_triger(self):
        # 分派单据（节点信号），test_ui_distribution
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_DISTRIBUTION)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_dis)
        self.trigger_event()

    def test_08_hang_triger(self):
        # 分派单据（节点信号），test_ui_hang
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_HANG)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_dis)
        self.trigger_event()

    def test_09_recover_triger(self):
        # 分派单据（节点信号），test_ui_recover
        self.click(xpath=page.add_triger)
        self.type(xpath=page.triger_name, text=settings.TRIGGER_RECOVER)
        self.click(xpath=page.triger_event)
        self.click(xpath=page.choose_triger_event_dis)
        self.trigger_event()

    def trigger_event(self):
        js= 'document.getElementsByClassName("bk-sideslider-content")[0].scrollTo(0,1000)'
        self.execute_script(js)
        self.click(xpath=page.event_name)
        self.click(xpath=page.choose_event_name)
        self.click(xpath=page.event_id, index=0)
        sleep(2)
        self.click(xpath=page.choose_event_id)
        self.click(xpath=page.event_id, index=1)
        sleep(2)
        self.click(xpath=page.choose_event_id2)
        self.click(xpath=page.triger_commit)
        self.assertText(page.assert_create_successful)
