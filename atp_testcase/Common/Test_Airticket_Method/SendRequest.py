import datetime
import hashlib
import re
import time
import json
from Utils.get_config import get_config_data
from Utils.get_data import get_config_path
from Common.Base_Method.request import HttpRequest



pid = get_config_data(get_config_path(__file__,'/Config/test/pid_secretkey.yaml'),'air_pid')

secretkey = get_config_data(get_config_path(__file__,'/Config/test/pid_secretkey.yaml'),'air_secretkey')

pGroupId = get_config_data(get_config_path(__file__,'/Config/test/pid_secretkey.yaml'),'air_pGroupId')



class Air_request(HttpRequest):


    def post(self, url, data=None, json=None, **kwargs):
        if data:
            if data.get('takeOffDate'):
                data['takeOffDate'] = self.create_time()
        data = self.get_sec_data(data)
        return self.request(url, "POST", data, json, **kwargs)


    def get_sec_data(self,olddata):  # data加密
        pass

    def create_time(self):

        later_time = (datetime.datetime.now() + datetime.timedelta(days=21)).strftime("%Y-%m-%d")
        return later_time

Air = Air_request()