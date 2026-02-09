# 主要是存放常用的函数和方法
import sys

import requests
import logging
import yaml

# 配置日志
# logging.basicConfig(level=logging.INFO)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.StreamHandler(sys.stdout)]
)
logger = logging.getLogger(__name__)


# 发起请求的方法
def send_request(name, method, url, **kwargs):
    headers = kwargs.get("headers", {})
    json = kwargs.get("json", {})
    # 记录请求信息
    logger.info(f"用例名称: {name}")
    logger.info(f"请求方法: {method}")
    logger.info(f"请求URL: {url}")
    logger.info(f"请求参数: {json}")

    print("请求接口url：" + url)
    print("请求接口方法：" + method)
    print("请求接口headers：" + str(headers))
    print("请求参数 :" + str(json))

    try:
        # 发起请求
        response = requests.request(method, url, **kwargs)

        # 记录响应信息
        logger.info(f"响应状态码: {response.status_code}")
        logger.info(f"响应内容: {response.text}")

        print("响应状态码: " + str(response.status_code))
        print("响应数据: " + str(response.json()))

        return response
    except Exception as e:
        # 记录异常信息
        logger.error(f"请求失败: {e}")
        raise


# 读取yaml文件的方法
def read_yaml_file(file_path):
    """
    读取 YAML 文件并返回解析后的内容
    :param file_path: YAML 文件路径
    :return: 解析后的数据（字典或列表）
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = yaml.safe_load(file)
            return data
    except FileNotFoundError:
        print(f"文件未找到: {file_path}")
    except yaml.YAMLError as e:
        print(f"YAML 解析错误: {e}")
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
