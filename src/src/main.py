from datetime import datetime

from src.CustomerRegistration import CustomerRegistration
from src.LatLongUpdater import LatLongUpdater
from src.TaxiRegistration import TaxiRegistration

# Simulating registration of 5 users
print("Simulating registration of 5 users")
Customer_registration = CustomerRegistration()
print(Customer_registration.customer_register_simulator())

print("\n\nFetching Customer Details")
print(Customer_registration.customer_details())

# Simulating registration of 50 taxis
print("\n\nSimulating registration of 50 taxis")
taxi_registration = TaxiRegistration()
print(taxi_registration.taxi_register_simulator())


print("\n\nFetching Taxi Details")
print(taxi_registration.taxi_details())
