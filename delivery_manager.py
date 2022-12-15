import datetime
from typing import Tuple

import config
from courier import Courier, CarCourier, FootCourier, BikeCourier
from path_finder import CityGraph


class DeliveryTask:
    def __init__(self,
                 origin: 'Tuple[float, float]',
                 destination: 'Tuple[float, float]',
                 created_at: datetime.datetime):
        self.__destination = destination
        self.__origin = origin
        self.__created_at = created_at

    @property
    def origin(self):
        return self.__origin

    @property
    def destination(self):
        return self.__destination

    @property
    def created_at(self):
        return self.__created_at


class DeliveryManager:
    def __init__(self, tasks: 'list[DeliveryTask]' = None):
        if tasks is None:
            tasks = []

        self.__tasks = tasks
        self.__city_walk_graph = CityGraph(config.city_name, 'walk', False)
        self.__city_bike_graph = CityGraph(config.city_name, 'bike', False)
        self.__city_car_graph = CityGraph(config.city_name, 'car', False)

    @property
    def tasks(self):
        return self.__tasks

    def add_task(self, task: DeliveryTask):
        return self.__tasks.append(task)

    def manage_tasks(self):
        pass

    def get_suitable_couriers(self, task: DeliveryTask) -> 'list[Courier]':
        walk_origin = self.__city_walk_graph.get_nearest_node(task.origin)
        walk_destination = self.__city_walk_graph.get_nearest_node(task.destination)

        bike_origin = self.__city_bike_graph.get_nearest_node(task.origin)
        bike_destination = self.__city_bike_graph.get_nearest_node(task.destination)

        walk_path = self.__city_walk_graph.shortest_path(walk_origin, walk_destination)
        bike_path = self.__city_bike_graph.shortest_path(bike_origin, bike_destination)

        walk_path_length = self.__city_walk_graph.path_length(walk_path)
        bike_path_length = self.__city_bike_graph.path_length(bike_path)

        couriers: 'list[Courier]' = [CarCourier()]

        if walk_path_length < config.foot_courier_config:
            couriers.append(FootCourier())
        if bike_path_length < config.bike_courier_config:
            couriers.append(BikeCourier())

        return couriers

    def get_available_actions(self, task: DeliveryTask):
        pass
