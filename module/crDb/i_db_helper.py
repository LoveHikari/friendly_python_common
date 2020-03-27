# coding=utf-8
# 数据库访问接口
class IDbHelper:

    def executeInsert(self, sql: str, params: list = None):
        '''
        执行添加语句，并返回添加后的id
        :param sql: SQL语句
        :param params: 参数列表
        :return: id
        '''

    def executeNonQuery(self, sql: str, params: list = None):
        '''
        执行非查询语句,并返回受影响的记录行数
        :param sql: SQL语句
        :param params: 参数列表
        :return: 影响行数
        '''

    def executeDataSet(self, sql: str, params: list = None):
        '''
        执行查询，并以list[dict]返回结果集
        :param sql:  SQL语句
        :param params: 参数列表
        :return:
        '''
