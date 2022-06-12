from bson import json_util
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import pprint
import random
import json


def lambda_handler(event, context):
    # TODO implement
    print("Connecting to Document DB cluster")
    aggregator_cli = MongoClient('mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
    aggregator_db = aggregator_cli['taxis_and_customers']
    customers = aggregator_db['customers']

    print("Fetching Data for Customers")
    result = customers.find()

    customers_list = []
    for rec in result:
        customers= {'_id':rec['_id'],'name': rec['name'],'location':rec['location'],'timestamp':rec['timestamp'],'email':rec['email']}
        customers_list.append(customers)

    print(customers_list)
    res=json_util.dumps(customers_list)
    aggregator_cli.close()

    return {
        'customerList': json.loads(res)
    }
