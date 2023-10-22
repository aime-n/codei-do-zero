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
    'N': None, # No note (rest)
    'C/3': 48, 'C#/3': 49, 'D/3': 50, 'D#/3': 51, 'E/3': 52, 'F/3': 53, 'F#/3': 54, 'G/3': 55, 'G#/3': 56, 'A/3': 57, 'A#/3': 58, 'B/3': 59,
    'C/4': 60, 'C#/4': 61, 'D/4': 62, 'D#/4': 63, 'E/4': 64, 'F/4': 65, 'F#/4': 66, 'G/4': 67, 'G#/4': 68, 'A/4': 69, 'A#/4': 70, 'B/4': 71,
    'C/5': 72, 'C#/5': 73, 'D/5': 74, 'D#/5': 75, 'E/5': 76, 'F/5': 77, 'F#/5': 78, 'G/5': 79, 'G#/5': 80, 'A/5': 81, 'A#/5': 82, 'B/5': 83,
    
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
