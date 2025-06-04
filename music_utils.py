import os
import random

def get_loop_path(tempo_category):
    folder = f"loops/{tempo_category}"
    if os.path.exists(folder):
        files = [f for f in os.listdir(folder) if f.endswith(".wav")]
        if files:
            return os.path.join(folder, random.choice(files))
    return None
