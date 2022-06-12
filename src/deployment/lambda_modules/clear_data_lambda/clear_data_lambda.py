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
    taxis = aggregator_db['taxis']
    restaxi = taxis.delete_many({})
    
    customers = aggregator_db['customers']
    rescustomers = customers.delete_many({})

    aggregator_cli.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Data deleted successfully !')
    }
