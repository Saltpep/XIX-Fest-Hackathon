from abc import ABC, abstractmethod

from config import car_courier_config, bike_courier_config, foot_courier_config


class Courier(ABC):
    @abstractmethod
    @property
    def map_type(self) -> str:
        """ map type """

    @abstractmethod
    @property
    def travel_speed(self) -> float:
        """ travel speed"""

    @abstractmethod
    def travel_time(self, path_length: float) -> float:
        """ travel time"""


class CarCourier(Courier):
    def __init__(self):
        self.payment_per_hour = car_courier_config.get("payment_per_hour")
        self.payment_for_the_order = car_courier_config.get("payment_for_the_order")
        self.payment_per_kilometer = car_courier_config.get("payment_per_kilometer")
        self.speed = car_courier_config.get("average_speed")
        self.__map_type = 'car'

    @property
    def map_type(self) -> str:
        return self.__map_type

    @property
    def travel_speed(self) -> float:
        return self.speed

    def travel_time(self, path_length: float):
        return path_length / self.travel_speed


class BikeCourier(Courier):
    def __init__(self):
        self.payment_per_hour = bike_courier_config.get("payment_per_hour")
        self.payment_for_the_order = bike_courier_config.get("payment_for_the_order")
        self.speed = bike_courier_config.get("average_speed")
        self.__map_type = 'bike'

    @property
    def map_type(self) -> str:
        return self.__map_type

    @property
    def travel_speed(self) -> float:
        return self.speed

    def travel_time(self, path_length: float):
        return path_length / self.travel_speed


class FootCourier(Courier):
    def __init__(self):
        self.payment_per_hour = foot_courier_config.get("payment_per_hour")
        self.payment_for_the_order = foot_courier_config.get("payment_for_the_order")
        self.speed = foot_courier_config.get("average_speed")
        self.__map_type = 'walk'

    @property
    def map_type(self) -> str:
        return self.__map_type

    @property
    def travel_speed(self) -> float:
        return self.speed

    def travel_time(self, path_length: float):
        return path_length / self.travel_speed
