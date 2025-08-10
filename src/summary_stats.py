import pandas as pd

df = pd.read_csv("data/Crop_recommendation.csv")

def summary(crop):
    crop = crop.strip()
    if crop not in df['label'].unique():
        print(f"Crop '{crop}' not found in the dataset!")
        return

    x = df[df['label'] == crop]

    print(f"\nSummary for {crop}")
    print("N (min/avg/max):", x['N'].min(), "/", round(x['N'].mean(), 2), "/", x['N'].max())
    print("P (min/avg/max):", x['P'].min(), "/", round(x['P'].mean(), 2), "/", x['P'].max())
    print("K (min/avg/max):", x['K'].min(), "/", round(x['K'].mean(), 2), "/", x['K'].max())

    print("\nEnvironmental Conditions (min/avg/max):")
    print("Temperature (°C):", round(x['temperature'].min(), 2), "/", round(x['temperature'].mean(), 2), "/", round(x['temperature'].max(), 2))
    print("Humidity (%):", round(x['humidity'].min(), 2), "/", round(x['humidity'].mean(), 2), "/", round(x['humidity'].max(), 2))
    print("Soil pH:", round(x['ph'].min(), 2), "/", round(x['ph'].mean(), 2), "/", round(x['ph'].max(), 2))
    print("Rainfall (mm):", round(x['rainfall'].min(), 2), "/", round(x['rainfall'].mean(), 2), "/", round(x['rainfall'].max(), 2))
