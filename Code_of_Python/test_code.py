import unittest
from unittest.mock import patch
from code_missileThrust_mock import get_code


class TestGetCode(unittest.TestCase):

    @patch('random.randint')
    def test_code(self, mocked_random):
        mocked_random.return_value = 500
        actual = get_code()
        expected = 'Thrust of engine 8740.0'
        self.assertEqual(actual, expected)






