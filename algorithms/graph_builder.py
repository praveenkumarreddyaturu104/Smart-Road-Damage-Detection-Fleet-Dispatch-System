"""
Graph construction.
"""


class Graph:
    """
    Graph representation.
    """

    def __init__(self):

        # Store graph
        self.graph = {}

    def add_node(
            self,
            node):
        """
        Add node.
        """

        if node not in self.graph:

            self.graph[node] = []

    def add_edge(
            self,
            source,
            destination,
            distance):
        """
        Add edge between nodes.
        """

        self.graph[source].append(
            (
                destination,
                distance
            )
        )

    def display_graph(self):
        """
        Print graph.
        """

        for node in self.graph:

            print(
                node,
                "->",
                self.graph[node]
            )


if __name__ == "__main__":

    graph = Graph()

    graph.add_node("A")
    graph.add_node("B")

    graph.add_edge(
        "A",
        "B",
        5
    )

    graph.display_graph()