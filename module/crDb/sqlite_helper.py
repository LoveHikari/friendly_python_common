# -*- coding: utf-8 -*-
import sqlite3

from module.crDb.i_db_helper import IDbHelper


# sqlite 数据库访问类
class SqliteHelper(IDbHelper):
    # 构造函数
    def __init__(self, dbfile: str = 'data.db'):
        self.conn = sqlite3.connect(dbfile)
        self.cursor = self.conn.cursor()
        print("打开数据库成功")

    def executeInsert(self, sql: str, params: list = None) -> int:
        '''
        执行添加语句，并返回添加后的id
        :param sql: SQL语句
        :param params: 参数列表
        :return: id
        '''
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.conn.commit()
        return self.cursor.lastrowid

    def executeNonQuery(self, sql: int, params: list = None) -> int:
        '''
        执行非查询语句,并返回受影响的记录行数
        :param sql: SQL语句
        :param params: 参数列表
        :return: 影响行数
        '''
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        self.conn.commit()
        return self.conn.total_changes

    def executeDictList(self, sql, params: list = None) -> list[dict]:
        '''
        执行查询，并以list[dict]返回结果集
        :param sql:  SQL语句
        :param params: 参数列表
        :return:
        '''
        if params is None:
            self.cursor.execute(sql)
        else:
            self.cursor.execute(sql, params)
        desc = self.cursor.description  # 获取字段的描述，默认获取数据库字段名称，重新定义时通过AS关键重新命名即可
        data_dict = [dict(zip([col[0] for col in desc], row)) for row in self.cursor.fetchall()]  # 列表表达式把数据组装起来
        return data_dict

    # 关闭数据库
    def __del__(self):
        """
        关闭数据库
        :return:
        """
        self.conn.close()
