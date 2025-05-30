# preprocess.py
import pandas as pd
import numpy as np
import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), "model", "model_columns.pkl")
MODEL_COLUMNS = joblib.load(model_path)

def preprocess_user_input(user_input: dict) -> pd.DataFrame:
    """
    Preprocess a single row input for inference to match training preprocessing.
    """
    # Step 1: Convert user input to DataFrame
    df = pd.DataFrame([user_input])

    # Step 2: Fill missing values with median
    df = df.fillna(df.median(numeric_only=True))

    # Step 3: One-hot encode with drop_first
    df = pd.get_dummies(df, drop_first=True)

    # Step 4: Add any missing columns from training, set them to 0
    for col in MODEL_COLUMNS:
        if col not in df.columns:
            df[col] = 0

    # Step 5: Ensure correct column order
    df = df[MODEL_COLUMNS]

    return df
