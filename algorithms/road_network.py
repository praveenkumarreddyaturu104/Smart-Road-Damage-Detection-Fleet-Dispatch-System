"""
Road network.
"""

from graph_builder import Graph


def build_road_network():
    """
    Build graph.
    """

    graph = Graph()

    # Add locations
    graph.add_node("Depot")
    graph.add_node("Road_A")
    graph.add_node("Road_B")
    graph.add_node("Road_C")

    # Add distances
    graph.add_edge(
        "Depot",
        "Road_A",
        3
    )

    graph.add_edge(
        "Road_A",
        "Road_B",
        5
    )

    graph.add_edge(
        "Road_B",
        "Road_C",
        2
    )

    graph.add_edge(
        "Road_C",
        "Depot",
        7
    )

    return graph


if __name__ == "__main__":

    network = build_road_network()

    network.display_graph()