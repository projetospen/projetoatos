import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="Meu App de IA", layout="centered")
st.title("🤖 Meu Aplicativo com Gemini")

# Pega a chave das variáveis secretas da hospedagem
genai.configure(api_key=os.environ["AQ.Ab8RN6I69LIGDldB9vuTg-SQ-lfOQXKE0JO4EGE87Wq9uK0B0w"])
model = genai.GenerativeModel("gemini-3.8-flash") # ou o modelo que você escolheu

pergunta = st.text_input("Digite sua mensagem:")
if st.button("Enviar"):
    resposta = model.generate_content(pergunta)
    st.write(resposta.text)