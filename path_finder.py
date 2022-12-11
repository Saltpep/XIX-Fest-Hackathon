from typing import Any, Tuple

import osmnx
import networkx


class CityGraph:
    def __init__(self, place: str, network_type: str, simplify: bool, optimize_for: str = 'time'):
        self.__graph = osmnx.graph_from_place(place, network_type=network_type, simplify=simplify)
        self.__optimize_for = optimize_for

    @property
    def optimizer(self) -> str:
        return self.__optimize_for

    @optimizer.setter
    def optimizer(self, value: str):
        self.__optimize_for = value

    @property
    def graph(self) -> networkx.MultiDiGraph:
        return self.__graph

    def get_nearest_node(self, coordinate: 'Tuple[float, float]') -> \
            tuple[int | list[int] | list, Any] | int | list[int] | list:
        return osmnx.nearest_nodes(self.__graph, coordinate[1], coordinate[0], True)

    def shortest_path(self, origin_node: int, destination_node: int, method: str = 'dijkstra') -> 'list[int]':
        return networkx.shortest_path(self.__graph, origin_node, destination_node,
                                      weight=self.__optimize_for, method=method)

    def plot_path_folium(self, shortest_path: 'list[int]', tiles: str = 'openstreetmap'):
        return osmnx.plot_route_folium(self.__graph, shortest_path, tiles=tiles)

    def plot_static_graph(self, shortest_path: 'list[int]'):
        return osmnx.plot_graph_route(self.__graph, shortest_path, save=True)

    # TODO: Refactor?
    def path_length(self, path: 'list[int]') -> float:
        assert len(path) > 1
        length = 0
        for i in range(0, len(path) - 1):
            edge_data: 'dict[int, dict[str, Any]]' = self.__graph.get_edge_data(path[i], path[i + 1])
            edge_length: float = edge_data.get(0).get('length')
            length += edge_length
        return length


if __name__ == 'path_finder':
    osmnx.config(log_console=True, use_cache=True)
