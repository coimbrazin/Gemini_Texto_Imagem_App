import streamlit as st
from gemini import gerar_texto, gerar_imagem

# Configuração da página
st.set_page_config(
    page_title="COIMBRA GENERATOR 🔥",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="expanded",
)

# Adicionar a imagem de fundo
bg_image_url = "https://wallpapers.com/images/featured/simple-clean-8g9017acqfddycrl.jpg"  # Substitua pela URL da imagem desejada
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url({bg_image_url});
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        min-height: 100vh;
    }}
    </style>
    """, 
    unsafe_allow_html=True
)

# Sidebar para seleção
st.sidebar.title("🎛️ Escolha o modo")
modo = st.sidebar.radio("O que você deseja gerar?", ["Texto (Chat)", "Imagem"])

# Título e descrição
st.markdown("# 🔥 COIMBRA GENERATOR")
st.markdown("Gere **textos criativos** ou **imagens realistas** com inteligência artificial.")

# === TEXTO COMO CHAT ===
if modo == "Texto (Chat)":
    st.markdown("## 🗨️ Bate-papo com a IA")
    formato = st.selectbox("📝 Formato da resposta:", ["Texto livre", "Artigo", "Poema", "Resumo", "Crônica", "Argumentativo"])

    # Inicializa histórico de mensagens
    if "chat" not in st.session_state:
        st.session_state.chat = []

    # Caixa de entrada
    user_input = st.text_input("Digite sua pergunta ou comando:")

    if st.button("Enviar") and user_input:
        with st.spinner("Gerando resposta..."):
            resposta = gerar_texto(user_input, formato)
            st.session_state.chat.append(("Você", user_input))
            st.session_state.chat.append(("IA", resposta))

    # Exibe o histórico
    for autor, msg in st.session_state.chat:
        if autor == "Você":
            st.markdown(f"**🧍 {autor}:** {msg}")
        else:
            st.markdown(f"**🤖 {autor}:** {msg}")

# === IMAGEM ===
else:
    st.markdown("## 🎨 Gerador de Imagens")
    prompt = st.text_input("Descreva a imagem que deseja gerar:")

    if st.button("Gerar Imagem"):
        if not prompt:
            st.warning("Por favor, descreva a imagem.")
        else:
            with st.spinner("Gerando imagem..."):
                resultado_imagem = gerar_imagem(prompt)
                if resultado_imagem.startswith("Ocorreu um erro"):
                    st.error(resultado_imagem)
                else:
                    st.image(resultado_imagem, caption="Imagem Gerada pela IA")
