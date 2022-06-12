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
    taxis = aggregator_db['taxis']

    print("Fetching Data for taxis")
    result = taxis.find()

    taxis_list = []
    for rec in result:
        taxis = {'_id': rec['_id'], 'name': rec['name'], 'location': rec['location'], 'timestamp': rec['timestamp'],
                 'email': rec['email'], 'hired': rec['hired'], 'type': rec['type']}
        taxis_list.append(taxis)

    print(taxis_list)
    res=json_util.dumps(taxis_list)
    aggregator_cli.close()

    return {
        'taxiList': json.loads(res)
    }
