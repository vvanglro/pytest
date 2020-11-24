# -*- coding:utf-8 -*-
import os
import logging
from datetime import datetime
from Utils.get_data import get_log_path


LOG_PATH = get_log_path(__file__,'/logs')

class Logger:
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        if not self.logger.handlers:
            self.logger.setLevel(logging.DEBUG)

            # 创建一个handler，用于写入日志文件
            fh = logging.FileHandler(self.log_path, encoding='utf-8')
            fh.setLevel(logging.DEBUG)

            # 在控制台输出
            ch = logging.StreamHandler()
            ch.setLevel(logging.INFO)

            # 定义hanler的格式
            formatter = logging.Formatter(self.fmt)
            fh.setFormatter(formatter)
            ch.setFormatter(formatter)

            # 给log添加handles
            self.logger.addHandler(fh)
            self.logger.addHandler(ch)

    @property
    def fmt(self):
        return '%(asctime)s %(levelname)s %(filename)s:%(lineno)d %(message)s'

    @property
    def log_path(self):
        if not os.path.exists(LOG_PATH):
            os.makedirs(LOG_PATH)
        month = datetime.now().strftime("%Y_%m_%d")
        return os.path.join(LOG_PATH, '{}.log'.format(month))


log = Logger('root').logger
if __name__ == '__main__':
    log.info("你好")
