import streamlit as st

st.title("Fine Tune OpenAI")


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    st.write(uploaded_file)
    bytes_data = uploaded_file.getvalue()
