import random
#点击网络
network = '//div[2]/ul/li[3]/div[1]/div/div/div[1]/div/i'
#新建模型
creat_model = '//div[1]/div[2]/ul/li[3]/div[1]/div/div/div[3]/ul/li[1]/span'
#模型名
model_name = '//div[2]/div/div/div[2]/label[2]/div/div/div[1]/input'
#唯一标识
unique = '//div[2]/div/div/div[2]/label[1]/div/div/div[1]/input'
#提交模型信息
commit_model_message='//div[@class="model-dialog dialog bk-dialog-no-padding v-transfer-dom"]/div/div/div/div[3]/div/button[1]/div/span'
#断言新建模型
asserttext = "模型创建成功"
# 随机新建模型唯一标识/模型名称
alphabet = 'abcdefghijklmnopqrstuvwxyz'
char = random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(alphabet) + random.choice(
            alphabet)
#模型的唯一标识
model_unique_text = f"test_{char}"
#模型名
model_name_text = f"测试模型_{char}"
#搜索框搜索模型名
search_model = '//input[@placeholder="请输入关键字"]'
#模型名
search_model_text = f'测试模型_{char}'
#点击模型
click_model = '//div[@class="model-info"]'
#点击模型旁的3个点删除
click_delete_model = '//i[@class="menu-trigger"]'
# 点击删除
click_delete_mo = '//div[@class="menu-content"]/ul/li[2]/span/div'
#确定删除模型
sure_delete_model ='//div[@class="bk-dialog bk-info-box"]/div/div[4]/div/button[1]/div/span'




# ------------------- 关联类型 --------------
# 点击关联类型
click_relevancy_type = '//i[@class="menu-icon icon-cc-nav-associated"]'
# 点击新建
click_create_type = '//button[@class="create-btn bk-primary bk-button-normal bk-button"]/div/span'
# 关联类型的唯一标识
relevancy_type_unique ='[placeholder="请输入英文标识"]'
#唯一标识名称
unique_name ="ceshi_test"
# 关联类型名称
relevancy_type_name ='[placeholder="请输入名称"]'
#输入关联类型名称
type_name ="UI测试专用"
# 源->目标描述
target_describe ='[placeholder="请输入关联描述如：连接、运行"]'
# 输入目标描述
input_target_describe ="测试—连接"
# 目标->源描述
target_source_describe ='[placeholder="请输入关联描述如：属于、上联"]'
# 输入目标->源描述
input_describe="测试-属于"
# 提交按钮
submit ="//div[@class='btn-group']/button/div/span"
# 关联类型搜索框
relevancy_type_search ='[placeholder="请输入关联类型名称"]'
# 搜索框输入不存的条件搜索
search_no_name ="测试不存在的条件"
# 断言
assert_search="搜索结果为空"
# 点击清空搜索条件
clear_search_condition='//button[@class="text-btn bk-primary bk-button-normal bk-button-text"]/div/span'
# 点击编辑按钮
click_edit='//td[@class="bk-table-2-column-9   is-last"]/div/span[1]/button/div/span'
# 编辑增加内容
edit_name="123"
# 点击保存
click_save="/html/body/article/section/div[2]/div[1]/div[2]/button[1]/div/span"
# 断言编辑成
assert_search_save="UI测试专用123"
# 点击删除
click_delete='//td[@class="bk-table-2-column-9   is-last"]/div/span[2]/button/div/span'
# 二次确认点击删除
reconfirm_delete ='//div[@class="footer-wrapper"]/button[1]/div/span'