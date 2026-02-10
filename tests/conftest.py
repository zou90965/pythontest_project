# pytest配置文件，定义fixture和钩子函数。如数据库连接，http客户端等

import pytest
import subprocess
import os


@pytest.fixture
def login():  # 调用时直接在函数或者方法中的参数中添加fixture名称(login)
    print("登录")  # 执行用例前会打印登录
    yield  # 可以返回一个值： yield 123供后面的的用例使用
    print("登出")  # 执行用例后会打印登出


@pytest.fixture
def sample_data():
    return {"name": "test", "value": 123}


def pytest_sessionfinish(session, exitstatus):
    """
    在测试会话结束后自动生成 Allure 报告
    """
    alluredir = "temps"  # 与 pytest.ini 中的 --alluredir 保持一致
    report_dir = "report"  # HTML 报告输出目录

    # 确保 alluredir 存在
    if not os.path.exists(alluredir):
        print(f"[WARNING] Allure 数据目录 {alluredir} 不存在，跳过报告生成")
        return

    # 调试：打印当前环境变量
    # print("当前 PATH:", os.environ.get("PATH"))

    # 执行 allure generate 命令
    try:
        # 显式传递当前环境变量
        # env = os.environ.copy()
        # 调试：检查 allure 命令路径
        # result = subprocess.run(["which", "allure"], capture_output=True, text=True, env=env)
        # print("allure 命令路径:", result.stdout)

        subprocess.run(
            ["D:\\tools\\allure\\allure-2.16.1\\bin\\allure.bat", "generate", alluredir, "-o", report_dir, "--clean"],
            check=True
        )
        print(f"[INFO] Allure 报告已生成至 {report_dir}")
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] 生成 Allure 报告失败: {e}")
    except FileNotFoundError:
        print("[ERROR] 未找到 allure 命令，请确保已安装并配置 Allure 命令行工具")
