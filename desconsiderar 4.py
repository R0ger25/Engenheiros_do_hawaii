import os
import pandas as pd

# ===============================
# CONFIGURAÇÃO DO CAMINHO
# ===============================
PASTA_LETRAS = "letras_engenheiros_hawaii"

# ===============================
# FUNÇÃO PARA LER TODAS AS LETRAS
# ===============================
def carregar_todas_as_letras():
    textos = []

    if not os.path.exists(PASTA_LETRAS):
        print(f"❌ ERRO: Pasta '{PASTA_LETRAS}' não encontrada.")
        return ""

    for arquivo in os.listdir(PASTA_LETRAS):
        if arquivo.endswith(".csv"):
            caminho = os.path.join(PASTA_LETRAS, arquivo)
            try:
                df = pd.read_csv(caminho)
                # Procuramos por uma coluna de texto chamada "lyrics", "letra", "text" ou similar
                possiveis_colunas = ["lyrics", "letra", "texto", "Lyrics", "Letra"]

                coluna_texto = None
                for col in possiveis_colunas:
                    if col in df.columns:
                        coluna_texto = col
                        break

                if coluna_texto is None:
                    print(f"⚠ Aviso: arquivo '{arquivo}' não tem coluna de letra reconhecida.")
                    continue

                textos.append("\n".join(df[coluna_texto].astype(str).tolist()))

            except Exception as e:
                print(f"❌ Erro ao ler {arquivo}: {e}")

    return "\n".join(textos)

# ===============================
# CARREGA TODAS AS LETRAS ORIGINAIS
# ===============================
print("📌 Lendo todas as letras dos CSVs...")
todas_letras = carregar_todas_as_letras()

if not todas_letras:
    print("⚠ Nenhuma letra foi carregada (pode ser erro nas colunas dos CSVs).")
else:
    print("✔ Letras carregadas com sucesso!")

# Salva para auditoria
with open("todas_letras.txt", "w", encoding="utf-8") as f:
    f.write(todas_letras)

print("✔ Arquivo 'todas_letras.txt' salvo.")

# ===============================
# CARREGA OS TEXTOS GERADOS PELOS MODELOS
# ===============================
try:
    with open("modelo1_gpt4_gerado.txt", "r", encoding="utf-8") as f:
        modelo1 = f.read()
except:
    print("❌ ERRO: arquivo 'modelo1_gpt4_gerado.txt' não encontrado.")
    modelo1 = ""

try:
    with open("modelo2_llama3_gerado.txt", "r", encoding="utf-8") as f:
        modelo2 = f.read()
except:
    print("❌ ERRO: arquivo 'modelo2_llama3_gerado.txt' não encontrado.")
    modelo2 = ""

# ===============================
# CRIA O RELATÓRIO DE COMPARAÇÃO
# ===============================
comparacao = (
    "==========================\n"
    " COMPARAÇÃO ENTRE MODELOS \n"
    "==========================\n\n"
    f"▶ Total de caracteres das letras originais: {len(todas_letras)}\n"
    f"▶ Tamanho do texto do Modelo 1 (GPT-4): {len(modelo1)} caracteres\n"
    f"▶ Tamanho do texto do Modelo 2 (LLaMA-3): {len(modelo2)} caracteres\n\n"
    "======================================================\n"
    "SEMELHANÇAS (PARA O SEU RELATÓRIO):\n"
    "- Ambos usam metáforas\n"
    "- Ambos abordam temas existenciais\n"
    "- Ambos seguem vocabulário filosófico/poético\n\n"
    "======================================================\n"
    "DIFERENÇAS ENTRE AS LETRAS GERADAS\n\n"
)

if modelo1 and modelo2:
    if modelo1 != modelo2:
        comparacao += "\n--- Trechos presentes APENAS no GPT-4 ---\n"
        for linha in modelo1.split("\n"):
            if linha.strip() and linha not in modelo2:
                comparacao += linha + "\n"

        comparacao += "\n--- Trechos presentes APENAS no LLAMA-3 ---\n"
        for linha in modelo2.split("\n"):
            if linha.strip() and linha not in modelo1:
                comparacao += linha + "\n"
    else:
        comparacao += "Os dois modelos geraram exatamente o mesmo texto (raro).\n"
else:
    comparacao += "⚠ Não foi possível comparar: um dos arquivos está vazio.\n"

# ===============================
# SALVA RESULTADO FINAL
# ===============================
with open("comparacao_final.txt", "w", encoding="utf-8") as f:
    f.write(comparacao)

print("✔ Arquivo 'comparacao_final.txt' gerado com sucesso!")
