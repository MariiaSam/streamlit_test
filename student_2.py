import streamlit as st
import joblib

# Назва застосунку
st.title("Передбачення класу студента за допомогою моделей ML")

# Завантаження моделей
@st.cache_resource
def load_models():
    svm_model = joblib.load("student_svm_model.pkl")
    rf_model = joblib.load("random_forest_model.pkl")
    lr_model = joblib.load("logistic_regression_model.pkl")
    return svm_model, rf_model, lr_model

svm_model, rf_model, lr_model = load_models()

# Інтерфейс для вибору моделі
model_option = st.selectbox(
    "Оберіть модель для передбачення",
    ("SVM", "Random Forest", "Logistic Regression")
)

selected_model = {
    "SVM": svm_model,
    "Random Forest": rf_model,
    "Logistic Regression": lr_model
}[model_option]

# Введення характеристик користувачем
st.sidebar.header("Введіть характеристики студента")

studentId = st.sidebar.slider("StudentID")
age = st.sidebar.slider("Age", 10, 25, 18)
gender = st.sidebar.selectbox("Gender", [1, 0])  # 1: Male, 0: Female
ethnicity = st.sidebar.slider("Ethnicity (0-4)", 0, 4, 0)
parental_education = st.sidebar.slider("Parental Education (0-3)", 0, 3, 2)
study_time_weekly = st.sidebar.slider("Study Time Weekly", 0.0, 40.0, 15.0)
absences = st.sidebar.slider("Absences", 0, 30, 5)
tutoring = st.sidebar.selectbox("Tutoring", [1, 0])
parental_support = st.sidebar.slider("Parental Support (0-4)", 0, 4, 2)
extracurricular = st.sidebar.slider("Extracurricular (0-1)", 0, 1, 0)
sports = st.sidebar.slider("Sports (0-1)", 0, 1, 0)
music = st.sidebar.slider("Music (0-1)", 0, 1, 0)
volunteering = st.sidebar.slider("Volunteering (0-1)", 0, 1, 0)
gpa = st.sidebar.slider("GPA", 0.0, 4.0, 3.0)

# Формування вхідних характеристик
features = [
    studentId, age, gender, ethnicity, parental_education, study_time_weekly,
    absences, tutoring, parental_support, extracurricular, sports,
    music, volunteering, gpa
]

# Передбачення
if st.button("Передбачити"):
    prediction = selected_model.predict([features])[0]
    probabilities = selected_model.predict_proba([features])[0]

    st.write(f"## Результат передбачення за моделлю **{model_option}**")
    st.write(f"Передбачений клас: **GradeClass {prediction}**")

    st.write("### Ймовірності для кожного класу:")
    st.bar_chart(probabilities)
