import pytest

from tests.common.api_client import read_yaml_file, send_request

# 获取yaml文件中的数据
data = read_yaml_file("D:\\tools\pycharm\pythontest_project\\tests\data\\testa_data.yaml")
print(data)

data1 = data["test_cases"]
print(data1)


# def test_1():
#     print(data)
#     print(data1)


@pytest.mark.parametrize("test_data", data1)
def test_request(test_data):
    # print(test_data)
    name, request_info = test_data["name"], test_data["request_info"]
    # print("用例名称:" + name)
    # print("接口请求信息 :" + str(request_info))
    url, method, headers, expected = request_info["url"], request_info["method"], request_info["headers"], request_info[
        "expected"]
    if "json" in request_info:
        json = request_info["json"]
        response = send_request(name, method, url, headers=headers, json=json)
    else:
        response = send_request(name, method, url, headers=headers)
    assert response.status_code == expected["status_code"]
    assert response.json()["id"] == expected["id"]
