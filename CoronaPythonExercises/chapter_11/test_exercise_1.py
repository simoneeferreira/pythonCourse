import unittest
from exercise_1 import city_info

class test_city_country(unittest.TestCase):
    
    def test_city_info(self):
        city_full_info = city_info('Santiago', 'chile')
        self.assertEqual(city_full_info, 'Santiago, Chile')

if __name__ == '__main__':
    unittest.main()