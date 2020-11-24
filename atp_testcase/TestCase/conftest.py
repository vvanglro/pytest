# from typing import List
# #修改用例中文unicode问题
# def pytest_collection_modifyitems(
#     session: "Session", config: "Config", items: List["Item"]
# ) -> None:
#     for item in items:
#         item.name = item.name.encode('utf-8').decode('unicode-escape')
#         item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

import os
import pytest
import yaml
from Common.Base_Method.request import req
from Utils.variable import is_vars

@pytest.fixture(scope="session",autouse=True)
def env(request):
    config_path = os.path.join(request.config.rootdir,
                               "Config",
                               request.config.getoption("environment"),
                               "host.yaml")
    with open(config_path) as f:
        env_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
    is_vars.set('host',env_config['host'])


def pytest_addoption(parser):
    parser.addoption("--env",
                     action="store",
                     dest="environment",
                     default="test",
                     help="environment: test or prod")


@pytest.fixture(scope='session',autouse=True)
def is_login(request):
    pass

    def fn():
        req.close_session()

    request.addfinalizer(fn)