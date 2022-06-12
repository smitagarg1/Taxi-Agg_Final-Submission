import json
import pprint
from datetime import datetime
from time import sleep

import requests
import numpy as np

from src.APIGatewayUrls import API_GATEWAY_ENDPOINT_TAXI, API_GATEWAY_ENDPOINT_LATLONG_UPDATER

RELATIVE_CONFIG_PATH = '../config/'
CUSTOMER_SIMULATOR_DATA_FILE = 'customer_simulator_data'



class LatLongUpdater:

    def lat_long_updater(self):
        print("\nConnecting to API Gateway for updating lat long for following taxis")
        query_complete_url = API_GATEWAY_ENDPOINT_TAXI + '?id=ALL'
        response = requests.get(API_GATEWAY_ENDPOINT_TAXI)
        print(response.json())

        all_taxis_latlong_data=response.json()['taxiList']

        while True:
            for taxis in all_taxis_latlong_data:
                current_latitude = taxis['location']['coordinates'][0]
                current_longitude = taxis['location']['coordinates'][1]
                new_lat_long = self.create_random_point(current_latitude, current_longitude, 100)
                timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
                dict_latlong = {'id': taxis['_id'], 'new_lat_long': new_lat_long, 'timestamp': timestamp}

                print("\nConnecting to api gateway to update latlong for taxi ", taxis["name"], " with id ",
                      taxis['_id']['$oid'])
                jsondata = json.dumps(dict_latlong)

                response = requests.post(API_GATEWAY_ENDPOINT_LATLONG_UPDATER, data=jsondata)

                print(response.json())
            print("\nSleeping for 60 secs")
            sleep(60)




    # funcion to create new lat long for a taxi per minute
    def create_random_point(self,x0, y0, distance):
        """
                Utility method for simulation of the points
        """
        r = distance / 111300
        u = np.random.uniform(0, 1)
        v = np.random.uniform(0, 1)
        w = r * np.sqrt(u)
        t = 2 * np.pi * v
        x = w * np.cos(t)
        x1 = x / np.cos(y0)
        y = w * np.sin(t)
        x0= x0 + x1
        y0 =y0 + y
        new_lat_long = [round(x0,4) ,round(y0,4)]
        return new_lat_long



