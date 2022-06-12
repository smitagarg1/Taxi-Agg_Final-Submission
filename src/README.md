# cloud-capstone

main data storage = Document DB 

####### Local python files #############################
Inside src/  folder

customer_simulator_data.json - Seed data of 5 customers for user registration simulation 
taxi_simulator_data.json  - Seed data of 50 taxis for taxi registration simulation 

main.py  - Running this file will register taxi and users and insert data to Document DB .It will also fetch the 			registered 	data too via API gateway which in turns calls lambda .Lambda inserts data to Document DB . 				This file internally calls 'TaxiRegistration.py' and 'CustomerRegistration.py'

main2.py  - Running this file will simulate lat/long updation every minute via API gateway which in turns calls lambda 			.Lambda inserts data to Document DB .Infinite loop will run every minute until interrupted to update 		  lat/long data .This file internally calls 'LatLongUpdater.py'


			main2.py also calls 'BoundingBox.py' to generate coordinates of initial area boundary 


APIGatewayUrls.py  : Contains urls/endpoints for API Gateway 



####### AWS Lambda files  #############################
Inside src/lamda  folder

customer_details_lambda.py
customer_registration_lambda.py
latlong_update_lambda.py
taxi_details_lambda.py
taxi_registration_lambda.py


####### API GATEWAY endpoints which can be directly accessed :#############################

https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/customer  => Fetch registerd customers
https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/taxi   =>    Fetch registerd taxis
https://3598y3s21l.execute-api.us-east-1.amazonaws.com/api/booktaxi?name=Mohan   =>Booking APi with sample params



