import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from source.lastfm_api import fetch_track_info




def tratar_beatles(nome):
    nome = nome.replace('_', ' ')
    nome = nome.split('-')[1]
    return nome.strip()

def tratar_queen(music):
    partes = music.split()
    music = " ".join(partes[1:])
    return music.strip()

def webscrapping_do_zero(banda, folder='chords_txt'):
    '''
    faz webscrapping dos chords e pega metadata do lastfm api
    '''

    if banda == 'queen':
    # URL da página específica da banda Queen
        url = "http://www.isophonics.net/files/annotations/Queen.html"
    elif banda == 'the beatles':
        url = 'http://www.isophonics.net/files/annotations/The%20Beatles.html'

    # Cria um diretório para salvar os arquivos, se ele ainda não existir
    os.makedirs('data', exist_ok=True)

    # Realiza uma requisição para obter o conteúdo da página
    response = requests.get(url)
    # Se a requisição foi bem-sucedida
    if response.status_code == 200:
        # Analisa o conteúdo da página com BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Itera pelos links na página
        for index, link in enumerate(soup.find_all('a')):
            href = link.get('href')
            
            # Se o link contém 'keylab' e termina com '.lab'
            if href and 'chordlab' in href and href.endswith('.lab'):
                file_url = urljoin(url, href)  # Constrói o URL completo do arquivo
                music = file_url.split('/')[-1].split('.')[0]
                # Baixa o conteúdo do link
                file_response = requests.get(file_url)
                
                if file_response.status_code == 200:
                    # Salva o conteúdo baixado em um arquivo dentro do diretório 'data'
                    if banda == 'queen':
                        track = tratar_queen(music)
                    elif banda == 'the beatles':
                        print(music)
                        track = tratar_beatles(music)
                    with open(f'{folder}/{banda} - {track}.txt', 'w') as file:
                        # file.write(f'track name: {banda} - {track}\n')
                        # tags, wiki = fetch_track_info(artist_name=banda, track_name=track)
                        # file.write(f'tags: {tags}\n')
                        # file.write(f'wiki: {wiki}\n')
                        file.write(file_response.text)
                else:
                    print(f"Failed to download the file. URL: {file_url}, Status code: {file_response.status_code}")
    else:
        print(f"Failed to retrieve the content. Status code: {response.status_code}, Reason: {response.reason}")


if __name__ == '__main__':
    webscrapping_do_zero(banda='the beatles')
    webscrapping_do_zero(banda='queen')