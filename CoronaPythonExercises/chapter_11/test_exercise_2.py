import unittest
from exercise_2 import city_info

class test_city_country(unittest.TestCase):
    
    def test_city_info(self):
        city_full_info = city_info('Santiago', 'chile')
        self.assertEqual(city_full_info, 'Santiago, Chile')

    def test_city_population_info(self):
        city_full_info = city_info('Santiago', 'chile', population=5_500_000)
        self.assertEqual(city_full_info, 'Santiago, Chile - population 5500000')
        
if __name__ == '__main__':
    unittest.main()