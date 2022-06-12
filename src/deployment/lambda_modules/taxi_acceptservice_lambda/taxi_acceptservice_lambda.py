import boto3
import json
from email.mime.text import MIMEText
from botocore.exceptions import ClientError
from bson import json_util


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
    inputParams = {
        "bookingid": event['bookingid'],
        "taxiid": event['taxiid'],
        "accept": event['accept']
    }
    clientLambda = boto3.client('lambda')
    response = clientLambda.invoke(
        FunctionName='arn:aws:lambda:us-east-1:202217686242:function:taxi_acceptDB_lambda',
        InvocationType='RequestResponse',
        Payload=json.dumps(inputParams)
    )

    responseFromChild = json.load(response['Payload'])
    print(responseFromChild)

    print('\n')
    print("msg : ", responseFromChild['msg'])
    print("customeremail :", responseFromChild['customeremail'])

    txt = "Your booking has been accpeted by taxi " + event['taxiid']
    BODY_HTML = """<html>
                <head></head>
                    <body>
                        <h1>Booking Accepted</h1>

                            '""" + txt + """'


                        </p>
                    </body>
                        </html>
                    """
    print(BODY_HTML)
    recipient = responseFromChild['customeremail']
    print(recipient)
    if not len(recipient) == 0:
        sendAlerts(recipient, BODY_HTML)

    return {
        'msg': responseFromChild['msg']

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