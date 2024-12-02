import streamlit as st
import numpy as np
import joblib

rf_model = joblib.load("random_forest_model.pkl")
lr_model = joblib.load("logistic_regression_model.pkl")
svm_model = joblib.load("svm_model.pkl")

def predict_cancer(model, input_data):
    input_data = np.array(input_data).reshape(1, -1) 
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0] if hasattr(model, "predict_proba") else [0.0, 0.0]
    return prediction, probability

def get_features_from_user():
    st.sidebar.header("Введіть характеристики")
    
    radius_mean = st.sidebar.slider("radius_mean", 6.0, 30.0, 15.0)
    texture_mean = st.sidebar.slider("texture_mean", 9.0, 40.0, 20.0)
    perimeter_mean = st.sidebar.slider("perimeter_mean", 40.0, 190.0, 100.0)
    area_mean = st.sidebar.slider("area_mean", 100.0, 2500.0, 700.0)
    smoothness_mean = st.sidebar.slider("smoothness_mean", 0.05, 0.2, 0.1)
    compactness_mean = st.sidebar.slider("compactness_mean", 0.02, 0.3, 0.1)
    concavity_mean = st.sidebar.slider("concavity_mean", 0.0, 0.4, 0.2)
    concave_points_mean = st.sidebar.slider("concave points_mean", 0.0, 0.2, 0.1)
    symmetry_mean = st.sidebar.slider("symmetry_mean", 0.1, 0.3, 0.2)
    fractal_dimension_mean = st.sidebar.slider("fractal_dimension_mean", 0.05, 0.1, 0.08)
    
    radius_se = st.sidebar.slider("radius_se", 0.1, 3.0, 1.0)
    texture_se = st.sidebar.slider("texture_se", 0.1, 5.0, 1.5)
    perimeter_se = st.sidebar.slider("perimeter_se", 0.1, 25.0, 5.0)
    area_se = st.sidebar.slider("area_se", 5.0, 100.0, 50.0)
    smoothness_se = st.sidebar.slider("smoothness_se", 0.001, 0.03, 0.01)
    compactness_se = st.sidebar.slider("compactness_se", 0.005, 0.1, 0.03)
    concavity_se = st.sidebar.slider("concavity_se", 0.0, 0.4, 0.05)
    concave_points_se = st.sidebar.slider("concave points_se", 0.0, 0.05, 0.02)
    symmetry_se = st.sidebar.slider("symmetry_se", 0.005, 0.08, 0.02)
    fractal_dimension_se = st.sidebar.slider("fractal_dimension_se", 0.001, 0.03, 0.01)
    
    radius_worst = st.sidebar.slider("radius_worst", 7.0, 50.0, 20.0)
    texture_worst = st.sidebar.slider("texture_worst", 12.0, 50.0, 25.0)
    perimeter_worst = st.sidebar.slider("perimeter_worst", 50.0, 300.0, 150.0)
    area_worst = st.sidebar.slider("area_worst", 200.0, 4000.0, 1000.0)
    smoothness_worst = st.sidebar.slider("smoothness_worst", 0.1, 0.25, 0.15)
    compactness_worst = st.sidebar.slider("compactness_worst", 0.05, 1.0, 0.2)
    concavity_worst = st.sidebar.slider("concavity_worst", 0.0, 1.0, 0.3)
    concave_points_worst = st.sidebar.slider("concave points_worst", 0.0, 0.2, 0.1)
    symmetry_worst = st.sidebar.slider("symmetry_worst", 0.1, 0.4, 0.25)
    fractal_dimension_worst = st.sidebar.slider("fractal_dimension_worst", 0.05, 0.2, 0.1)
    
    features = [
        radius_mean, texture_mean, perimeter_mean, area_mean, smoothness_mean,
        compactness_mean, concavity_mean, concave_points_mean, symmetry_mean, fractal_dimension_mean,
        radius_se, texture_se, perimeter_se, area_se, smoothness_se,
        compactness_se, concavity_se, concave_points_se, symmetry_se, fractal_dimension_se,
        radius_worst, texture_worst, perimeter_worst, area_worst, smoothness_worst,
        compactness_worst, concavity_worst, concave_points_worst, symmetry_worst, fractal_dimension_worst
    ]
    
    return features

st.title("Класифікація Breast Cancer")

model_option = st.selectbox(
    "Оберіть модель",
    ["Random Forest", "Logistic Regression", "SVM"]
)

model = rf_model if model_option == "Random Forest" else lr_model if model_option == "Logistic Regression" else svm_model

input_data = get_features_from_user()

if st.button("Передбачити"):
    prediction, probability = predict_cancer(model, input_data)
    cancer_type = "Malignant" if prediction == 1 else "Benign"
    st.write(f"**Результат передбачення**: {cancer_type}")
    if hasattr(model, "predict_proba"):
        st.write(f"**Ймовірності класів**: Benign: {probability[0]:.2f}, Malignant: {probability[1]:.2f}")
        st.bar_chart(probability)
    else:
        st.write("Ця модель не підтримує виведення ймовірностей.")
