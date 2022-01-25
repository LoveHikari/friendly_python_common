import pymssql


class MssqlUtils(object):
    def __init__(self, host, user, password, database):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__database = database

    def any(self, name) -> bool:
        self.__create_connect()
        b = False
        try:
            sql_str = 'select count(*) from dt_company where name=%s'
            self.cursor.execute(sql_str, name)
            rows = self.cursor.fetchall()
            b = rows[0][0] > 0
        except Exception as ex:
            self.conn.rollback()
            # raise ex
        finally:
            self.conn.close()
            return b

    def add(self, entity) -> int:
        self.__create_connect()
        id_s = 0
        try:
            keys = str.join(',', list(entity.keys()))
            sql_str = f"""insert into dt_company ({keys}) values ({('%s,' * len(entity.keys())).rstrip(',')})"""
            self.__cursor.execute(sql_str, tuple(entity.values()))
            self.__conn.commit()
            # rows = self.cursor.fetchall()
            # id_s = rows[0][0]
        except Exception as ex:
            self.__conn.rollback()
            raise ex
        finally:
            self.__conn.close()
            return id_s

    def __create_connect(self):
        self.__conn = pymssql.connect(self.__host, self.__user, self.__password, self.__database)
        self.__cursor = self.__conn.cursor()
