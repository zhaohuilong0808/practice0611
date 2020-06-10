# 导包
import requests

# 发送ihrm接口请求
url = "http://ihrm-test.itheima.net/api/sys/login"
data = {"mobile": "13800000002", "password": "123456"}
response = requests.post(url=url, json=data)
# 查看响应数据
print(response.json())
