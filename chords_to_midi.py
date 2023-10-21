from midiutil import MIDIFile

# Define the mapping of note names to MIDI note numbers
NOTE_MAPPING = {
    'C': 60,  # C4 in MIDI
    'D': 62,  # D4 in MIDI
    'E': 64,  # E4 in MIDI
    'F': 65,  # F4 in MIDI
    'G': 67,  # G4 in MIDI
    'A': 69,  # A4 in MIDI
    'B': 71,  # B4 in MIDI
    'N': None # No note (rest)
}


# Define a function to convert your text to MIDI
def text_to_midi(text, output_midi_file):
    midi = MIDIFile(1)
    
    track = 0
    channel = 0
    time = 0 
    duration = 1 
    tempo = 120 
    volume = 100 
    
    midi.addTempo(track, time, tempo)
    
    lines = text.strip().split("\n")
    for line in lines:
        start, end, note_info = line.split()
        start, end = float(start), float(end)
        duration = end - start
        
        note_name = note_info.split(":")[0]  # Extract note before the colon
        
        note_number = NOTE_MAPPING.get(note_name)
        if note_number is None and note_name != 'N':
            print(f"Warning: Note '{note_name}' is not mapped, skipping.")
            continue
        
        if note_number is not None:
            midi.addNote(track, channel, note_number, start, duration, volume)
        
    with open(output_midi_file, "wb") as midi_file:
        midi.writeFile(midi_file)
    print(f"MIDI file '{output_midi_file}' has been created.")

with open('midi_data\love_me_do.txt', 'r') as file:
    music_text = file.read()

# Convert the text to a MIDI file
text_to_midi(music_text, "output_lovemedo.mid")
