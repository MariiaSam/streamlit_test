import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Назва застосунку
st.title('Демонстрація роботи з даними в Streamlit')

# Завантаження даних
df_data = pd.read_csv('Student_data.csv')

# Вибір колонки для аналізу
column = st.selectbox('Виберіть колонку для аналізу:', df_data.columns)
st.write(f"Описова статистика для колонки '{column}':")
st.write(df_data[column].describe())

# Додаємо заголовок для аналізу прогулів
st.title('Аналіз прогулів студентів')

# Обчислюємо середнє значення GPA для кожної кількості прогулів
average_gpa_per_absence = df_data.groupby('Absences')['GPA'].mean()

# Вибір кількості прогулів на основі середнього GPA
selected_absence = st.sidebar.selectbox(
    'Виберіть кількість прогулів (за середнім GPA):',
    average_gpa_per_absence.index
)

# Фільтруємо дані за вибраним значенням прогулів
filtered_data = df_data[df_data['Absences'] == selected_absence]

# Відображення вибраних даних
st.write(f"Дані для студентів із прогулами {selected_absence}:")
st.write(filtered_data)

# Вибір типу графіка
plot_type = st.sidebar.radio('Виберіть тип графіка:', ['Histogram', 'Boxplot'])

# Генерація вибраного типу графіка
fig, ax = plt.subplots()

if plot_type == 'Histogram':
    ax.hist(filtered_data['GPA'], bins=20, color='blue', edgecolor='black')
    ax.set_xlabel('Середній бал (GPA)')
    ax.set_ylabel('Частота')
    st.write(f'Гістограма GPA для студентів із прогулами {selected_absence}')
elif plot_type == 'Boxplot':
    sns.boxplot(x=filtered_data['Absences'], y=filtered_data['GPA'], ax=ax)
    ax.set_xlabel('Кількість прогулів')
    ax.set_ylabel('Середній бал (GPA)')
    st.write(f'Boxplot GPA для студентів із прогулами {selected_absence}')

# Відображення графіка
st.pyplot(fig)
