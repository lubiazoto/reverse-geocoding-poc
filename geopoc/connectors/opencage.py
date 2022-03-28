from geopoc.connectors.apiabstractclass import ApiAbstractClass
from geopoc.domain.address import Address


class OpenCage(ApiAbstractClass):
    KEY = "dfece9d06eae43889aeca571da30ec96"
    URL = "https://api.opencagedata.com/geocode/v1/json?key=[KEY]&q=[LAT]%2C[LON]&limit=3"

    def get_addresses(self, resp_json):
        # print(resp_json)
        addr_result = []
        for feat in resp_json['results']:
            if 'components' in feat:
                if 'road' in feat['components']:
                    street = feat['components']['road']
                else:
                    street = ''
                if 'house_number' in feat['components']:
                    nbr = feat['components']['house_number']
                else:
                    nbr = ''
                if len(street) > 0 and len(nbr) > 0:
                    addr = Address(street, nbr)
                    # print(addr.__str__())
                    addr_result.append(addr)
        return addr_result

    def get_name(self):
        return 'OpenCage'

    def __init__(self):
        super().__init__(OpenCage.KEY, OpenCage.URL)
