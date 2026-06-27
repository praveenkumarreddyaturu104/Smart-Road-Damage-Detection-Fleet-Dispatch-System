"""
Generate reports.
"""

import pandas as pd


def generate_report(
        records):
    """
    Create report.
    """

    dataframe = pd.DataFrame(
        records
    )

    dataframe.to_csv(
        "damage_report.csv",
        index=False
    )

    print(
        "Report generated successfully."
    )


if __name__ == "__main__":

    sample_data = [

        {
            "damage_id": "D101",
            "severity": "High"
        }

    ]

    generate_report(
        sample_data
    )