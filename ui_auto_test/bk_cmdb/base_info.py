from configobj import ConfigObj


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

