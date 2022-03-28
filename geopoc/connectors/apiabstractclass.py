import requests
from abc import ABC, abstractmethod

from requests.structures import CaseInsensitiveDict


class ApiAbstractClass(ABC):
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    def callsingle(self, lat, long):
        callurl = self.url.replace("[LAT]", str(lat)) \
            .replace("[LON]", str(long)). \
            replace("[KEY]", self.key)
        try:
            resp = requests.get(callurl, headers=self.headers)
            print(self.get_name() + ' ' + str(resp.status_code))
            if resp.status_code == 200:
                return self.get_addresses(resp.json())
            else:
                return
        except requests.exceptions.RequestException as e:
            print('Exception ' + e.strerror)
            return

    def call_and_get_result(self, lat, long):
        return self.callsingle(lat, long)

    @abstractmethod
    def get_name(self):
        pass

    @abstractmethod
    def get_addresses(self, json):
        pass

    def __init__(self, new_key, new_url):
        self.key = new_key
        self.url = new_url
