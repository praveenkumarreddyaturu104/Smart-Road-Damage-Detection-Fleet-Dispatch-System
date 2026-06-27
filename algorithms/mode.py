"""
Node class.
"""


class Node:
    """
    Store location information.
    """

    def __init__(
            self,
            name,
            latitude,
            longitude):

        # Store node name
        self.name = name

        # Store coordinates
        self.latitude = latitude
        self.longitude = longitude

    def display_information(self):
        """
        Display node information.
        """

        print("Location:", self.name)

        print("Latitude:", self.latitude)

        print("Longitude:", self.longitude)