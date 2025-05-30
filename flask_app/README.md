# 🏠 Housing Price Prediction App

A Flask web application that predicts house prices based on features like average number of rooms, % lower status of the population, and pupil-teacher ratio. The model is trained on the Boston Housing dataset.

---

## 🚀 Features

- Predicts house prices in **USD ($)**
- Uses a trained `LinearRegression` model
- Simple HTML form for user input
- Preprocessing handled before prediction

---

## 📁 Project Structure

```
flask_house_price_app/
│
├── model/
│   └── model.pkl                # Trained model
│
├── templates/
│   └── index.html               # User input form
│   └── result.html              # Prediction display
│
├── app.py                       # Main Flask app
├── utils.py                     # (Optional) Preprocessing functions
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

---

## 🧰 Requirements

- Python 3.7+
- `pip`

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/flask_house_price_app.git
   cd flask_house_price_app
   ```

2. **Create virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Make sure the model file is present:**
   Ensure `model/model.pkl` exists. If not, train your model using your notebook or separate script.

5. **Run the Flask app:**
   ```bash
   python app.py
   ```

6. **Access it in your browser:**
   ```
   http://127.0.0.1:5000/
   ```

---

## 📝 Usage

- Enter:
  - Average number of rooms
  - % lower status of the population
  - Pupil-teacher ratio
- Click **Predict Price**
- View the predicted house price in **USD**

---

## 📚 Dataset Used

[Boston Housing Dataset](https://www.kaggle.com/datasets/schirmerchad/bostonhoustingmlnd)

---

## 📌 Notes

- Make sure the input fields in `index.html` match the variable names in `app.py`.
- The prediction is scaled to dollars by multiplying by 1000.

---

## 📬 Contact

Feel free to reach out if you need help integrating other features or improving the model.