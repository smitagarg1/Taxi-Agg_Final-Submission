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

customer_details_lambda.py
customer_registration_lambda.py
latlong_update_lambda.py
taxi_details_lambda.py
taxi_registration_lambda.py


Inside ../deployment/lambda_modules/ 

the deployment package is created for all lambdas along with modules like 'pymongo' which are not supported in aws lambda and have to import specifically from outside 


####### API GATEWAY endpoints which can be accessed :#############################


https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/customer 
GET :  Fetch registerd customers
POST : Register customer 

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/taxi
GET :  Fetch registerd taxis
POST : Register Taxis 

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/booktaxi?name=Mohan
GET :Booking APi with sample params
	This api takes cutomer name as input and fetch the closest taxi based on his location .

Please use following customer names for testing as exception for non-registered user is not handled as part of intermediate deliverables :
-Mohan
-Isaac
-Amir
-Ashok
-Leonard


https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/cleardata
GET : Clear all data from taxis and customers collection 


