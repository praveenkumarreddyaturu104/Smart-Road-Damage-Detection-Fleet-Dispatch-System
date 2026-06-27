"""
Priority queue manager.
"""

import heapq


class PriorityQueueManager:
    """
    Manage damage priorities.
    """

    def __init__(self):

        # Create empty heap
        self.heap = []

    def add_damage(
            self,
            priority,
            damage_id):
        """
        Add damage to heap.
        """

        # Negative priority is used because
        # heapq is a min heap
        heapq.heappush(
            self.heap,
            (
                -priority,
                damage_id
            )
        )

    def get_next_damage(self):
        """
        Return highest priority damage.
        """

        if len(self.heap) == 0:

            return None

        priority, damage_id = (
            heapq.heappop(
                self.heap
            )
        )

        return (
            abs(priority),
            damage_id
        )


if __name__ == "__main__":

    queue = PriorityQueueManager()

    queue.add_damage(
        90,
        "D101"
    )

    queue.add_damage(
        60,
        "D102"
    )

    print(
        queue.get_next_damage()
    )