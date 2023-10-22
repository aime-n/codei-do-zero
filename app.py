import streamlit as st
import cohere
# from source.midi_to_mp3 import midi_to_mp3
from source.model import generate_response, get_response_from_promissor_prompt, filter_table
from source.chords_to_midi import text_to_midi
from source.midi_to_mp3 import midi_to_mp3

#Front End starts here
st.title("Codei do Zero 🎵")

form = st.form(key="user_settings")
with form:
    # User input - Song mid to txt
    song_input = st.text_input("Song", key="song_input")

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
        if song_input == "":
            st.error("Music field cannot be blank")
        else:
            my_bar = st.progress(0.05)
            st.subheader("Listen ")

            generate_response(song_input)

# New End button
promissor_button = st.button("Promp para gerar música pronto")

if promissor_button:
    st.balloons()

    response = get_response_from_promissor_prompt()
    table = filter_table(response)
    print('table')
    print(table)

    text_to_midi(table)
    midi_to_mp3()
    # Se você tiver o mp3 como bytes
    mp3_bytes = b'output'

    # Adiciona um player de áudio ao app com os bytes mp3
    st.audio(mp3_bytes, format='audio/mp3')
    

