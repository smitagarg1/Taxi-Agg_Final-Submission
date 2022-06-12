import json
from datetime import datetime

import requests

from src.APIGatewayUrls import API_GATEWAY_ENDPOINT_CUSTOMER

RELATIVE_CONFIG_PATH = '../config/'
CUSTOMER_SIMULATOR_DATA = 'customer_simulator_data'



class CustomerRegistration:

    def customer_register_simulator(self):
        f = open(RELATIVE_CONFIG_PATH + CUSTOMER_SIMULATOR_DATA + ".json")
        config = json.loads(f.read())
        f.close()

        for rec in config['customer_list']:
            timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')
            rec['timestamp']=timestamp

        jsondata = json.dumps(config['customer_list'])

        print("Connecting to API Gateway for customer data update")
        response = requests.post(API_GATEWAY_ENDPOINT_CUSTOMER, data=jsondata)
        return response.json()


    def customer_details(self):
        print("Connecting to API Gateway for customer details")
        response = requests.get(API_GATEWAY_ENDPOINT_CUSTOMER)
        return response.json()