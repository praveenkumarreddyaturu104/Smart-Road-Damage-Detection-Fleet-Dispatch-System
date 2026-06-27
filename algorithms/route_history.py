"""
Store completed route history.
"""


class RouteHistory:
    """
    Route history class.
    """

    def __init__(self):

        # List for history
        self.history = []

    def add_history(
            self,
            route):

        # Save route
        self.history.append(route)

    def show_history(self):

        print("\nRoute History")

        for item in self.history:

            print(item)


if __name__ == "__main__":

    history = RouteHistory()

    history.add_history(
        "Depot -> Road_A -> Road_C"
    )

    history.show_history()