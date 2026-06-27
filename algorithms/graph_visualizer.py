"""
Visualize graph.
"""

import networkx as nx
import matplotlib.pyplot as plt


def visualize_graph(graph):
    """
    Draw graph.
    """

    G = nx.Graph()

    # Loop through graph
    for source in graph.graph:

        for destination, distance in graph.graph[source]:

            G.add_edge(
                source,
                destination,
                weight=distance
            )

    # Draw graph
    nx.draw(
        G,
        with_labels=True
    )

    plt.show()