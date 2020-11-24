import datetime
import hashlib
import re
import time
import json
from Utils.get_config import get_config_data
from Utils.get_data import get_config_path
from Common.Base_Method.request import HttpRequest


pid = get_config_data(get_config_path(__file__,'/Config/test/pid_secretkey.yaml'),'train_pid')

secretkey = get_config_data(get_config_path(__file__,'/Config/test/pid_secretkey.yaml'),'train_secretkey')



class Train_request(HttpRequest):

    def post(self, url, data=None, json=None, **kwargs):
        if data:
            if data.get('trainDate'):
                data['trainDate'] = self.create_time()
        data = self.get_sec_data(data).encode('utf-8')

        return self.request(url, "POST", data, json, **kwargs)


    def get_sec_data(self,datanow):  # data加密
        pass


    def create_time(self):

        later_time = (datetime.datetime.now() + datetime.timedelta(days=21)).strftime("%Y-%m-%d") + " 00:00:00"
        return later_time

Train = Train_request()
