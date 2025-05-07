import streamlit as st
from gemini import gerar_texto, gerar_imagem

# Configuração da página
st.set_page_config(
    page_title="COIMBRA GENERATOR 🔥",
    page_icon="🔥",
    layout="centered",
    initial_sidebar_state="auto",
)

# Fundo personalizado com imagem via URL
BACKGROUND_IMAGE_URL = "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2Fwallpapers%2Fcomments%2F106ubm6%2Fdesktop_aesthetic_wallpaper_19201080%2F%3Ftl%3Dpt-br&psig=AOvVaw3nVCHjl7AB1gRVxxKvhgQd&ust=1746126985575000&source=images&cd=vfe&opi=89978449&ved=0CBQQjRxqFwoTCJD3uYi8gI0DFQAAAAAdAAAAABAE"  # <-- troque aqui se quiser outro

st.markdown(f"""
    <style>
    .stApp {{
        background-image: url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-attachment: fixed;
        background-position: center;
    }}
    .main {{
        background-color: rgba(255, 255, 255, 0.9);
        padding: 2rem;
        border-radius: 20px;
    }}
    h1, h2, h3 {{
        color: #4B0082;
        text-shadow: 1px 1px 2px #ccc;
    }}
    .stButton > button {{
        background-color: #4B0082;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        font-size: 16px;
        border: none;
    }}
    .stTextArea, .stTextInput {{
        border-radius: 8px !important;
    }}
    </style>
""", unsafe_allow_html=True)

# Título
st.markdown("# 🔥 COIMBRA GENERATOR")
st.markdown("Gere **textos criativos** ou **imagens realistas** com inteligência artificial.")

# Escolha entre texto ou imagem
modo = st.radio("Escolha o que deseja gerar:", ["Texto", "Imagem"])

# Se for gerar texto
if modo == "Texto":
    tema = st.text_input("📌 Digite um tema para o texto:", placeholder="Ex: Faça uma receita")
    formato = st.selectbox("📝 Escolha o formato do texto:", ["Texto livre", "Artigo", "Poema", "Resumo", "Crônica", "Argumentativo"])
    if st.button("🚀 Gerar Texto"):
        if not tema:
            st.warning("Por favor, insira um tema.")
        else:
            with st.spinner("Gerando texto..."):
                resultado = gerar_texto(tema, formato)
                st.success("✅ Texto gerado com sucesso!")
                st.text_area("📄 Resultado:", resultado, height=300)

# Se for gerar imagem
else:
    prompt = st.text_input("🎨 Descreva a imagem que deseja gerar:", placeholder="Ex: Um dragão voando sobre uma cidade futurista")
    if st.button("🖼️ Gerar Imagem"):
        if not prompt:
            st.warning("Por favor, descreva a imagem.")
        else:
            with st.spinner("Gerando imagem..."):
                resultado_imagem = gerar_imagem(prompt)
                if resultado_imagem.startswith("Ocorreu um erro"):
                    st.error(resultado_imagem)
                else:
                    st.image(resultado_imagem, caption="Imagem Gerada pela IA")
