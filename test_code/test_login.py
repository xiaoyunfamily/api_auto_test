import unittest
from parameterized import parameterized
from api.login_api import login
from case_data.login_data import get_login_data


class TestLogin(unittest.TestCase):
    @parameterized.expand(get_login_data)
    def test_login(self, username, password, expect_retcode):
        res = login(username, password)
        self.assertEqual(res['retcode'], expect_retcode)


if __name__ == '__main__':
    unittest.main()
