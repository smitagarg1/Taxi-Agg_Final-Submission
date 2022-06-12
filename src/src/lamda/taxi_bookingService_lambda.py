import boto3
import json
from email.mime.text import MIMEText
from botocore.exceptions import ClientError
from bson import json_util

API_GATEWAY_BOOKING_RESPONSE = 'https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/bookingresponse'

SENDER = "suraj.nsit@gmail.com"
AWS_REGION = "us-east-1"
SUBJECT = "Booking request"

# The email body for recipients with non-HTML email clients.
BODY_TEXT = ("Amazon SES Test (Python)\r\n"
             "This email was sent with Amazon SES using the "
             "AWS SDK for Python (Boto)."
             )

# The HTML body of the email.


CHARSET = "UTF-8"

clientses = boto3.client('ses', region_name=AWS_REGION)


def lambda_handler(event, context):
    msg = ''
    print("User id is ", event['userid'])
    inputParams = {
        "userid": event['userid'],
        "type": event['type']
    }
    clientLambda = boto3.client('lambda')
    response = clientLambda.invoke(
        FunctionName='arn:aws:lambda:us-east-1:202217686242:function:taxi_bookingDB_lambda',
        InvocationType='RequestResponse',
        Payload=json.dumps(inputParams)
    )

    responseFromChild = json.load(response['Payload'])

    print('\n')
    print("bookingId : ", responseFromChild['bookingId'])
    if responseFromChild['bookingId'] == -1:
        msg = "No taxis found in your area"

    taxiList = json_util.loads(responseFromChild['taxiList'])
    for rec in taxiList:
        taxi_id = str(rec['_id'])
        accept = API_GATEWAY_BOOKING_RESPONSE + "?bookingid=" + responseFromChild[
            'bookingId'] + "&taxiid=" + taxi_id + "&accept=Y"
        deny = API_GATEWAY_BOOKING_RESPONSE + "?bookingid=" + responseFromChild[
            'bookingId'] + "&taxiid=" + taxi_id + "&accept=N"
        BODY_HTML = """<html>
                <head></head>
                    <body>
                        <h1>Booking request</h1>
                         <p>There is a booking request
                            <a href='""" + accept + """'>Accept Booking</a> 
                            <a href='""" + deny + """'>Deny Booking</a> 
                        </p>
                    </body>
                        </html>
                    """
        print(BODY_HTML)
        recipient = rec['email']
        print(recipient)
        sendAlerts(recipient, BODY_HTML)

        msg = "Booking recieved .Your booking id is " + responseFromChild[
            'bookingId'] + " .You will soon receive alert with taxi details "

    return {
        'statusCode': 200,
        'body': json.dumps(msg)
    }


def sendAlerts(recipient, BODY_HTML):
    try:
        # Provide the contents of the email.
        response = clientses.send_email(
            Destination={
                'ToAddresses': [
                    recipient,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    # Display an error if something goes wrong.
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        print("Email sent! Message ID:"),
        print(response['MessageId'])