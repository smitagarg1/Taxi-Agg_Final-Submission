from pymongo import MongoClient, GEOSPHERE
from bson.son import SON
import pprint
import random
import json


def lambda_handler(event, context):
    # TODO implement
    print("Connecting to Document DB cluster")
    aggregator_cli = MongoClient(
        'mongodb://GLCapstone:GLCapstone@docdb-2022-05-28-11-30-45.cluster-cyw3i89emzkt.us-east-1.docdb.amazonaws.com:27017'
        '/?ssl=true&ssl_ca_certs=rds-combined-ca-bundle.pem&replicaSet=rs0&readPreference=secondaryPreferred'
        '&retryWrites=false')

    aggregator_db = aggregator_cli['taxis_and_customers']
    taxis = aggregator_db['taxis']
    

    customers = aggregator_db['customers']

    x = customers.find_one(event)

    
    #print(x)                        
    customer_loc = x['location']
    
    range_query = {'location': SON([("$near", customer_loc), ("$maxDistance", 1000)])}
    
    doc = taxis.find_one(range_query)
    #print(doc)

    taxiid = doc['name']
    hiredflag = doc['hired']

    while hiredflag == 'n':
        doc = taxis.find_one(range_query)
        hiredflag = doc['hired']
        
        
    print(taxiid)
    print(hiredflag)
    
    taxis.update_one({"name": taxiid},
                    {
                        "$set": {
                        "hired": "y"
                                }
                    })

    aggregator_cli.close()

    #print(customer_loc)

    return {
        'statusCode': 200,
        'body': json.dumps('taxi booked successfully !')
    }