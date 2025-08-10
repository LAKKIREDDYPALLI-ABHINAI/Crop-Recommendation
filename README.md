# Crop Recommendation System

This project implements a crop recommendation system using machine learning and provides an easy-to-use Streamlit web interface.

## Features

- Train a Random Forest model to recommend crops based on soil and environmental parameters.
- Perform exploratory data analysis with visualizations.
- Display summary statistics about recommended crops.
- Interactive user interface using Streamlit for real-time crop recommendation.

## Folder Structure

- `data/`: Contains the dataset CSV file.
- `models/`: Stores the trained model and scaler files.
- `src/`: Source code modules for EDA, model training, prediction, and summary.
- `app.py`: Streamlit app interface.
- `main.py`: Python script to launch training or visualization from command line.
- `requirements.txt`: List of Python dependencies.

## Setup & Installation

1. Clone or download this repository.

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Place your dataset CSV file inside the `data/` folder as `Crop_recommendation.csv`.

4. Train the model:
   ```bash
   python main.py train
   ```

5. Perform EDA:
   ```bash
   python main.py eda
   ```

6. Launch the Streamlit app:
   ```bash
   streamlit run app.py
   ```

## Dataset

The dataset should contain the following columns:

- N, P, K: Soil nutrients (Nitrogen, Phosphorus, Potassium)
- temperature: Temperature in °C
- humidity: Humidity in %
- ph: Soil pH
- rainfall: Rainfall in mm
- label: Crop label/name (target)

## Contact

For questions or support, please open an issue or contact the maintainer.


python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python main.py train
streamlit run app.py
