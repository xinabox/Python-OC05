import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('hello world'.upper(), 'HELLO WORLD')

if __name__ == '__main__':
    unittest.main()
