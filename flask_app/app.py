from flask import Flask, render_template, request
import pickle
import numpy as np
from utils import preprocess_user_input

app = Flask(__name__)

# Load model
with open("model/model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        rm = float(request.form['rm'])  # average number of rooms
        lstat = float(request.form['lstat'])  # % lower status of the population
        ptratio = float(request.form['ptratio'])  # pupil-teacher ratio

        features = np.array([[rm, lstat, ptratio]])
        prediction = model.predict(features)[0]

        # Convert to actual dollars
        prediction_in_dollars = prediction * 10000

        return render_template('index.html', prediction=round(prediction_in_dollars, 2))
    except Exception as e:
        return f"Error occurred: {e}"


if __name__ == "__main__":
    app.run(debug=True)
