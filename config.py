from os import environ

# Payment in rubles
# Speed in kilometers per hour
# Distance in kilometers, '-1' - not limited
# Time in minutes

car_courier_config = {
    "payment_per_hour": 60,
    "payment_for_the_order": 100,
    "payment_per_kilometer": 5.5,
    "average_speed": 20,
    "distance_restrictions": -1,
    "time_to_rise": 2,
    "parking_time": 5,
}

bike_courier_config = {
    "payment_per_hour": 60,
    "payment_for_the_order": 70,
    "average_speed": 10,
    "distance_restrictions": 5,
    "time_to_rise": 2
}

foot_courier_config = {
    "payment_per_hour": 60,
    "payment_for_the_order": 70,
    "average_speed": 5,
    "distance_restrictions": 2,
    "time_to_rise": 2
}

# In hours
minimum_shift_duration = 4
maximum_shift_duration = 12
average_time_to_delivery = 1
max_time_to_delivery = 2

# In minutes
cooking_time = 25

maximum_orders_per_courier = 3
filepath = environ["PATHCSV"]

city_name = 'Arkhangelsk, Arkhangelsk Oblast, Russian Federation'
