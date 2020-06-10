# 导包
import time, unittest
import HTMLTestRunner_PY3
from script.test_ihrm_login import TestIHRMLogin
# 创建测试套件
suite = unittest.TestSuite()
# 测试用例添加到测试套件上
suite.addTest(unittest.makeSuite(TestIHRMLogin))
# 定义测试报告的目录和文件名
path = "./report/tpshop{}.html".format(time.strftime("%Y%m%d--%H%M%S"))
# 使用HTMLTestRunner_PY3生成测试报告
with open(path, "wb") as f:
    # 实例化HTMLTestRunner_PY3
    runner = HTMLTestRunner_PY3.HTMLTestRunner(f, title="测试报告", description="赵慧龙")
    # 生成报告
    runner.run(suite)