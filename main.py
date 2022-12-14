from config import *
from path_finder import CityGraph


def main():
    walk_graph = CityGraph(city_name, 'walk', False, 'time')

    origin, distance_to_origin = walk_graph.get_nearest_node((64.54163541632319, 40.53513805881834))
    destination, distance_to_destination = walk_graph.get_nearest_node((64.53597673079206, 40.534853703364995))

    path = walk_graph.shortest_path(origin, destination)

    walk_graph.save_html_map(path, './cache/city_map.html')


if __name__ == '__main__':
    main()
