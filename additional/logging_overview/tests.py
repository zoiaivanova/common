import unittest

import testfixtures

from main import pay_developer


class TestDevelopersSalary(unittest.TestCase):

    def test_normal_salary(self):
        with testfixtures.LogCapture() as logs:
            pay_developer(180)

        print(logs)


if __name__ == "__main__":
    unittest.main()
