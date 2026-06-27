"""
Generate charts.
"""

import matplotlib.pyplot as plt


def create_bar_chart(
        labels,
        values):
    """
    Create bar chart.
    """

    plt.bar(
        labels,
        values
    )

    plt.xlabel(
        "Severity"
    )

    plt.ylabel(
        "Count"
    )

    plt.title(
        "Road Damage Statistics"
    )

    plt.show()


if __name__ == "__main__":

    labels = [

        "Low",

        "Medium",

        "High",

        "Critical"

    ]

    values = [

        12,

        18,

        9,

        4

    ]

    create_bar_chart(
        labels,
        values
    )