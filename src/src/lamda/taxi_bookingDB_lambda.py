from bson import ObjectId
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import json
from datetime import datetime
from bson import json_util

aggregator_cli = MongoClient(
    'mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
aggregator_db = aggregator_cli['taxis_and_customers']


def lambda_handler(event, context):
    # TODO implement
    print(event)
    msg = ''
    print("Connecting to Document DB cluster")

    print("User ID ", event['userid'], event['type'])

    taxis = aggregator_db['taxis']
    customers = aggregator_db['customers']

    print("Finding customer by ID ", event['userid'])
    customer = customers.find_one({"_id": ObjectId(event['userid'])})
    print(customer)

    customer_loc = customer['location']

    if event['type'] == 'ALL':
        range_query = {'location': SON([("$near", customer_loc), ("$maxDistance", 1000)]), 'hired': 'N'}
        print("Finding All nearest taxis of type ALL")
    else:
        range_query = {'location': SON([("$near", customer_loc), ("$maxDistance", 1000)]), 'hired': 'N',
                       'type': event['type']}
        print("Finding All nearest taxis of type ", event['type'])

    doc = taxis.find(range_query).limit(2)

    taxiList = list(doc)
    print(len(taxiList), " taxis found")

    if (len(taxiList) > 0):
        booking_id = str(createBooking(customer['_id'], customer['location']))
    else:
        booking_id = -1

    taxiList = json_util.dumps(taxiList)

    return {
        'bookingId': booking_id,
        'taxiList': taxiList
    }


def createBooking(id, location):
    print("Create Booking Started")

    timestamp = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.%f')

    mydict = {"customer_id": str(id), "location": location, "timestamp": timestamp, "booking_accepted": 'N',
              "booking_active": 'Y', "taxiid": ''}

    bookings = aggregator_db['bookings']
    res = bookings.insert_one(mydict)

    print("Booking Created with id ", res.inserted_id)
    print("Create Booking Ended")
    return (res.inserted_id)

