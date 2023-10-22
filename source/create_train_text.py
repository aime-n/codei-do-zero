import os
import glob
import pandas as pd
from source.lastfm_api import fetch_track_info

banda = 'the beatles'

# Caminho para o diretório de origem
folder_path = 'chords_txt/the beatles/*.txt'

# Caminho para o diretório de destino
dest_folder_path = 'dados_treino'

def criar_arquivos_combinados():
    # Certifique-se de que o diretório de destino exista
    if not os.path.exists(dest_folder_path):
        os.makedirs(dest_folder_path)

    # Lista para armazenar os caminhos dos arquivos
    file_paths = glob.glob(folder_path)

    # Iterar sobre os arquivos dois a dois
    for i in range(0, len(file_paths), 2):
        # Definir o nome do arquivo de destino
        dest_filename = f"combined_thebeatles_{i//2}.txt"
        dest_filepath = os.path.join(dest_folder_path, dest_filename)
        
        # Abrir os arquivos e ler o conteúdo
        with open(dest_filepath, 'w') as dest_file:
            for j, label in zip(range(i, min(i+2, len(file_paths))), ["original", "relative"]):
                with open(file_paths[j], 'r') as file:
                    filename = os.path.basename(file_paths[j])
                    music_name = filename.split(' - ')[1].split('.')[0].lower()

                    tags, wiki = fetch_track_info(artist_name=banda, track_name=music_name)
                    
                    content = file.read()
                    dest_file.write(f"{label} music: {filename}\n")
                    dest_file.write(f"{label} tags: {tags}\n")
                    dest_file.write(f"{label} wiki: {wiki}\n")



                    dest_file.write(content)
                    if j < min(i+2, len(file_paths)) - 1:
                        dest_file.write("\n")
            
            # Escrever os hífens no final
            dest_file.write("--------")
                        
            print(f"Arquivo {dest_filename} criado com sucesso.")


def concatena_TODOS_txts(diretorio, nome_novo_arquivo='output_dataset.txt'):
    # Lista para armazenar o conteúdo dos arquivos
    # conteudo_concatenado = []
    
    # Escrever o conteúdo concatenado em um novo arquivo
    with open(os.path.join(diretorio, nome_novo_arquivo), 'w') as novo_arquivo:
        # Iterar sobre os arquivos no diretório
        for nome_arquivo in os.listdir(diretorio):
            if nome_arquivo.endswith('.txt'):
                with open(os.path.join(diretorio, nome_arquivo), 'r') as arquivo:
                    # Adicionando o conteúdo do arquivo à lista
                    conteudo = arquivo.read()
                    conteudo += '\n---------\n'
                    # conteudo_concatenado.append(conteudo)
                    novo_arquivo.write(''.join(conteudo))
    
        
    print('ESCREVEU')

def pegar_infos_do_dataset(artist, music,
        df_path='data/tcc_ceds_music.csv',
        ):
    # catar a musica no df
    df = pd.read_csv(df_path)
    music = music.lower()
    df_music = df[(df['artist_name'] == artist) & (df['track_name'] == music)]

    if len(df_music) == 1:
        print('ACHOU')
        topic = df.topic[0]
        energy = df.energy[0]
        return topic, energy
    elif len(df_music) == 0:
        return 'feelings', '0.80'
    else:
        print(artist, music)
        print('ACHOU MAIS DE UMA MUSICA')
        return 'feelings', '0.80'
    




# Usando a função
# concatena_txts('dados_treino/validacao', 'arquivo_de_validacao_final.txt')

if __name__ == "__main__":
    concatena_TODOS_txts(diretorio='chords_txt')
