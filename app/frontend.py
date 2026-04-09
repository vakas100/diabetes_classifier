import streamlit as st
import requests

# ─── Page Config ───────────────────────────────────────────
st.set_page_config(
    page_title="Diabetes Classifier",
    layout="centered"
)

# ─── Custom Styling ────────────────────────────────────────
st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .stButton>button {
            width: 100%;
            background-color: #2563eb;
            color: white;
            font-size: 18px;
            padding: 10px;
            border-radius: 10px;
            border: none;
        }
        .stButton>button:hover {
            background-color: #1d4ed8;
        }
        .result-box {
            padding: 20px;
            border-radius: 12px;
            text-align: center;
            font-size: 22px;
            font-weight: bold;
            margin-top: 20px;
        }
        .diabetic {
            background-color: #fee2e2;
            color: #dc2626;
            border: 2px solid #dc2626;
        }
        .not-diabetic {
            background-color: #dcfce7;
            color: #16a34a;
            border: 2px solid #16a34a;
        }
    </style>
""", unsafe_allow_html=True)

# ─── Header ────────────────────────────────────────────────
st.title("🩺 Diabetes Classifier")
st.markdown("Enter patient details below to predict diabetes risk.")
st.divider()

# ─── Input Form ────────────────────────────────────────────
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=1)
    glucose = st.number_input("Glucose", min_value=0, max_value=300, value=120)
    blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
    skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
    insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5)
    age = st.number_input("Age", min_value=1, max_value=120, value=25)

st.divider()

# ─── Predict Button ────────────────────────────────────────
if st.button("Predict"):

    # Send data to FastAPI backend
    payload = {
        "Pregnancies": pregnancies,
        "Glucose": glucose,
        "BloodPressure": blood_pressure,
        "SkinThickness": skin_thickness,
        "Insulin": insulin,
        "BMI": bmi,
        "DiabetesPedigreeFunction": dpf,
        "Age": age
    }

    try:
        # 🔁 Replace this URL with your Render URL after deployment
        response = requests.post(
            "http://127.0.0.1:8000/docs#/default/predict_predict_post",
            json=payload
        )
        result = response.json()

        if result["prediction"] == 1:
            st.markdown("""
                <div class='result-box diabetic'>
                    High Risk — Diabetic
                </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
                <div class='result-box not-diabetic'>
                    Low Risk — Not Diabetic
                </div>
            """, unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Could not connect to API: {e}")