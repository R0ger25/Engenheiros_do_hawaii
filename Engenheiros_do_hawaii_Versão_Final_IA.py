# WEB SCRAPPING ENGENHEIROS DO HAWAII

# 1. IMPORTS NECESSÁRIOS
import requests
from bs4 import BeautifulSoup
import time  # Para pausas entre requisições
import csv   # Para criar os arquivos .csv
import os    # Para criar a pasta de arquivos
import re    # Para limpar nomes de arquivos

# 2. CONFIGURAÇÕES INICIAIS
url = 'https://www.letras.mus.br/engenheiros-do-hawaii/discografia/'
url_base = 'https://www.letras.mus.br'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}

# 3. COLETA INICIAL DOS ÁLBUNS (USANDO SEU MÉTODO ORIGINAL)
print("Buscando lista de álbuns...")
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

albuns_data = []
# Usando seu seletor para os álbuns
albuns = soup.find_all('h1', class_='songList-header-name')
for album in albuns:
    album_content = album.find('a')
    if album_content:
        album_link = album_content['href']
        album_name = album_content.text
        albuns_data.append({'name': album_name, 'link': album_link})

print(f"Encontrados {len(albuns_data)} álbuns.")
print("-" * 30)

# 4. ESTRUTURA DE DADOS PRINCIPAL
dados_completos = []

# 5. LOOP PRINCIPAL PARA PROCESSAR CADA ÁLBUM E SUAS MÚSICAS
for i, album in enumerate(albuns_data):
    album_url = url_base + album['link']
    album_nome = album['name']
    
    print(f"Processando álbum {i+1}/{len(albuns_data)}: {album_nome}")

    album_atual_info = {
        'nome_album': album_nome,
        'musicas': []
    }

    try:
        site_album = requests.get(album_url, headers=headers)
        soup_album = BeautifulSoup(site_album.content, 'html.parser')
        
        # Usando seu seletor para os containers de música
        containers_musicas = soup_album.find_all('li', class_='songList-table-row --song isVisible')
        print(f"-> Encontradas {len(containers_musicas)} músicas.")

        for j, container in enumerate(containers_musicas):
            # Usando seus seletores para nome e link da música
            el_nome = container.find('div', class_='songList-table-songName font --base --size16')
            el_link = container.find('a', class_='songList-table-playButton')
            
            if el_nome and el_link:
                musica_nome = el_nome.text.strip()
                musica_url = url_base + el_link['href']
                
                print(f"  ({j+1}/{len(containers_musicas)}) Buscando letra de: {musica_nome}")

                site_musica = requests.get(musica_url, headers=headers)
                soup_musica = BeautifulSoup(site_musica.content, 'html.parser')
                
                # Usando seu seletor para a div da letra
                div_letra = soup_musica.find('div', class_='lyric-original')
                letra_final = "Letra não encontrada."
                
                if div_letra:
                    letra_final = div_letra.find_all('p')
                
                album_atual_info['musicas'].append({
                    'titulo': musica_nome,
                    'letra': letra_final
                })
                
                time.sleep(1)

    except requests.exceptions.RequestException as e:
        print(f"!!! Erro ao processar o álbum {album_nome}: {e}")

    dados_completos.append(album_atual_info)
    print("-" * 30)

print("✅ Coleta de dados finalizada!")

# 6. GERANDO OS ARQUIVOS .CSV
pasta_csv = 'letras_engenheiros_hawaii'
if not os.path.exists(pasta_csv):
    os.makedirs(pasta_csv)

print(f"\nIniciando a criação dos arquivos CSV na pasta '{pasta_csv}'...")

for album in dados_completos:
    nome_album = album['nome_album']
    
    nome_arquivo_seguro = re.sub(r'[\\/*?:"<>|]', "", nome_album).replace(' ', '_')
    caminho_arquivo = os.path.join(pasta_csv, f"{nome_arquivo_seguro}.csv")
    
    print(f"-> Criando arquivo: {caminho_arquivo}")
    
    with open(caminho_arquivo, 'w', newline='', encoding='utf-8') as arquivo_csv:
        cabecalho = ['Musica', 'Letra']
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(cabecalho)
        
        for musica in album['musicas']:
            escritor_csv.writerow([musica['titulo'], musica['letra']])

print("\n🚀 Processo finalizado! Todos os arquivos CSV foram criados.")