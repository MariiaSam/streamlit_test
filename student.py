import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Назва застосунку
st.title('Демонстрація роботи з даними в Streamlit')


df_data = pd.read_csv('Student_data.csv')
column = st.selectbox('Виберіть колонку для аналізу:', df_data.columns)

# Відображення статистики для вибраної колонки
st.write(df_data[column].describe())

# Створення графіку
fig, ax = plt.subplots()
sns.histplot(df_data[column], bins=16, ax=ax)
st.pyplot(fig)

# st.button('Click')
# st.checkbox('Check the checkbox')
# st.radio('Radio Button', [1, 2, 3])
# st.selectbox('Select', [1, 2, 3])
# st.multiselect('Multiselect', [1, 2, 3])
# st.slider('slide', min_value=0, max_value=10)
# st.text_input('Enter Username')
# st.number_input('Enter a Number')
# st.text_area('Enter Text Here!')
# st.date_input('Date Input')
# st.time_input('Time entry')
# st.file_uploader('File Uploader')

# Додаємо заголовок
st.title('Аналіз датасету Student')

# Вибір виду ірису
species = st.sidebar.selectbox('Виберіть вид ірису:', df_data['Age'].unique())

# Вибір типу графіка
plot_type = st.sidebar.radio('Виберіть тип графіка:', ['Histogram', 'Boxplot'])

# Фільтруємо датасет за видом
filtered_data = df_data[df_data['Age'] == species]

# # Генеруємо вибраний тип графіка
# if plot_type == 'Histogram':
#     fig, ax = plt.subplots()
#     ax.hist(filtered_data['petal_length'], bins=20)
#     st.write(f'Гістограма довжини пелюсток для {species}')
#     st.pyplot(fig)
# elif plot_type == 'Boxplot':
#     fig, ax = plt.subplots()
#     sns.boxplot(x=filtered_data['StudentID'], y=filtered_data['petal_length'], ax=ax)
#     st.write(f'Boxplot довжини пелюсток для {species}')
#     st.pyplot(fig)