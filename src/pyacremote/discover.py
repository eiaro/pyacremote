import logging
import time
import zeroconf
from typing import Optional
import urllib.request, json
from  config import ACState

class ACRemote(object):

    def __init__(self, address=None):
        if address is not None:
            self._address = address

    def getState(self, asJson = False):
        with urllib.request.urlopen("http://" + self._address +  "/acstate") as url:
            data = json.loads(url.read().decode())

        if asJson:
            return data
        else:
            return ACState(data)


class Discover:

    def __init__(self):
        self._foundDevices = []
        
    def add_service(self, zeroconf, serviceType, name):
        """
        """
        info = zeroconf.get_service_info(serviceType, name)
        
        self._foundDevices.append(ACRemote(info.server))


    def run(self, ttl=None) -> Optional[ACRemote]:
        """
        Run MDNS discovery.
        """
        zconf = zeroconf.Zeroconf()

        zconf.add_service_listener("_acremote._tcp.local.", self)

        if ttl is not None:
            count = 0
            while count < ttl:
                count+=1
                time.sleep(0.01)
        
        zconf.close()

        if len(self._foundDevices) > 0:
            return self._foundDevices
        return None


        

            
