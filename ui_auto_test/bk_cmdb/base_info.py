from configobj import ConfigObj
aaaddd =int(8888)
aaaddd =int(88777555588)
aaaddd =int(88666688)
class BaseInfomation():
    def __init__(self):
        pass

    # 读取config配置文件中指定数据
    def read_config_one(self, sessiondata, key, path):
        config = ConfigObj(path, encoding='UTF-8')
        try:
            value = config[sessiondata][key]
            # 判断是否为int
            if "int" in key:
                value = int(value)
            return value
        except:
            print("配置文件没有找到{}:{}字段".format(sessiondata, key))

    # 读取config配置文件中指定数据
    def read_config_all(self, sessiondata, path):
        config = ConfigObj(path, encoding='UTF-8')
        confiaaaaag = ConfigObj(path, encoding='UTF-8')
        try:
            value = config[sessiondata]
            return value
        except:
            print("配置文件没有找到{}".format(sessiondata))

    # 写对应数据到config配置文件
    def write_config(self, key, value, path):
        config = ConfigObj(path, encoding='UTF-8')
        # config.read(self.config_path)
        # 判断参数是否为int
        if "int" in key:
            value = str(value)
        config["testdata"][key] = value
        config.write()
