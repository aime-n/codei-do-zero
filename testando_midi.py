import mido
from mido import MidiFile

def midi_to_text(midi_file_path):
    midi = MidiFile(midi_file_path)
    
    for track in midi.tracks:
        print(f"Track {track.name}")
        for msg in track:
            print(msg)

# Provide the path to your MIDI file
midi_to_text("midi_data\Ludovico Einaudi - Nuvole Bianche.mid")
