# Credit Card Fraud Detection Web App

##  Overview

This project is a **Machine Learning-based web application** that predicts whether a credit card transaction is **fraudulent or legitimate**.

It uses a **Random Forest Classifier** trained on transaction data and a **Flask web interface** for user interaction.

---

##  Objective

* Detect fraudulent credit card transactions
* Provide real-time predictions
* Build a simple ML-powered web application

---

##  Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas, NumPy
* HTML, CSS

---

##  Project Structure

```
credit_card_fraud_detection/
│
├── app.py
├── train_model.py
├── fraud_model.pkl
├── scaler.pkl
├── creditcard.csv
│
├── templates/
│   └── index.html
│
└── static/
    └── style.css
```

---

##  How It Works

1. User enters:

   * Transaction Time (in hours)
   * Transaction Amount

2. System:

   * Converts time from hours → seconds
   * Scales input data
   * Uses trained ML model for prediction

3. Output:

   *  Legitimate Transaction
   * Fraudulent Transaction

---

##  Setup Instructions

### 1. Clone Repository

```
git clone https://github.com/your-username/credit-card-fraud-detection.git
cd credit-card-fraud-detection
```

### 2. Install Dependencies

```
pip install pandas numpy scikit-learn flask
```

### 3. Train Model

```
python train_model.py
```

### 4. Run Application

```
python app.py
```

### 5. Open Browser

```
http://127.0.0.1:5000/
```

---

##  Sample Input

| Time (hours) | Amount |
| ------------ | ------ |
| 2            | 500    |
| 5            | 2000   |

---

## Output

* Legitimate Transaction
* Fraudulent Transaction

---

##  Machine Learning Model

* Algorithm: Random Forest
* Features Used:

  * Transaction Time (`unix_time`)
  * Transaction Amount (`amt`)

---

##  Features

* Simple UI
* Fast predictions
* Easy to use
* Beginner-friendly project

---

##  Future Enhancements

* Add more input features
* Improve model accuracy
* Deploy online
* Add dashboard visualization

---

## Author
Puli Madhavi

---

##Conclusion

This project shows how **Machine Learning and Flask** can be used together to build a real-world fraud detection system.

---
