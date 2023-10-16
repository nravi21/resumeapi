
import streamlit as st
import requests

st.title('Resume Parser')

resume_text = st.text_area('Paste your resume text here:')

if st.button('Parse Resume'):
    response = requests.post('http://localhost:5000/parse_resume', json={'text': resume_text})
    entities = response.json()
    st.write('Parsed Entities:', entities)
