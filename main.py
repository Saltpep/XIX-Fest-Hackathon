from abc import ABC
from config import *


class Courier(ABC):
    pass


class CarCourier(Courier):
    def __init__(self):
        self.payment_per_hour = car_courier_config.get("payment_per_hour")
        self.payment_for_the_order = car_courier_config.get("payment_for_the_order")
        self.payment_per_kilometer = car_courier_config.get("payment_per_kilometer")
        self.speed = car_courier_config.get("average_speed")


class BikeCourier(Courier):
    def __init__(self):
        self.payment_per_hour = bike_courier_config.get("payment_per_hour")
        self.payment_for_the_order = bike_courier_config.get("payment_for_the_order")
        self.speed = bike_courier_config.get("average_speed")


class FootCourier(Courier):
    def __init__(self):
        self.payment_per_hour = foot_courier_config.get("payment_per_hour")
        self.payment_for_the_order = foot_courier_config.get("payment_for_the_order")
        self.speed = foot_courier_config.get("average_speed")

