import numpy as np

def classify_tempo(tempo):
    if 80 <= tempo < 100:
        return "Chill"
    elif 100 <= tempo < 120:
        return "Pop"
    elif 120 <= tempo <= 140:
        return "EDM"
    return "Unmatched"

def score_consistency(onsets):
    if len(onsets) < 2:
        return 0
    intervals = np.diff(onsets)
    variance = np.var(intervals)
    score = max(0, 100 - int(variance * 1000))
    return min(score, 100)
