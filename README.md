Please refre files :
1.Taxi Agg_SURESH NATARAJAN_Final Submission\TestingSteps_result\Testing_Steps_Screenshots
	- for step by step testing
	
2.Taxi Agg_SURESH NATARAJAN_Final Submission\GL_Account_aws_services_setup  (GL account servies details) 
3.Taxi Agg_SURESH NATARAJAN_Final Submission\AWS_Resources_Screenshot		 (GL account servies screesnhsot)
4.Taxi Agg_SURESH NATARAJAN_Final Submission\GLTaxiAgg-BookingandTrackingSystem  (presentation slides)
5.Taxi Agg_SURESH NATARAJAN_Final Submission\Architectural_flow


taxi-aggregator-angular-ui  => UI code
cloud-capstone   => backend code

# cloud-capstone


main data storage = Document DB 

Based on our mentor's advice we did not deploy client code on AWS EC2 instance and have chosen to run locally 

For UI details Please refer 
			-taxi-aggregator-angular-ui/README-taxiaggregator-angular-ui 
			
The architectural flow is as follows
local machine/UI => API gateway => lambda => Document DB 

Please refer ../TestingSteps_result/Testing_Steps_Screenshots.doc for testing flow and results 
####### Local python files #############################
Inside ../src/  folder



customer_simulator_data.json - Seed data of 5 customers for user registration simulation 
taxi_simulator_data.json  - Seed data of 50 taxis for taxi registration simulation 

main.py  - Running this file will register taxi and users and insert data to Document DB .It will also fetch the 		  registered 	data too via API gateway which in turns calls lambda .Lambda inserts data to Document DB . 			This file internally calls 
					-'TaxiRegistration.py'
					-'CustomerRegistration.py'

main2.py  - Running this file will simulate lat/long updation every minute via API gateway which in turns calls lambda 			.Lambda inserts data to Document DB .Infinite loop will run every minute until interrupted to update 		  lat/long data .This file internally calls
					- 'LatLongUpdater.py'
					- 'BoundingBox.py'


			main2.py also calls 'BoundingBox.py' to generate coordinates of initial area boundary .This generates
			min_long,max_long,min_lat and max_lat based on which UI is displayed and seed data was created 


APIGatewayUrls.py  : Contains urls/endpoints for API Gateway 



####### AWS Lambda files  #############################
Inside ..src/lambda  folder the code is maintained for tracking purpose 

1.	clear_data_lambda.py
2.	get_trip_details.py
3.	customer_details_lambda.py
4.	taxi_registration_lambda.py
5.	taxi_acceptservice_lambda.py
6.	taxi_acceptDB_lambda.py
7.	booking_response_service.py
8.	taxi_bookingDB_lambda.py
9.	taxi_bookingService_lambda.py
10.	latlong_update_lambda.py
11.	customer_registration_lambda.py
12.	trip_details_lambda.py
13.	booking_details_lambda.py
14.	taxi_details_lambda.py



Inside ../deployment/lambda_modules/ 

the deployment package is created for all lambdas along with modules like 'pymongo' which are not supported in aws lambda and have to import specifically from outside 
The package can be directly uploade to lambda code 


####### API GATEWAY endpoints which can be accessed :#############################


https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/cleardata
GET

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/taxi
GET
POST

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/customer
GET
POST

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/latlongupdater
POST

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/booktaxi?userid=62a0b257e6a7360da3fc44e2&type=ALL
GET with query params



https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/bookingresponse?bookingid=62a0b9e5d8de0010df60905b&taxiid=62a0b25a9e531b402a65119e&accept=Y
GET with query params

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/bookingdetails
GET


https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/trip
GET
POST