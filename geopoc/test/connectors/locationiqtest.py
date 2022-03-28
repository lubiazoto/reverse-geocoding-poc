import unittest
from geopoc.connectors.locationiq import LocationIQ
from geopoc.domain.address import Address


class LocationIQTest(unittest.TestCase):
    RESULT1 = Address('Rua Emílio Mallet', '1015')

    #  RESULT2 = Address('Rua Apucarana', '850')

    def test_call_and_get_result(self):
        locationiq = LocationIQ()
        result_list = locationiq.call_and_get_result("-23.5459078", "-46.5638089")
        self.assertGreater(len(result_list), 0)  # add assertion here
        self.assertIn(self.RESULT1, result_list)
    #    self.assertIn(self.RESULT2, result_list)


if __name__ == '__main__':
    unittest.main()
