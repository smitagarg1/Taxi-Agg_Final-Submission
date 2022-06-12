import json
import requests
from datetime import datetime
from src.APIGatewayUrls import API_GATEWAY_ENDPOINT_TAXI

RELATIVE_CONFIG_PATH = '../config/'
TAXI_SIMULATOR_DATA='taxi_simulator_data'


class TaxiRegistration:
    def taxi_register_simulator(self):
        f = open(RELATIVE_CONFIG_PATH + TAXI_SIMULATOR_DATA + ".json")
        config = json.loads(f.read())
        f.close()

        for rec in config['taxi_list']:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            rec['timestamp']=timestamp

        jsondata = json.dumps(config['taxi_list'])





        print("Connecting to API Gateway for taxi data update")
        response = requests.post(API_GATEWAY_ENDPOINT_TAXI, data=jsondata)
        return response.json()

    def taxi_details(self):
        print("Connecting to API Gateway for taxi details")
        response = requests.get(API_GATEWAY_ENDPOINT_TAXI)
        return response.json()
