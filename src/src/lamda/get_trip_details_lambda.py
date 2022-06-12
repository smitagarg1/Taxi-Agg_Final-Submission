from bson import json_util
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import pprint
import random
import json


def lambda_handler(event, context):
    print("Connecting to Document DB cluster")
    taxi_customer_cli = MongoClient('mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
    taxi_customer_db = taxi_customer_cli['taxis_and_customers']
    trips = taxi_customer_db['trips']

    print("Fetching Data for Trips")
    result = trips.find()
    res=list(result)

    res=json_util.dumps(res)
    taxi_customer_cli.close()

    return {
        'trips': json.loads(res)
    }