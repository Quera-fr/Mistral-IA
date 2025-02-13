import streamlit as st
from openai import OpenAI

st.title("Fine Tuning with OpenAI")

api_key = st.text_input("Your API_KEY")

client = OpenAI(api_key=api_key)

# Préparation des données pour l'entrainement d'un modèle ChatCompletion
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    st.write(uploaded_file)
    bytes_data = uploaded_file.getvalue()

    upload_file = client.files.create(
          file=bytes_data,
          purpose="fine-tune"
        )
