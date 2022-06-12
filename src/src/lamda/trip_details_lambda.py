import json
from pymongo import MongoClient, GEOSPHERE
import datetime
from bson import ObjectId


def lambda_handler(event, context):
    print("Connecting to Document DB cluster")
    taxi_customer_cli = MongoClient(
        'mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
    taxi_customer_db = taxi_customer_cli['taxis_and_customers']
    trips = taxi_customer_db['trips']

    booking_id = event['booking_id']
    trip_status = event['trip_status']
    taxi_id = event["taxi_id"]
    ct = datetime.datetime.now().isoformat()
    if trip_status == 'STARTED':
        print(f"Marking booking id {booking_id} trip started")
        res = trips.insert_one({
            "booking_id": ObjectId(booking_id),
            "trip_start": ct,
            "trip_end": None
        })
    else:
        print(f"Marking booking id {booking_id} trip ended")
        res = trips.update_one({"booking_id": ObjectId(booking_id)},
                               {"$set": {"trip_end": ct}})
        res = taxi_customer_db['taxis'].update_one({"_id": ObjectId(taxi_id)},
                                                       {"$set": {"hired": "n"}})

    res = trips.find()
    print("Printing the updated trip details")
    print(list(res))
    taxi_customer_cli.close()

    return {
        'statusCode': 200,
        'body': json.dumps('Trip details updated !')
    }
