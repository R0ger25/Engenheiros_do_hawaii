import requests
import json
import os

# -----------------------------
# Configurações de pastas e arquivos
# -----------------------------
output_dir = "resultado_experimento3"
os.makedirs(output_dir, exist_ok=True)

gpt_file = os.path.join(output_dir, "modelo1_gpt4_gerado.txt")  # você coloca manualmente
llama_file = os.path.join(output_dir, "modelo2_llama3_gerado.txt")
comparacao_file = os.path.join(output_dir, "comparacao_final.txt")

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"

# -----------------------------
# Prompt LLaMA-3
# -----------------------------
PROMPT = (
    "Aja como um letrista de rock brasileiro dos anos 80/90, similar a Humberto Gessinger.\n"
    "Suas letras são filosóficas, irônicas, céticas e usam muitas metáforas sobre tecnologia, a passagem do tempo, solidão urbana e crítica social.\n"
    "Use um vocabulário rico, jogos de palavras, referências literárias e termos técnicos ou científicos.\n"
    "Tema: 'a ansiedade na era digital'.\n"
    "Escreva entre 14 e 40 linhas. Apenas a letra.\n"
)

# -----------------------------
# Função para gerar LLaMA-3
# -----------------------------
def call_ollama_stream(model, prompt):
    payload = {"model": model, "prompt": prompt}
    headers = {"Content-Type": "application/json"}
    with requests.post(OLLAMA_URL, json=payload, headers=headers, stream=True, timeout=200) as r:
        r.raise_for_status()
        for line in r.iter_lines():
            if not line:
                continue
            data = json.loads(line.decode("utf-8"))
            if "response" in data:
                yield data["response"]

# -----------------------------
# Gerando texto LLaMA-3
# -----------------------------
output_text = ""
print("Gerando texto do LLaMA-3:\n")
for chunk in call_ollama_stream(MODEL_NAME, PROMPT):
    print(chunk, end="")
    output_text += chunk

with open(llama_file, "w", encoding="utf-8") as f:
    f.write(output_text)

print(f"\n\nLetra LLaMA-3 salva em: {llama_file}")

# -----------------------------
# Lendo GPT-4 e LLaMA-3
# -----------------------------
with open(gpt_file, "r", encoding="utf-8") as f:
    gpt_text = f.read()

with open(llama_file, "r", encoding="utf-8") as f:
    llama_text = f.read()

# -----------------------------
# Comparação
# -----------------------------
total_original = 672897  # fornecido no enunciado
len_gpt = len(gpt_text)
len_llama = len(llama_text)

gpt_lines = set(gpt_text.splitlines())
llama_lines = set(llama_text.splitlines())

gpt_only = gpt_lines - llama_lines
llama_only = llama_lines - gpt_lines

# -----------------------------
# Salvando comparação
# -----------------------------
with open(comparacao_file, "w", encoding="utf-8") as f:
    f.write("==========================\n")
    f.write(" COMPARAÇÃO ENTRE MODELOS \n")
    f.write("==========================\n\n")
    f.write(f"▶ Total de caracteres das letras originais: {total_original}\n")
    f.write(f"▶ Tamanho do texto do Modelo 1 (GPT-4): {len_gpt} caracteres\n")
    f.write(f"▶ Tamanho do texto do Modelo 2 (LLaMA-3): {len_llama} caracteres\n\n")
    f.write("======================================================\n")
    f.write("SEMELHANÇAS (PARA O SEU RELATÓRIO):\n")
    f.write("- Ambos usam metáforas\n")
    f.write("- Ambos abordam temas existenciais\n")
    f.write("- Ambos seguem vocabulário filosófico/poético\n\n")
    f.write("======================================================\n")
    f.write("DIFERENÇAS ENTRE AS LETRAS GERADAS\n\n")
    f.write("--- Trechos presentes APENAS no GPT-4 ---\n")
    f.write("\n".join(sorted(gpt_only)))
    f.write("\n\n--- Trechos presentes APENAS no LLaMA-3 ---\n")
    f.write("\n".join(sorted(llama_only)))

print(f"Comparação salva em: {comparacao_file}")

# -----------------------------
# Fim do Script
# -----------------------------
print("\nExperimento 3 concluído com sucesso!")
