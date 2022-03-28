from geopoc.connectors.apiabstractclass import ApiAbstractClass
from geopoc.domain.address import Address


class MapBox(ApiAbstractClass):
    KEY = "pk.eyJ1IjoibGJpYXpvdG8iLCJhIjoiY2wwcHNkZG15MDF5MzNvbXRtdTI3Y3IxMCJ9.gQbDfB_QxCwi3REd2eXHFg"
    URL = "https://api.mapbox.com/geocoding/v5/mapbox.places/[LON],[LAT].json?access_token=[KEY]"

    def get_addresses(self, resp_json):
        # print(resp_json)
        addr_result = []
        for feat in resp_json['features']:
            if feat['id'].startswith('address.'):
                if 'text' in feat:
                    street = feat['text']
                else:
                    street = ''
                if 'address' in feat:
                    nbr = str(feat['address'])
                else:
                    nbr = ''
                if len(street) > 0 and len(nbr) > 0:
                    addr = Address(street, nbr)
                    # print(addr.__str__())
                    addr_result.append(addr)
        return addr_result

    def get_name(self):
        return 'MapBox'

    def __init__(self):
        super().__init__(MapBox.KEY, MapBox.URL)
