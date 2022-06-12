from pymongo import MongoClient, GEOSPHERE
import json
from bson import ObjectId


def lambda_handler(event, context):
    # TODO implement
    print("Connecting....")
    aggregator_cli = MongoClient('mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
    aggregator_db = aggregator_cli['taxis_and_customers']
    taxis = aggregator_db['taxis']

    new_lat_long = event['new_lat_long']
    print(new_lat_long)
    new_location = {"type": "Point",
                    "coordinates": new_lat_long}
    taxis.update_one({"_id": ObjectId(event['id']['$oid'])}, {"$set": {"location": new_location,"timestamp":event['timestamp']}})

    aggregator_cli.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Coordinates for Taxi updated !')
    }



