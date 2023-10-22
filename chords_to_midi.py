from midiutil import MIDIFile

# Define the mapping of note names to MIDI note numbers
NOTE_MAPPING = {
    'G9':127,
    'F\#9\/Gb9':126,
    'F9':125,
    'E9':124,
    'D#9/Eb9':123,
    'D9':122,
    'C#9/Db9':121,
    'C9':120,
    'B8':119,
    'A#8/Bb8':118,
    'A8':117,
    'G#8/Ab8':116,
    'G8':115,
    'F#8/Gb8':114,
    'F8':113,
    'E8':112,
    'D#8/Eb8':111,
    'D8':110,
    'C#8/Db8':109,
    'C8':108,
    'B7':107,
    'A#7/Bb7':106,
    'A7':105,
    'G#7/Ab7':104,
    'G7':103,
    'F#7/Gb7':102,
    'F7':101,
    'E7':100,
    'D#7/Eb7':99,
    'D7':98,
    'C#7/Db7':97,
    'C7':96,
    'B6':95,
    'A#6/Bb6':94,
    'A6':93,
    'G#6/Ab6':92,
    'G6':91,
    'F#6/Gb6':90,
    'F6':89,
    'E6':88,
    'D#6/Eb6':87,
    'D6':86,
    'C#6/Db6':85,
    'C6':84,
    'B5':83,
    'A#5/Bb5':82,
    'A5':81,
    'G#5/Ab5':80,
    'G5':79,
    'F#5/Gb5':78,
    'F5':77,
    'E5':76,
    'D#5/Eb5':75,
    'D5':74,
    'C#5/Db5':73,
    'C5':72,
    'B4':71,
    'A#4/Bb4':70,
    'A4 ':69,
    'G#4/Ab4':68,
    'G4':67,
    'F#4/Gb4':66,
    'F4':65,
    'E4':64,
    'D#4/Eb4':63,
    'D4':62,
    'C#4/Db4':61,
    'C4':60,
    'B3':59,
    'A#3/Bb3':58,
    'A3':55,
    'G#3/Ab3':56,
    'G3':55,
    'F#3/Gb3':54,
    'F3':53,
    'E3':52,
    'D#3/Eb3':51,
    'D3':50,
    'C#3/Db3':49,
    'C3':48,
    'B2':47,
    'A#2/Bb2':46,
    'A2':45,
    'G#2/Ab2':44,
    'G2':43,
    'F#2/Gb2':42,
    'F2':41,
    'E2':40,
    'D#2/Eb2':39,
    'D2':38,
    'C#2/Db2':37,
    'C2':36,
    'B1':35,
    'A#1/Bb1':34,
    'A1':33,
    'G#1/Ab1':32,
    'G1':31,
    'F#1/Gb1':30,
    'F1':29,
    'E1':28,
    'D#1/Eb1':27,
    'D1':26,
    'C#1/Db1':25,
    'C1':24,
    'B0':23,
    'A#0/Bb0':22,
    'A0':21,
    'G#':20,
    'G':19,
    'F#':18,
    'F':17,
    'E':16,
    'D#':15,
    'D':14,
    'C#':13,
    'C0':12,
    'B':11,
    'A#':10,
    'A':9,
    'G#':8,
    'G':7,
    'F#':6,
    'F':5,
    'E':4,
    'D#':3,
    'D':2,
    'C#':1,
    'C-1':0,
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
