import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()  # Carrega as variáveis do .env

genai.configure(api_key=os.getenv("AIzaSyCHf2inc4P6xld3jBdRlOC2iA6Qyqw0d_U"))

# Criação do modelo Gemini Flash
modelo = genai.GenerativeModel("gemini-2.0-flash")

def gerar_resposta(prompt):
    resposta = modelo.generate_content(prompt)
    return resposta.text
