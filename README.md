# Movie Genre Prediction using Machine Learning

## Project Overview

This project is a **Machine Learning-based web application** that predicts the **genre of a movie** based on its **plot summary (text input)**.

The system uses **Natural Language Processing (NLP)** techniques like **TF-IDF** and classification algorithms such as **Naive Bayes / Support Vector Machine (SVM)** to analyze the text and predict the genre.

---

## Features

* Predicts movie genre from plot description
* Uses Machine Learning and NLP techniques
* Simple and interactive web interface
* Supports multiple genres (Action, Comedy, Romance, Horror, etc.)
* Fast and efficient prediction

---

##  Technologies Used

* Python
* Machine Learning (Scikit-learn)
* Natural Language Processing (TF-IDF)
* Flask (Web Framework)
* HTML & CSS (Frontend)

---

##  Project Structure

```
movie_gener_project
│
├── app.py                 # Flask web application
├── train_model.py         # Model training script
├── dataset.csv            # Movie dataset
├── model.pkl              # Trained ML model
├── vectorizer.pkl         # TF-IDF vectorizer
│
├── templates
│   ├── index.html         # Input page
│   └── result.html        # Output page
│
└── static
    └── style.css          # Styling file
```

---

##  Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/movie-genre-prediction.git
cd movie-genre-prediction
```

### 2️⃣ Install Dependencies

```
pip install pandas scikit-learn flask
```

### 3️⃣ Train the Model

```
python train_model.py
```

### 4️⃣ Run the Application

```
python app.py
```

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

##  How It Works

1. User enters a movie plot (text)
2. Text is converted into numerical features using TF-IDF
3. Machine Learning model analyzes the features
4. Model predicts the movie genre
5. Result is displayed on the web page

---

## 🧪 Example Input

```
A detective investigates a mysterious murder case and uncovers a dangerous conspiracy.
```

### Output:

```
Thriller
```

---

##  Model Performance

* Algorithm: Naive Bayes / SVM
* Accuracy: ~60% to 75% (depends on dataset)

---

##  Future Improvements

* Use deep learning models (LSTM, BERT)
* Improve dataset quality
* Add multiple genre prediction
* Enhance UI design

---

##  Applications

* Movie recommendation systems
* Streaming platforms
* Content classification
* Search engines

---

##  Author

* Puli Madhavi

---

##  License

This project is for educational purposes.
