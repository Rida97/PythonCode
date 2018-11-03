import unittest
from city_functions import City_Country


class CityCountryTestCase(unittest.TestCase):
    def test_names_city_country(self):
        formatted_name = City_Country('Chicago','USA')
        self.assertEqual(formatted_name,'Chicago USA')

unittest.main()
