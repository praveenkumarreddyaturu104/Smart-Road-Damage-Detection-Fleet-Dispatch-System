"""
Edge class.
"""


class Edge:
    """
    Store edge information.
    """

    def __init__(
            self,
            source,
            destination,
            distance):

        # Store source node
        self.source = source

        # Store destination node
        self.destination = destination

        # Store distance
        self.distance = distance

    def display_information(self):
        """
        Print edge information.
        """

        print(
            self.source,
            "->",
            self.destination,
            ":",
            self.distance,
            "km"
        )