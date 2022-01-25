import unittest

from module.crDb.mssql_utils import MssqlUtils
from module.except_hook_handler import ExceptHookHandler
from module.http_utils import HttpUtils


class MyTestCase(unittest.TestCase):
    def test_something(self):
        e = MssqlUtils()
        e.__c
        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()
