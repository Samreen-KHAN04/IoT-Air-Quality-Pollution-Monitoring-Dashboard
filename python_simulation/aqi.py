def classify_air_quality(value):
    """
    AQI Classification
    """

    if value <= 100:
        return "GOOD"

    elif value <= 200:
        return "MODERATE"

    elif value <= 350:
        return "POOR"

    else:
        return "HAZARDOUS"


def get_alert(status):

    if status in ["POOR", "HAZARDOUS"]:
        return "ALERT"

    return "NORMAL"