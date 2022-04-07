import unittest
from geopoc.connectors.locationiq import LocationIQ
from geopoc.domain.address import Address


class LocationIQTest(unittest.TestCase):
    RESULT1 = Address('Avenida José Luiz Ferraz', '250')

    #  RESULT2 = Address('Rua Apucarana', '850')

    def test_call_and_get_result(self):
        locationiq = LocationIQ()
        result_list = locationiq.call_and_get_result("-23.020642", "-43.486812")
        print(result_list[0])
        self.assertGreater(len(result_list), 0)  # add assertion here
        self.assertIn(self.RESULT1, result_list)




if __name__ == '__main__':
    unittest.main()
