# WEB SCRAPPING ENGENHEIROS DO HAWAII

contador = 0

import requests
from bs4 import BeautifulSoup

url = 'https://www.letras.mus.br/engenheiros-do-hawaii/discografia/'
url_base = 'https://www.letras.mus.br'

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36'}

site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

albuns = soup.find_all('h1', class_='songList-header-name')

#ALBUM E LINK
albuns_data = []
# MUSICA E LINK
musicas_data = []
# MUSICAS E LETRA
musicas_letras = []
# ALBUM E CONTAGEM
albuns_e_contagem = []

# PEGA OS ALBUNS
for album in albuns:
    album_content = album.find('a')
    if album_content:
        album_link = album_content['href']
        album_name = album_content.text
        albuns_data.append({'name': album_name, 'link': album_link})

# PRA CADA ALBUM PEGAS TODAS SUAS MUSICAS E LINKS
for i, album in enumerate(albuns_data):
    album_url = url_base + album['link']
    album_nome_atual = album['name']
    
    print(f"Processando álbum {i+1}/{len(albuns_data)}: {album['name']}")
    print()

    site_album = requests.get(album_url, headers=headers)
    soup_album = BeautifulSoup(site_album.content, 'html.parser')
    
    containers_musicas = soup_album.find_all('li', class_='songList-table-row --song isVisible')
    
    numero_de_musicas = len(containers_musicas)
    print(f"-> Encontradas {numero_de_musicas} músicas neste álbum.")
    
    albuns_e_contagem.append({
        'nome_album': album_nome_atual,
        'quantidade_musicas': numero_de_musicas
    })
    
    print()
    
    # ADICIONA TODAS AS MUSICAS E LINKS NA LISTA
    if containers_musicas:
        for container in containers_musicas:
            musica_nome = container.find('div', class_='songList-table-songName font --base --size16')
            musica_link = container.find('a', class_='songList-table-playButton')
            
            if musica_nome and musica_link:
                musica_nome = musica_nome.text
                musica_link = musica_link['href']
                musicas_data.append({'name': musica_nome, 'link': musica_link})

# PEGA TODAS AS MUSICAS E SUAS LETRAS
for i, musica in enumerate(musicas_data):
    musica_url = url_base + musica['link']
    
    print(f"Processando música {i+1}/{len(musicas_data)}: {musica['name']}")
    print()
    
    site_musica = requests.get(musica_url, headers=headers)
    soup_musica = BeautifulSoup(site_musica.content, 'html.parser')
    
    letra_musica = soup_musica.find('div', class_='lyric-original')
    
    if letra_musica:
        letra_final = letra_musica.find_all('p')
        musicas_letras.append({'name': musica['name'], 'letra': letra_final})