# -*- coding:utf-8 -*-
import allure
import urllib3
import requests
from Utils.logger import log
from requests import Response
from requests.exceptions import RequestException
from Utils.variable import is_vars
import json as complexjson

urllib3.disable_warnings()

__all__ = ['req', 'defaultHeader']



class HttpRequest():

    def __init__(self):
        self.timeout = 30.0
        self.session = requests.session()

    def get(self, url, **kwargs):
        return self.request(url, "GET", **kwargs)

    def post(self, url, data=None, json=None, **kwargs):
        return self.request(url, "POST", data, json, **kwargs)

    def put(self, url, data=None, **kwargs):
        return self.request(url, "PUT", data, **kwargs)

    def delete(self, url, **kwargs):
        return self.request(url, "DELETE", **kwargs)

    def patch(self, url, data=None, **kwargs):
        return self.request(url, "PATCH", data, **kwargs)

    def request(self, url, method, data=None, json=None, **kwargs):
        url = is_vars.get('host') + url
        headers = dict(**kwargs).get("headers")
        defaultHeader(headers, method)
        params = dict(**kwargs).get("params")
        files = dict(**kwargs).get("files")
        cookies = dict(**kwargs).get("cookies")
        self.request_log(url, method, data, json, params, headers, files, cookies)
        try:
            if method == "GET":
                response = self.session.get(url, **kwargs)
            elif method == "POST":
                response = self.session.post(url, data, json, **kwargs)
            elif method == "PUT":
                if json:
                    # PUT 和 PATCH 中没有提供直接使用json参数的方法，因此需要用data来传入
                    data = complexjson.dumps(json)
                response = self.session.put(url, data, **kwargs)
            elif method == "DELETE":
                response = self.session.delete(url, **kwargs)
            elif method == "PATCH":
                if json:
                    data = complexjson.dumps(json)
                response = self.session.patch(url, data, **kwargs)
            else:
                raise AttributeError("send request method is ERROR!")
            with allure.step("%s请求接口" % method):
                allure.attach(url, name="请求地址")
                allure.attach(complexjson.dumps(headers,ensure_ascii=False,indent=2), "请求头")
                if data:
                    allure.attach(str(data), name="请求参数")
                if params:
                    allure.attach(str(params), name="请求参数")
                allure.attach(str(response.status_code), name="响应状态码")
                allure.attach(str(self.elapsed_time(response)), name="响应时间(单位秒)")
                allure.attach(response.text, "响应内容")
            log.info(response)
            log.info("Response Data: {}".format(response.text[:40] + "....." + response.text[-10:]))
            return response
        except RequestException as e:
            log.exception(format(e))
        except Exception as e:
            raise e

    def request_log(self, url, method, data=None, json=None, params=None, headers=None, files=None, cookies=None, **kwargs):

        log.info("接口请求地址 ==>> {}".format(url))
        log.info("接口请求方式 ==>> {}".format(method))
        # Python3中，json在做dumps操作时，会将中文转换成unicode编码，因此设置 ensure_ascii=False
        log.info("接口请求头 ==>> {}".format(complexjson.dumps(headers,ensure_ascii=False)))
        if params:
            log.info("接口请求 params 参数 ==>> {}".format(complexjson.dumps(params, ensure_ascii=False)))
        if data:
            log.info("接口请求体 data 参数 ==>> {}".format(data))
        if json:
            log.info("接口请求体 json 参数 ==>> {}".format(complexjson.dumps(json, ensure_ascii=False)))
        if files:
            log.info("接口上传附件 files 参数 ==>> {}".format(files))
        if cookies:
            log.info("接口 cookies 参数 ==>> {}".format(complexjson.dumps(cookies,  ensure_ascii=False)))


    def elapsed_time(self,func: Response, fixed: str = 's'):
        """
        用时函数
        :param func: response实例
        :param fixed: 1或1000 秒或毫秒
        :return:
        """
        try:
            if fixed.lower() == 's':
                second = func.elapsed.total_seconds()
            elif fixed.lower() == 'ms':
                second = func.elapsed.total_seconds() * 1000
            else:
                raise ValueError("{} not in ['s'，'ms']".format(fixed))
            return second
        except RequestException as e:
            log.exception(e)
        except Exception as e:
            raise e

    def close_session(self):
        print("关闭会话")
        self.session.close()


# 默认头
class defaultHeader:

    def __init__(self, header, type):
        if header == None:
            header = {}
        self.header = header
        self.__addAccept()
        self.__addUser_Agent()
        self.__addConnection()
        if type == "POST":
            self.__addContentType()

    # 添加关闭keep-alive
    def __addConnection(self):
        if "Connection" not in self.header:
            self.header["Connection"] = "keep-alive"

    # 添加Content-Type
    def __addContentType(self):
        if "Content-Type" not in self.header:
            self.header["Content-Type"] = "application/json;charset=UTF-8"

    def __addAccept(self):
        if "Accept" not in self.header:
            self.header["Accept"] = "application/json, text/plain, */*"

    def __addUser_Agent(self):
        if "User-Agent" not in self.header:
            self.header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"




req = HttpRequest()
if __name__ == '__main__':
    pass