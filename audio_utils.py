import librosa
import numpy as np

def analyze_tempo(audio, sr):
    onset_env = librosa.onset.onset_strength(y=audio, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)[0]
    onsets = librosa.onset.onset_detect(y=audio, sr=sr, units='time')
    return tempo, onsets
