# pytest配置文件，定义fixture和钩子函数。如数据库连接，http客户端等

import pytest


@pytest.fixture
def login():
    print("登录")
    yield
    print("登出")


@pytest.fixture
def sample_data():
    return {"name": "test", "value": 123}
