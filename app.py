from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    plot = request.form["plot"]

    plot_vector = vectorizer.transform([plot])

    prediction = model.predict(plot_vector)

    return render_template("index.html", prediction=prediction[0])

if __name__ == "__main__":
    app.run(debug=True)