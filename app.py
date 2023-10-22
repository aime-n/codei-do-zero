import streamlit as st
import cohere
import time
# from source.midi_to_mp3 import midi_to_mp3
from source.model import generate_response, get_response_from_promissor_prompt, filter_table, get_response_from_promissor_prompt_continuacao
from source.model import get_musica_1, get_prompt_padrao
from source.chords_to_midi import text_to_midi
from source.midi_to_mp3 import midi_to_mp3
import pandas as pd
import threading

#Front End starts here
st.title("Codei do Zero 🎵")
function_running = False
def run_progress_bar():
    progress = st.progress(0)  # Inicia a barra de progresso
    increment = 0.01  # Valor que a barra de progresso será incrementada
    
    # Enquanto a função estiver rodando, atualiza a barra de progresso
    while function_running:
        if progress.progress + increment <= 1:  # Se a barra de progresso não está completa
            progress.progress += increment  # Incrementa a barra de progresso
        time.sleep(0.1)  # Pausa entre as atualizações

form = st.form(key="user_settings")
with form:
    musica1 = get_musica_1()
    text_to_midi(musica1, output_midi_file="musica1.mid")
    midi_to_mp3(midi_file_path='musica1.mid', mp3_file_path='musica1.mp3')
    st.audio('musica1.mp3', format='audio/mp3')
    # Botão para preencher o campo de texto
    if st.button('Preencher Prompt de Texto'):
        song_input_default = get_prompt_padrao()  # Texto que você quer preencher automaticamente
    else:
        song_input_default = ""
    # User input - Song mid to txt
    song_input = st.text_input("Song", value=song_input_default, key="song_input")

    # Create a two-column view
    col1, col2 = st.columns(2)
    with col1:  
        # User input - The happiness of the generated song
        happiness_input = st.slider(
            "Happiness of ideas",
            value=3,
            key="num_input",
            min_value=0,
            max_value=1,
            help="Choose how happy you want the generated song to be",
        )
    with col2:
        # User input - The 'temperature' value representing the level of creativity
        creativity_input = st.slider(
            "Creativi   \\\\\\\\\\ty",
            value=0.5,
            key="creativity_input",
            min_value=0.1,
            max_value=0.9,
            help="Lower values generate more “predictable” output, higher values generate more “creative” output",
        )
    # Submit button to start generating a song
    generate_button = form.form_submit_button("Generate Song")

    if generate_button:
        st.balloons()

        if song_input == "":
            st.error("Music field cannot be blank")
        else:
            progress_bar = st.progress(0.05)
            response = generate_response(song_input)
            st.write('Request 200')
            progress_bar.progress(0.25)

            table = filter_table(response)
            st.write('Tabela recebida no formato correto.')
            progress_bar.progress(0.50)
            print('table:')
            print(table)
            table_lines = table.strip().split('\n')
            # Splitting each line into columns and creating a DataFrame
            df = pd.DataFrame([line.split() for line in table_lines], columns=['Start', 'End', 'Chord'])
            st.dataframe(df)
            progress_bar.progress(0.75)

            text_to_midi(table)
            st.write('Convertido para MIDI.')
            midi_to_mp3()
            st.write('Convertido para mp3.')
            # Se você tiver o mp3 como bytes
            mp3_bytes = 'output.mp3'
            progress_bar.progress(1.0)
            # Adiciona um player de áudio ao app com os bytes mp3
            st.audio(mp3_bytes, format='audio/mp3')



# New End button
promissor_button = st.button("Promp para gerar música pronto")



# if promissor_button:
#     st.balloons()
    
#     progress_bar = st.progress(0)
#     thread1 = threading.Thread(target=run_progress_bar, args=(progress_bar,))
#     thread1.start()
    
#     response = get_response_from_promissor_prompt()
#     st.write('Request 200')
#     # progress_bar.progress(0.25)
#     table = filter_table(response)
#     st.write('Tabela recebida no formato correto.')
#     # progress_bar.progress(0.50)
#     print('table:')
#     print(table)
#     table_lines = table.strip().split('\n')
#     # Splitting each line into columns and creating a DataFrame
#     df = pd.DataFrame([line.split() for line in table_lines], columns=['Start', 'End', 'Chord'])
#     st.dataframe(df)
#     # progress_bar.progress(0.75)

#     text_to_midi(table)
#     st.write('Convertido para MIDI.')
#     midi_to_mp3()
#     st.write('Convertido para mp3.')
#     # Se você tiver o mp3 como bytes
#     mp3_bytes = 'output.mp3'
#     # progress_bar.progress(1.0)
#     # Adiciona um player de áudio ao app com os bytes mp3
#     st.audio(mp3_bytes, format='audio/mp3')
    
    # continuacao_button = st.button("Promp para continuar música gerada")
    # if continuacao_button:
    #     st.balloons()

    #     response = get_response_from_promissor_prompt_continuacao(table)
    #     table = filter_table(response)
    #     print('table')
    #     print(table)

    #     text_to_midi(table)
    #     midi_to_mp3()
    #     # Se você tiver o mp3 como bytes
    #     mp3_bytes = b'output'

    #     # Adiciona um player de áudio ao app com os bytes mp3
    #     st.audio(mp3_bytes, format='audio/mp3') 