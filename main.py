from source.webscrapping_chords import webscrapping_do_zero
from source.create_train_text import concatena_TODOS_txts


if __name__ == "__main__":
    webscrapping_do_zero(banda='queen', folder='chords_txt')
    webscrapping_do_zero(banda='the beatles', folder='chords_txt')
    concatena_TODOS_txts(diretorio='chords_txt')

