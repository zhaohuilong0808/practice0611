# 读取登录数据
import json
import os


def read_login_data():
    # 定义读取数据文件的地址
    login_data_path = os.path.dirname(os.path.abspath(__file__)) + "/data/login_data.json"
    # 打开文件,使用json加载文件流.加载成json格式
    with open(login_data_path, mode="r", encoding="utf-8") as f:
        # 使用json文件流
        jsonData  = json.load(f)
        # 定义空列表
        result_list = list()
        # 使用for循环遍历,去处登录数据
        for login_data in jsonData:  # type:dict
            result_list.append(tuple(login_data.values()))

        print(result_list)
        return result_list

if __name__ == '__main__':
    read_login_data()