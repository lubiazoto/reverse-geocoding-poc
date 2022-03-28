import sys

import pandas as pd

from geopoc.connectors.geoapify import GeoApify
from geopoc.connectors.locationiq import LocationIQ
from geopoc.connectors.mapbox import MapBox
from geopoc.connectors.opencage import OpenCage


class ReverseGeocodingController:
    COL_LST = ['URL', 'STREEET', 'NUMBER', 'LAT', 'LONG', 'API']

    def start_run_apis(self):
        for i in range(len(self.df_latlong)):
            row = self.df_latlong.iloc[i]
            print(row)
            for api in self.api_list:
                lat = str(row[3])
                long = str(row[4])
                addr_lst = api.call_and_get_result(lat, long)
                if addr_lst is not None:
                    for a in addr_lst:
                        self.rows_list.append([str(row[0]), a.street, a.number, lat, long, api.get_name()])
        df_result = pd.concat([self.df_latlong, pd.DataFrame(self.rows_list, columns=self.COL_LST)], axis=0)
        df_result.to_csv(self.fileout, index=False)

    def __init__(self, filename, fileout):
        self.fileout = fileout
        self.api_list = []
        self.api_list.append(GeoApify())
        self.api_list.append(MapBox())
        self.api_list.append(OpenCage())
        self.api_list.append(LocationIQ())
        self.df_latlong = pd.read_csv(filename, names=self.COL_LST, header=None)
        self.df_latlong['API'] = 'Google'
        self.rows_list = []


gc = ReverseGeocodingController(sys.argv[1], sys.argv[2])
gc.start_run_apis()
