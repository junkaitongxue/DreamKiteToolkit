from unittest import mock
import unittest

from dreamkite.toolkit.common.crypto.crypto import Encrypts

from unittest.mock import patch
import hashlib


# test Encrypts class
class TestCount(unittest.TestCase):

    # 以test开头的才能执行，另外需要使用unittest.main()来调用
    def test_md5_encrypt(self):
        encrypts = Encrypts()
        encrypts.md5_encrypt = mock.Mock(return_value='hello')
        result = encrypts.md5_encrypt('hjk')
        self.assertEqual(result, 'hello')

    # mock掉对需要mock的模块的依赖库
    @patch("hashlib.md5")
    def test_md5_encrypt2(self, mock_md5):
        # 以下对hashlib的md5mock之后会将实际调用都返回该hashlib.md5 导致结果不对
        mock_md5.return_value = hashlib.md5
        encrypts = Encrypts()
        result = encrypts.md5_encrypt('hello')
        self.assertNotEqual(result, '5d41402abc4b2a76b9719d911017c592')


if __name__ == '__main__':
    unittest.main()
