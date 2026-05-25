# Diabetes Classifier

An end-to-end machine learning pipeline that predicts diabetes risk based on patient health metrics. Trained on the Pima Indians Diabetes dataset with a deployed interactive Streamlit app.

**Live App:** https://jdvwq2mgnasjwfkwthkblw.streamlit.app/  
**Backend API:** Deployed on Render

**NOTE:** First request might take some time to start the backend
---

## Features

- Trained and compared multiple classifiers: Logistic Regression, KNN, and Random Forest
- Full preprocessing pipeline including missing value handling and feature scaling
- Optimized for recall to minimize false negatives in medical prediction
- Saved model and scaler as `.pkl` files for deployment
- Interactive Streamlit app for real-time predictions on new patient data

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Data Processing | Python, pandas, NumPy |
| Modeling | scikit-learn |
| Visualization | matplotlib, seaborn |
| Frontend | Streamlit |
| Deployment | Render, Streamlit Cloud |

---

## Results

| Model | Accuracy | Recall |
|-------|----------|--------|
| Random Forest | **76.9%** | **77.2%** |

Optimized for recall to reduce false negatives — missing a diabetes diagnosis is more costly than a false positive.

---

## How It Works

1. Raw data is loaded from `diabetes.csv` and preprocessed (scaling, null handling)
2. Multiple models are trained and evaluated in `Diabetes.ipynb`
3. Best model (Random Forest) and scaler are exported as `.pkl` files
4. `frontend.py` loads the saved model and serves predictions via Streamlit
5. `main.py` exposes a REST API for programmatic predictions via Render

---

## Project Structure

```
diabetes_classifier/
├── app/
│   ├── frontend.py        # Streamlit app for interactive predictions
│   └── main.py            # FastAPI backend for REST API predictions
├── Diabetes.ipynb         # Full EDA, model training, and evaluation
├── diabetes.csv           # Pima Indians Diabetes dataset (768 rows)
├── model.pkl              # Trained Random Forest model
├── scaler.pkl             # Fitted scaler for input preprocessing
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment config
└── .gitignore
```

---

## Run Locally

```bash
# Clone the repo
git clone https://github.com/vakas100/diabetes_classifier
cd diabetes_classifier

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app/frontend.py

# Or run the FastAPI backend
uvicorn app.main:app --reload
```

---

## Dataset

- **Source:** [Pima Indians Diabetes Dataset](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database) — Kaggle
- **Size:** 768 rows, 8 features
- **Target:** Binary classification (diabetic / non-diabetic)
- **Features:** Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age

---

## Future Improvements

- Add more models (XGBoost, LightGBM) and compare performance
- Implement SHAP values to explain individual predictions
- Collect more diverse training data to reduce dataset bias
- Add input validation and error handling in the API
