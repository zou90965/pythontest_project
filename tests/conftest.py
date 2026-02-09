# pytest配置文件，定义fixture和钩子函数。如数据库连接，http客户端等

import pytest


@pytest.fixture
def login():        # 调用时直接在函数或者方法中的参数中添加fixture名称(login)
    print("登录")    # 执行用例前会打印登录
    yield           # 可以返回一个值： yield 123供后面的的用例使用
    print("登出")   # 执行用例后会打印登出


@pytest.fixture
def sample_data():
    return {"name": "test", "value": 123}
