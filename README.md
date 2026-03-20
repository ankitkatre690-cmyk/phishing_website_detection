# 🛡️ Phishing Website Detection System

An end-to-end Machine Learning project that detects whether a website is **phishing or legitimate** using URL-based features and provides explainability using SHAP.

---

## 🚀 Project Overview

Phishing attacks are one of the most common cybersecurity threats. This project builds a **real-time phishing detection system** that:

* Accepts a website URL
* Extracts important features
* Predicts whether the site is phishing or legitimate
* Explains the prediction using SHAP

---

## 🎯 Features

* 🔍 Real-time URL analysis
* 🤖 Machine Learning model (Random Forest)
* 📊 SHAP explainability (Waterfall, Bar, Force plots)
* 🌐 Streamlit interactive UI
* ⚡ Fast and lightweight prediction

---

## 🧠 Tech Stack

* Python
* Pandas, NumPy
* Scikit-learn
* Streamlit
* SHAP
* Matplotlib
* Joblib

---

## 📂 Project Structure

```
phishing-website-detection/
│
├── data/
│   └── phishing.csv
│
├── models/
│   ├── phishing_model.pkl
│   └── features.pkl
│
├── notebooks/
│   └── eda.ipynb
│
├── src/
│   ├── train.py
│   ├── predict.py
│   └── feature_extraction.py
│
├── streamlit_app.py
├── requirements.txt
└── README.md
```

---

1.⚙️ Installation



2. Install dependencies:

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### 🔹 Train the Model

```
python src/train.py
```

---

### 🔹 Run Streamlit App

```
streamlit run streamlit_app.py
```

Open in browser:

```
http://localhost:8501
```

---

## 🔍 How It Works

1. User enters a URL
2. Features are extracted (URL length, dots, digits, etc.)
3. Machine Learning model predicts phishing or legitimate
4. SHAP explains the prediction

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Problem Type: Binary Classification
* Target Variable: `status` (Phishing / Legitimate)

---

## 🔬 Explainability (SHAP)

This project uses SHAP to provide:

* 🔹 Waterfall plot (individual prediction explanation)
* 🔹 Feature importance (global)
* 🔹 Beeswarm plot (feature distribution)
* 🔹 Force plot (interactive explanation)

---

## 📈 Example Output

* 🚨 Phishing Website (Confidence: 0.92)
* ✅ Legitimate Website (Confidence: 0.87)

---

## 💼 Use Cases

* Cybersecurity systems
* Browser extensions for phishing detection
* Fraud detection platforms
* Financial security systems

---

## 🚀 Future Improvements

* Real-time WHOIS API integration (domain age)
* Web scraping for content-based features
* Model upgrade (XGBoost, LightGBM)
* Cloud deployment & monitoring

---

## 👨‍💻 Author

**Ankit Katre**
Machine Learning & Data Science Enthusiast

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
