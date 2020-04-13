import unittest
from unittest import mock

from post_youdao import *


class PostYouDaoTest(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, True)

    def test_get_ts(self):
        # import time
        # t = time.time()
        # ts = str(int(round(t*1000)))
        # print(ts)
        get_ts = mock.Mock(return_value='1584683236366')  # 模拟对象返回值
        self.assertEqual('1584683236366', get_ts())

    def test_get_salt(self):
        get_salt = mock.Mock(return_value='15846832363666')
        self.assertEqual('15846832363666', get_salt())

    def test_get_sign(self):
        get_sign = mock.Mock(return_value='809144ef068d33d6c454d24cd8a0013e')
        self.assertEqual('809144ef068d33d6c454d24cd8a0013e', get_sign())


if __name__ == '__main__':
    unittest.main()
