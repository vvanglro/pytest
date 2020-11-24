#coding=utf-8

import pytest
import allure
from Utils.get_data import get_data_path
from Utils.get_data import get_test_data
from Common.Test_Airticket_Method.SendRequest import Air


case, param = get_test_data(get_data_path(__file__))

@allure.feature('机票')
class TestParam(object):
    """
    """
    # 在每个方法执行前执行
    @pytest.fixture(scope="function")
    def prepare(self, request):
        # print('执行前')
        api = "/wanghao/airticket/getFlightQuerySingle"
        yield api

        def fin():
            """
            Clean up test environment after testing
            """
            # print('执行后')

        request.addfinalizer(fin)

    @allure.story('查询接口')
    @allure.title("{case}")  # 报告上的用例标题
    @allure.link('http://www.baidu.com',name='接口文档') # 报告上的超链接
    @pytest.mark.parametrize("case,headers,querystring,data,expected", param, ids=case)   # 动态传参
    def test_param(self,case, headers, querystring, data, expected,prepare):
        response = Air.post(url=prepare,  headers=headers, data=data)
        res = response.json()
        for k,v in expected.items():
                assert res[k] == v

if __name__ == '__main__':
        pytest.main(['getFlightQuerySingle_test.py'])