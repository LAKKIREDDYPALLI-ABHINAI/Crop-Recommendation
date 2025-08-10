import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
import joblib
MODEL_DIR = "models"

def train_model():
    df = pd.read_csv('data/Crop_recommendation.csv')

    X = df.drop('label', axis=1)
    y = df['label']

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = RandomForestClassifier(random_state=42)
    model.fit(X_scaled, y)

    joblib.dump(model, 'models/crop_model.pkl')
    joblib.dump(scaler, 'models/scaler.pkl')

    print("Model and scaler saved to 'models/' folder.")
