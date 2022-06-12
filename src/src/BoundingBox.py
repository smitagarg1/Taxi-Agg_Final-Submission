import math

#This class was used to generate bounding area
class BoundingBox():
    def __init__(self, *args, **kwargs):
        self.lat_min = None
        self.lon_min = None
        self.lat_max = None
        self.lon_max = None



    def get_bounding_box(self,latitude_in_degrees, longitude_in_degrees, half_side_in_miles):
        assert half_side_in_miles > 0
        assert latitude_in_degrees >= -90.0 and latitude_in_degrees  <= 90.0
        assert longitude_in_degrees >= -180.0 and longitude_in_degrees <= 180.0

        half_side_in_km = half_side_in_miles * 1.609344
        lat = math.radians(latitude_in_degrees)
        lon = math.radians(longitude_in_degrees)

        radius  = 6371
        # Radius of the parallel at given latitude
        parallel_radius = radius*math.cos(lat)

        lat_min = lat - half_side_in_km/radius
        lat_max = lat + half_side_in_km/radius
        lon_min = lon - half_side_in_km/parallel_radius
        lon_max = lon + half_side_in_km/parallel_radius
        rad2deg = math.degrees

        box = BoundingBox()
        box.lat_min = rad2deg(lat_min)
        box.lon_min = rad2deg(lon_min)
        box.lat_max = rad2deg(lat_max)
        box.lon_max = rad2deg(lon_max)

        print("Min Lat : ",box.lat_min)
        print("Min Lon :",box.lon_min)
        print("Max Lat :",box.lat_max )
        print("Max Lon :",box.lon_max)


        return (box)

        # function to get value of _age

    def get_age(self):
        print("getter method called")
        return self._age

        # function to set value of _age

    def set_setProperties(self, lat_min,lon_min,lat_max,lon_max):
        self.lat_min=lat_min
        self.lon_min=lon_min
        self.lat_max=lat_max
        self.lon_max=lon_max