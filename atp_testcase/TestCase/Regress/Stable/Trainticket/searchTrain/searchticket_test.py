import pytest
import allure
from Utils.get_data import get_data_path
from Utils.get_data import get_test_data
from Common.Test_Trainticket_Method.SendRequest import Train


case, param = get_test_data(get_data_path(__file__))

@allure.feature('火车票')
class TestParam(object):
    """
    """

    @pytest.fixture(scope="function")
    def prepare(self, request):
        api = "/wanghao/train/searchTrain"
        yield api

        def fin():
            """
            Clean up test environment after testing
            """

        request.addfinalizer(fin)

    @allure.story('火车票接口')
    @pytest.mark.parametrize("case,headers,querystring,data,expected", param[:1], ids=case[:1])
    def test_param(self, case, headers, querystring, data, expected,prepare):
        response = Train.post(url=prepare, headers=headers, data=data)
        res = response.json()
        assert res["code"] == expected["code"]

    @allure.story('查询火车票接口')
    @pytest.mark.parametrize("case,headers,querystring,data,expected", param[1:2], ids=case[1:2])
    def test_param2(self, case, headers, querystring, data, expected,prepare):
        response = Train.post(url=prepare, headers=headers, data=data)
        res = response.json()
        assert res["code"] == expected["code"]

if __name__ == '__main__':
        pytest.main(['searchticket_test.py'])
