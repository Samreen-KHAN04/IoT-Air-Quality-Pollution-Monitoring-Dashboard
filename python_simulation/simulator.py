import random
import csv
import time
import requests

from datetime import datetime
from python_simulation.aqi import (
    classify_air_quality,
    get_alert
)

# ==================================
# THINGSPEAK CONFIGURATION
# ==================================

API_KEY = "YFIT39NRMZ5683UV"

CSV_FILE = "data/air_quality_log.csv"

# ==================================
# STATUS MAPPING FOR THINGSPEAK
# ==================================

STATUS_MAP = {
    "GOOD": 1,
    "MODERATE": 2,
    "POOR": 3,
    "HAZARDOUS": 4
}

ALERT_MAP = {
    "NORMAL": 0,
    "ALERT": 1
}


def send_to_thingspeak(
    air_quality,
    temperature,
    humidity,
    status,
    alert
):

    url = "https://api.thingspeak.com/update"

    payload = {
        "api_key": API_KEY,
        "field1": air_quality,
        "field2": temperature,
        "field3": humidity,
        "field4": STATUS_MAP[status],
        "field5": ALERT_MAP[alert]
    }

    try:

        response = requests.get(
            url,
            params=payload,
            timeout=10
        )

        if response.status_code == 200:

            if response.text != "0":
                print("✓ Data uploaded to ThingSpeak")
            else:
                print("⚠ ThingSpeak rejected update")

        else:

            print(
                f"ThingSpeak Error: {response.status_code}"
            )

    except Exception as e:

        print(
            f"Network Error: {e}"
        )


def run_simulation():

    with open(
        CSV_FILE,
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Timestamp",
            "AirQuality",
            "Temperature",
            "Humidity",
            "Status",
            "Alert"
        ])

        print("\n")
        print("=" * 60)
        print("AIR QUALITY MONITORING SIMULATION STARTED")
        print("=" * 60)

        for reading in range(1, 21):

            air_quality = random.choice([
                random.randint(50, 90),
                random.randint(120, 180),
                random.randint(220, 320),
                random.randint(360, 500)
            ])

            temperature = round(
                random.uniform(20, 40),
                1
            )

            humidity = round(
                random.uniform(30, 90),
                1
            )

            status = classify_air_quality(
                air_quality
            )

            alert = get_alert(
                status
            )

            timestamp = datetime.now()

            writer.writerow([
                timestamp,
                air_quality,
                temperature,
                humidity,
                status,
                alert
            ])

            print("\n")
            print(f"Reading #{reading}")
            print("-" * 40)

            print(f"Time        : {timestamp}")
            print(f"AQI         : {air_quality}")
            print(f"Temperature : {temperature} °C")
            print(f"Humidity    : {humidity} %")
            print(f"Status      : {status}")
            print(f"Alert       : {alert}")

            send_to_thingspeak(
                air_quality,
                temperature,
                humidity,
                status,
                alert
            )

            print(
                "Waiting 15 seconds for next upload..."
            )

            time.sleep(0.5)

    print("\n")
    print("=" * 60)
    print("SIMULATION COMPLETED")
    print("=" * 60)


if __name__ == "__main__":
    run_simulation()