import streamlit as st
from gemini import gerar_texto

def run_app():
    st.set_page_config(page_title="Gerador de Textos IA", page_icon="📝")
    st.title("📝 Gerador de Textos com IA (Gemini)")

    prompt = st.text_area("Escreva seu prompt aqui:", height=200)

    if st.button("Gerar Texto"):
        with st.spinner("Gerando..."):
            resposta = gerar_texto(prompt)
            st.markdown("### ✨ Resultado")
            st.write(resposta)
