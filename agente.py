from pathlib import Path
import os

from dotenv import load_dotenv
from openai import OpenAI

dotenv_path = Path(__file__).resolve().parent / ".env"
load_dotenv(dotenv_path=dotenv_path, override=True)

api_key = os.getenv("OPENAI_API_KEY", "").strip()
if not api_key:
    raise RuntimeError("OPENAI_API_KEY não foi encontrada no arquivo .env.")

if not api_key.startswith("sk-"):
    raise RuntimeError("OPENAI_API_KEY inválida. Verifique o valor no arquivo .env.")

qual_produto = "TV de 55 polegadas"
ambiente = "Sala de estar de 6 metros quadrados"
modelo = "u8600f"

prompt = f"""Crie um escritivo de suporte para o produto {qual_produto}, para o uso em {ambiente}
            detalhando o modelo {modelo} e descreva as melhores características."""

cliente = OpenAI(api_key=api_key)
response = cliente.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "Você é um assistente de suporte especializado em produtos eletrônicos."},
        {"role": "user", "content": prompt},
    ],
)

print(response.choices[0].message.content)