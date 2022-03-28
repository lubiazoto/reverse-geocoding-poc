from geopoc.connectors.apiabstractclass import ApiAbstractClass
from geopoc.domain.address import Address


class GeoApify(ApiAbstractClass):
    KEY = "c304001f597f49d49fe4943882d6846b"
    URL = "https://api.geoapify.com/v1/geocode/reverse?lat=[LAT]&lon=[LON]&apiKey=[KEY]&limit=3"

    # noinspection PyUnboundLocalVariable
    def get_addresses(self, resp_json):
        # print(resp_json)
        addr_result = []
        for feat in resp_json['features']:
            if 'properties' in feat:
                if 'street' in feat['properties']:
                    street = feat['properties']['street']
                else:
                    street = ''
                if 'housenumber' in feat['properties']:
                    nbr = feat['properties']['housenumber']
                else:
                    nbr = ''
            if len(street) > 0 and len(str(nbr)) > 0:
                addr = Address(street, nbr)
                # print(addr.__str__())
                addr_result.append(addr)
        return addr_result

    def get_name(self):
        return 'GeoApify'

    def __init__(self):
        super().__init__(GeoApify.KEY, GeoApify.URL)
