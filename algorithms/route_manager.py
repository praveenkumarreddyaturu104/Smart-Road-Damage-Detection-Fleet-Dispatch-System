"""
Manage repair routes.
"""


class RouteManager:
    """
    Store route details.
    """

    def __init__(self):

        # List of routes
        self.routes = []

    def add_route(
            self,
            source,
            destination):

        # Save route
        self.routes.append(
            (
                source,
                destination
            )
        )

    def display_routes(self):

        print("\nRepair Routes")

        for route in self.routes:

            print(
                route[0],
                "->",
                route[1]
            )


if __name__ == "__main__":

    manager = RouteManager()

    manager.add_route(
        "Depot",
        "Road_A"
    )

    manager.add_route(
        "Road_A",
        "Road_C"
    )

    manager.display_routes()