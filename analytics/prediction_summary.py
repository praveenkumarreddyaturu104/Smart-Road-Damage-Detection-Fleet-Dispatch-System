"""
Prediction summary.
"""


def generate_summary(
        total_images,
        detected_images):
    """
    Generate summary.
    """

    accuracy = (

        detected_images /
        total_images

    ) * 100

    return {

        "total_images": total_images,

        "detected_images": detected_images,

        "success_rate": round(
            accuracy,
            2
        )

    }


if __name__ == "__main__":

    summary = generate_summary(
        500,
        465
    )

    print(summary)