"""
Severity analysis.
"""


def analyze_severity(
        damage_list):
    """
    Count severity levels.
    """

    summary = {

        "Low": 0,

        "Medium": 0,

        "High": 0,

        "Critical": 0

    }

    for damage in damage_list:

        level = damage[
            "severity_level"
        ]

        summary[level] += 1

    return summary


if __name__ == "__main__":

    damages = [

        {
            "severity_level": "Low"
        },

        {
            "severity_level": "Critical"
        },

        {
            "severity_level": "Critical"
        }

    ]

    result = analyze_severity(
        damages
    )

    print(result)