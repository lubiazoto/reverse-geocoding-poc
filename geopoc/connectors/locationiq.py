from geopoc.connectors.apiabstractclass import ApiAbstractClass
from geopoc.domain.address import Address


class LocationIQ(ApiAbstractClass):
    KEY = "pk.c1073fe4821fcc93ebab8091e28eab8a"
    URL = "https://us1.locationiq.com/v1/reverse.php?key=[KEY]&lat=[LAT]&lon=[LON]&format=json"

    def get_addresses(self, resp_json):
        # print(resp_json)
        addr_result = []
        if 'address' in resp_json:
            if 'road' in resp_json['address']:
                street = resp_json['address']['road']
            else:
                street = ''
            if 'house_number' in resp_json['address']:
                nbr = resp_json['address']['house_number']
            else:
                nbr = ''
            addr = Address(street, nbr)
            # print(addr.__str__())
            addr_result.append(addr)
        return addr_result

    def get_name(self):
        return 'LocationIQ'

    def __init__(self):
        super().__init__(LocationIQ.KEY, LocationIQ.URL)
