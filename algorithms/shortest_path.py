"""
Find shortest route.
"""

from dijkstra import dijkstra


def get_shortest_path(
        graph,
        start_node,
        end_node):
    """
    Return shortest distance.
    """

    distances = dijkstra(
        graph,
        start_node
    )

    return distances[end_node]


if __name__ == "__main__":

    graph = {
        "Depot": [
            ("Road_A", 3),
            ("Road_B", 7)
        ],

        "Road_A": [
            ("Road_C", 4)
        ],

        "Road_B": [
            ("Road_C", 2)
        ],

        "Road_C": []
    }

    distance = get_shortest_path(
        graph,
        "Depot",
        "Road_C"
    )

    print(
        "Shortest distance:",
        distance
    )