# -*- coding: UTF-8 -*-

from redis import StrictRedis, ConnectionPool
from urllib import parse


class RedisUtils(object):
    # RedisUtils('redis://:{}@192.168.1.140:6379/0'.format(parse.quote('antoine123!@#')), True)
    def __init__(self, url: str, decode: bool = False):
        """
        构造函数
        :param url: 例: redis://:antoine123@192.168.1.140:6379/0
        :param decode: 密码是否加密
        """
        pool = ConnectionPool.from_url(url)
        self.redis = StrictRedis(connection_pool=pool, decode_responses=decode)

    def set(self, name: str, value: any):
        """
        设置值
        :param name:
        :param value:
        """
        self.redis.set(name=name, value=value)

    def get(self, name: str) -> any:
        """
        获取值
        :param name:
        :return:
        """
        return self.redis.get(name)

    def change_db(self, db: int):
        """
        改变当前数据库
        :param db: 数据库
        """
        self.redis.select(db)
