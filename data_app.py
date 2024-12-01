import streamlit as st

st.button('Click')
st.checkbox('Check the checkbox')
st.radio('Radio Button', [1, 2, 3])
st.selectbox('Select', [1, 2, 3])
st.multiselect('Multiselect', [1, 2, 3])
st.slider('slide', min_value=0, max_value=10)
st.text_input('Enter Username')
st.number_input('Enter a Number')
st.text_area('Enter Text Here!')
st.date_input('Date Input')
st.time_input('Time entry')
st.file_uploader('File Uploader')
