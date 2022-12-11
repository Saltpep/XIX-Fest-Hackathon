from abc import ABC

from config import *

from path_finder import CityGraph


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


def main():
    walk_graph = CityGraph(city_name, 'walk', False, 'time')

    origin, distance_to_origin = walk_graph.get_nearest_node((64.54163541632319, 40.53513805881834))
    destination, distance_to_destination = walk_graph.get_nearest_node((64.53597673079206, 40.534853703364995))

    path = walk_graph.shortest_path(origin, destination)

    print(walk_graph.path_length(path))

    route_map = walk_graph.plot_path_folium(path)
    route_map.save("./cache/city_map.html")


if __name__ == '__main__':
    main()
