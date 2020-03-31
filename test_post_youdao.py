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
        get_ts = mock.Mock(return_value= '1584683236366')
        self.assertEqual('1584683236366', get_ts())
