from public_method.login import LoginBase



class PublicMethod(LoginBase):
    def select_plugin_type(self, plugin_type: dict, plugin_name: dict):
        # 选择插件类型
        self.my_click(element=plugin_type)
        # 选择插件
        self.my_click(element=plugin_name)
