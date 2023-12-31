from midi2audio import FluidSynth
from pydub import AudioSegment

def midi_to_mp3(midi_file_path='output.mid', mp3_file_path='output.mp3'):
    # Convert MIDI to WAV
    fs = FluidSynth()
    fs.midi_to_audio(midi_file_path, 'output.wav')
    
    # Convert WAV to MP3
    AudioSegment.from_wav('output.wav').export(mp3_file_path, format="mp3")

if __name__ == "__main__":
    # Usage example
    midi_to_mp3('midi/musica_gerada.mid', 'output.mp3')
