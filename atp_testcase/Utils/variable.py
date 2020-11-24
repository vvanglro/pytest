# -*- coding:utf-8 -*-


class Variable:
    """全局变量池"""

    def __init__(self):
        pass
        # super().__init__()

    def set(self, key, value):
        setattr(self, key, value)

    def get(self, key):
        return getattr(self, key)

    def has(self, key):
        return hasattr(self, key)


is_vars = Variable()