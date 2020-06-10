# 导包
import unittest, requests

# 创建测试类
from parameterized import parameterized

from utils import read_login_data


class TestIHRMLogin(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def tearDown(self) -> None:
        pass

    @parameterized.expand(read_login_data())
    # 编写测试函数
    def test001_login(self, case_name, request_body,message):
        data = request_body
        response = requests.post(url=self.login_url, json=data,)
        # 查看响应数据
        print(response.json())
        # 断言
        self.assertIn(message, response.json().get("message"))
