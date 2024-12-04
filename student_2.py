import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Назва застосунку
st.title('Демонстрація роботи з даними в Streamlit')

# Завантаження даних
df_data = pd.read_csv('Student_data (1).csv')

column = st.selectbox('Виберіть колонку для аналізу:', df_data.columns)
st.write(f"Описова статистика для колонки '{column}':")
st.write(df_data[column].describe())

#Вивести кореляцію ознак із GradeClass
corr_gradeClass = df_data.corr()['GradeClass']
corr_gradeClass
