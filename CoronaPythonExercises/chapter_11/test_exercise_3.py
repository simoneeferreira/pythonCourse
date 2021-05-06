import unittest
from exercise_3 import Employee

class TestEmployee(unittest.TestCase):

    def setUp(self):
        self.anna = Employee('anna', 'souza', 25000)

    def test_give_default_raise(self):
        self.anna.give_raise()
        self.assertEqual(self.anna.salary, 25000)
    
    def test_give_custom_raise(self):
        self.anna.give_raise(10000)
        self.assertEqual(self.anna.salary, 35000)

if __name__ == '__main__':
    unittest.main()