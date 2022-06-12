from bson import ObjectId
from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import json
from datetime import datetime
from bson import json_util
aggregator_cli=MongoClient('mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017''/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred''&retryWrites=false')
aggregator_db = aggregator_cli['taxis_and_customers']


def lambda_handler(event, context):
    # TODO implement

    msg = ''
    customeremail = ''
    print("Connecting to Document DB cluster")
    bookings = aggregator_db['bookings']
    taxis = aggregator_db['taxis']
    customers = aggregator_db['customers']

    booking = bookings.find_one({"_id": ObjectId(event['bookingid'])})
    print(booking['booking_accepted'])

    if not booking['booking_accepted'] == 'Y':
        print("Accepting the booking")

        print("Marking booking as accepted in booking collection")
        resbookings = bookings.update_one({"_id": ObjectId(event['bookingid'])},
                                          {"$set": {"booking_accepted": 'Y', "taxiid": event['taxiid']}})
        print(resbookings)
        msg = "you have accepted the booking .Customer has been notified ."

        print("Marking taxi as hired in taxis collection")
        restaxis = taxis.update_one({"_id": ObjectId(event['taxiid'])},
                                    {"$set": {"hired": 'Y'}})

        print("get customer email to notify")
        res = bookings.find_one({'_id': ObjectId(event['bookingid'])})
        rescustomer = customers.find_one({'_id': ObjectId(res['customer_id'])})
        print(rescustomer['email'])
        customeremail = rescustomer['email']

        msg = "you have accepted the booking .Customer has been notified ."



    else:
        msg = 'Trip accepted by other driver'

    return {
        'msg': msg,
        'customeremail': customeremail

    }




