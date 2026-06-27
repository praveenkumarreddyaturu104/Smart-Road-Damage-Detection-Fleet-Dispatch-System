"""
Repair queue.
"""


class RepairQueue:
    """
    Store repair order.
    """

    def __init__(self):

        self.queue = []

    def add_repair(
            self,
            damage_id):

        self.queue.append(
            damage_id
        )

    def display_queue(
            self):

        print(
            "\nRepair Queue"
        )

        for damage in self.queue:

            print(damage)


if __name__ == "__main__":

    repair_queue = RepairQueue()

    repair_queue.add_repair(
        "D101"
    )

    repair_queue.add_repair(
        "D102"
    )

    repair_queue.display_queue()