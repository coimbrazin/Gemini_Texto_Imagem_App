import os
import google.generativeai as genai
from dotenv import load_dotenv
from stability_sdk import client
import stability_sdk.interfaces.gooseai.generation.generation_pb2 as generation

# Carregar as variáveis de ambiente
load_dotenv()

# Configurar a chave da API do Gemini
GEMINI_API_KEY = os.getenv("AIzaSyC67Pc_pFQbEzAVACuoSutNekFJQ7wc7UQ")
genai.configure(api_key="AIzaSyC67Pc_pFQbEzAVACuoSutNekFJQ7wc7UQ")

# Configurações do modelo Gemini
generation_config = {
    "temperature": 0.7,
    "top_p": 1,
    "top_k": 1,
    "max_output_tokens": 2048,
}

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
)

# Função para gerar texto
def gerar_texto(tema: str, formato: str) -> str:
    if not tema.strip():
        return "Digite um tema para gerar o texto."

    if formato == "Texto livre":
        prompt = f"Escreva um texto sobre {tema}."
    else:
        prompt = f"Gerar um texto no formato {formato} sobre o tema {tema}."

    try:
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"Ocorreu um erro ao gerar o texto: {str(e)}"

# Configuração da Stability API para gerar imagens
stability_api = client.StabilityInference(
    key=os.getenv("STABILITY_API_KEY"),  # use sua variável de ambiente
    verbose=True,
    engine="stable-diffusion-xl-1024-v1-0"
)

# Função para gerar imagem
def gerar_imagem(tema: str):
    try:
        # Geração com parâmetros válidos
        answers = stability_api.generate(
            prompt=tema,
            width=512,
            height=512,
            samples=1,
            seed=42,
            cfg_scale=7
        )

        # Salvar a imagem
        for resp in answers:
            for artifact in resp.artifacts:
                if artifact.finish_reason == generation.FILTER:
                    return "Conteúdo bloqueado pela moderação da IA."
                if artifact.type == generation.ARTIFACT_IMAGE:
                    image_path = "imagem_gerada.png"
                    with open(image_path, "wb") as f:
                        f.write(artifact.binary)
                    return image_path

        return "Não foi possível gerar a imagem."
    except Exception as e:
        return f"Ocorreu um erro ao gerar a imagem: {str(e)}"
