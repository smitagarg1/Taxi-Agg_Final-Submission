from src.LatLongUpdater import LatLongUpdater
from src.BoundingBox import BoundingBox
import numpy as np

bbox=BoundingBox()

box=bbox.get_bounding_box(12.931656,77.622696,10)

#generate random lat long inside bounding area
#for i in range(5):
 #   x_t = np.random.uniform(box.lat_min, box.lat_max)
 #   y_t = np.random.uniform(box.lon_min, box.lon_max)
 #   x_t=round(x_t,4)
 #   y_t=round(y_t,4)
 #   print(x_t,",",y_t)

#Lat long Simulator
print("Simulating per minute latlong update")
lat_long_updater = LatLongUpdater()
lat_long_updater.lat_long_updater()

