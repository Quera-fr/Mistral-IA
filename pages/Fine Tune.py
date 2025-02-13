import streamlit as st
from openai import OpenAI

st.title("Fine Tuning with OpenAI")

api_key = st.text_input("Your API_KEY")

client = OpenAI(api_key=api_key)

# Préparation des données pour l'entrainement d'un modèle ChatCompletion
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # Upload du fichier d'entrainement
    upload_file = client.files.create(
          file=uploaded_file.getvalue(),
          purpose="fine-tune"
        )

    # Fine tuning du modèle
    fine_tuned_model = client.fine_tuning.jobs.create(
      training_file=upload_file.id,
      model="gpt-4o-2024-08-06",
      suffix="Streamlit"
    )

model_selected = st.selectbox("Selectionnez un modèle", [client.fine_tuning.jobs.list(limit=10).data[u].fine_tuned_model for u in range(5)])

prompt = st.text_input("Entrez votre texte")

if st.button("Envoyer"):
    completion = client.chat.completions.create(
      model=model_selected,
      messages=[
        {"role": "user", "content": prompt}
      ]
    )
    st.write(completion.choices[0].message.content)
