import pandas as pd

df = pd.read_csv("data/air_quality_log.csv")

report = f"""
AIR QUALITY MONITORING REPORT
=============================

Total Readings: {len(df)}

Average AQI: {df['AirQuality'].mean():.2f}

Maximum AQI: {df['AirQuality'].max()}

Minimum AQI: {df['AirQuality'].min()}

Average Temperature: {df['Temperature'].mean():.2f}

Average Humidity: {df['Humidity'].mean():.2f}

Status Distribution:
{df['Status'].value_counts()}

"""

with open(
    "outputs/reports/air_quality_report.txt",
    "w"
) as file:
    file.write(report)

print("Report Generated Successfully")