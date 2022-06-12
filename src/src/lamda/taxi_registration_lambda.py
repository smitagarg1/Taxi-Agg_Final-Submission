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
    #res = taxis.delete_many({})

    print("Inserting seed  data for 50 taxis in taxis collection")
    res = taxis.insert_many(event)
    # print(res.inserted_ids)

    print("Creating index on taxis collection")
    taxis.create_index([('location', GEOSPHERE)])
    aggregator_cli.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Taxis registered successfully !')
    }
