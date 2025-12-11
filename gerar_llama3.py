# gerar_llama3.py

import requests
import json
import os
import sys

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# ============================
# PROMPT OFICIAL DO PROFESSOR
# ============================

PROMPT = (
    "Aja como um letrista de rock brasileiro dos anos 80/90, similar a Humberto Gessinger.\n"
    "Suas letras são filosóficas, irônicas, céticas e usam muitas metáforas sobre tecnologia,\n"
    "a passagem do tempo, solidão urbana e crítica social.\n"
    "Use um vocabulário rico, jogos de palavras, referências literárias e\n"
    "termos técnicos ou científicos (ex: paradoxo, algoritmo, radiação, cálculo).\n"
    "\n"
    "Exemplos de estilo (NÃO copie, apenas use como inspiração):\n"
    "\"O papa é pop, o pop não poupa ninguém...\"\n"
    "\"Eu me sinto um estrangeiro, passageiro de algum trem...\"\n"
    "\n"
    "Tarefa: Escreva uma letra ORIGINAL e COMPLETA sobre o tema 'a ansiedade na era digital'.\n"
    "Apenas a letra. Não explique nada.\n"
)

# ============================
# Função de streaming
# ============================

def call_ollama_stream(model, prompt):
    payload = {"model": model, "prompt": prompt}
    headers = {"Content-Type": "application/json"}

    try:
        with requests.post(OLLAMA_URL, json=payload, headers=headers, stream=True, timeout=200) as r:
            r.raise_for_status()
            for line in r.iter_lines():
                if not line:
                    continue
                data = json.loads(line.decode("utf-8"))
                if "response" in data:
                    yield data["response"]
    except Exception as e:
        print("Erro na requisição ao Ollama:", e)
        sys.exit(1)


# ============================
# MAIN
# ============================

def main():
    print(f"Gerando letra com {MODEL_NAME} via Ollama...\n")

    output_text = ""

    for chunk in call_ollama_stream(MODEL_NAME, PROMPT):
        print(chunk, end="")      # streaming na tela
        output_text += chunk      # junta tudo

    out_path = os.path.join(os.path.dirname(__file__), "modelo2_llama3_gerado.txt")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(output_text)

    print("\n\n✔ Letra salva em:", out_path)


if __name__ == "__main__":
    main()
