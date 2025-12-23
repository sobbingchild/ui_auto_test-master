
import bk_itsm.settings as settings
project="//a[@data-test-id='navigation-router-navRouter-project']"
#这个定位需要修改
service="//a[@data-test-id='navigation-menu-projectServiceList']"
new_service="//button[@data-test-id='service_button_createService']"
service_name= '//div[@class="bk-dialog-wrapper"]/div/div/div[3]/form/div[1]/div/div/div[1]/input'
service_dir="//div[@data-test-id='service-select-serviceDirectory']/div/div/div/span"
choose_service_dir="//div[@data-test-id='service-select-serviceDirectory']//ul/li[4]"

service_type="//div[@data-test-id='service-select-serviceType']/div"
#这个定位需要修改
choose_service_type="//div[@class='bk-select-dropdown-content']//ul/li[1]  "

comfirm_service='//div[@class="bk-dialog-wrapper"]/div/div/div[4]/div/button[1]'

service_temp=   '//div[@class="service-template"]/div[1]'
choose_service_temp="//div[@class='dialog-body']/ul/li/p[contains(.,'默认')]"
service_next="//button[@data-test-id='service_button_nextStepAndSave']"
flow_next="//button[@data-test-id='service_button_nextStepAndSave']"
flow_commit="//button[@data-test-id='service_button_nextStepAndSave']"
#这个定位需要修改
commit_tickets="//div[@class='nav-header']/button//span"
service_instance="//ul[@class='service-content']/li/div[contains(.,'{}')]".format(settings.SERVICE_NAME_DEFAULT_FLOW_CHANGE)

cancel="//div[@class='footer-wrapper']/button[@name='cancel']"
