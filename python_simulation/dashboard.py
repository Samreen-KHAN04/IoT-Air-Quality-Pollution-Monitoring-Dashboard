import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv(
    "data/air_quality_log.csv"
)

plt.figure(figsize=(12,6))

plt.plot(
    df["AirQuality"],
    marker="o"
)

plt.title(
    "Air Quality Trend"
)

plt.xlabel(
    "Reading Number"
)

plt.ylabel(
    "AQI Value"
)

plt.grid(True)

plt.savefig(
    "outputs/charts/air_quality_chart.png"
)

plt.show()