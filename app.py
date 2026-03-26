from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("fraud_model.pkl","rb"))
scaler = pickle.load(open("scaler.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    try:
        time_hours = float(request.form["time"])
        amount = float(request.form["amount"])

        # convert hours → seconds
        time_seconds = time_hours * 3600

        input_data = np.array([[time_seconds, amount]])

        input_scaled = scaler.transform(input_data)

        prediction = model.predict(input_scaled)

        if prediction[0] == 1:
            result = "Fraudulent Transaction"
        else:
            result = "Legitimate Transaction"

    except Exception as e:
        result = str(e)

    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)