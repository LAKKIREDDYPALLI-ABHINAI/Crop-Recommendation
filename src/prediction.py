import pandas as pd
import joblib

model = joblib.load("models/crop_model.pkl")
scaler = joblib.load("models/scaler.pkl")

def recommend_crop(N, P, K, temperature, humidity, ph, rainfall):
    input_df = pd.DataFrame([[N, P, K, temperature, humidity, ph, rainfall]],
                            columns=['N', 'P', 'K', 'temperature', 'humidity', 'ph', 'rainfall'])

    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)
    return prediction[0]
