# 导包
import unittest, requests


# 创建测试类
class UnittestTataIHRM(unittest.TestCase):
    # 初始化
    def setUp(self) -> None:
        self.login_url = "http://ihrm-test.itheima.net/api/sys/login"

    def tearDown(self) -> None:
        pass

    # 编写测试函数
    def test001_login(self):
        data = {"mobile": "13800000002", "password": "123456"}
        response = requests.post(url=self.login_url, json=data)
        # 查看响应数据
        print(response.json())
        # 断言
        self.assertIn("操作成功", response.json().get("message"))
