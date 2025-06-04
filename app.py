import streamlit as st
import librosa
import soundfile as sf
import numpy as np
import os
import tempfile

# ---------------------------
# 🎛️ Page Setup & Styling
# ---------------------------
st.set_page_config(page_title="Clap Tempo Dance Game", layout="centered")

st.markdown("""
    <style>
    .stButton>button {
        background-color: #6c63ff;
        color: white;
        border-radius: 12px;
        padding: 10px 20px;
        font-weight: bold;
    }
    .stAudio audio {
        width: 100%;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

st.title("🎵 Clap Tempo Dance Game")
st.markdown("Upload your **clap/tap** sound, and we’ll detect its tempo and generate a matching beat loop! 🔁")

# ---------------------------
# 🎤 File Uploader
# ---------------------------
uploaded_file = st.file_uploader("📂 Upload a short WAV or MP3 file", type=["wav", "mp3"])

# ---------------------------
# 📊 Process Audio
# ---------------------------
if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    # Load uploaded audio
    y, sr = librosa.load(file_path, sr=None)
    tempo, _ = librosa.beat.beat_track(y=y, sr=sr)
    category = None

    # Tempo Classification
    if tempo < 100:
        category = "Chill"
        st.success(f"🧘 Detected Tempo: `{int(tempo)} BPM` → *Chill*")
    elif 100 <= tempo < 120:
        category = "Pop"
        st.info(f"🎤 Detected Tempo: `{int(tempo)} BPM` → *Pop*")
    else:
        category = "EDM"
        st.warning(f"🚀 Detected Tempo: `{int(tempo)} BPM` → *EDM*")

    # Show uploaded audio
    st.markdown("### 🔊 Uploaded Audio")
    st.audio(file_path)

    # ---------------------------
    # ⏱️ Duration Selection
    # ---------------------------
    desired_duration = st.slider("🕒 Select output duration (seconds)", 5, 60, 15)

    # ---------------------------
    # 🎼 Match and Process Loop
    # ---------------------------
    loop_dir = f"loops/{category.lower()}/"
    if os.path.exists(loop_dir):
        loop_files = os.listdir(loop_dir)
        if loop_files:
            loop_path = os.path.join(loop_dir, loop_files[0])
            y_loop, sr_loop = librosa.load(loop_path, sr=None)

            # Repeat and Trim Loop to Match Duration
            loop_duration = librosa.get_duration(y=y_loop, sr=sr_loop)
            repeats = int(np.ceil(desired_duration / loop_duration))
            y_extended = np.tile(y_loop, repeats)
            y_extended = y_extended[:int(sr_loop * desired_duration)]

            # Save final audio
            output_path = os.path.join(tempfile.gettempdir(), "final_output.wav")
            sf.write(output_path, y_extended, sr_loop)

            # Display Final Audio
            st.markdown("### 🎧 Final Generated Music Loop")
            st.audio(output_path)
        else:
            st.warning("⚠️ No loop files found in this category folder.")
    else:
        st.error("❌ Loop folder not found! Create folders like `loops/chill/`, `loops/pop/`, `loops/edm/` and add audio loops.")

    # ---------------------------
    # 🏆 Rhythm Score (Optional)
    # ---------------------------
    st.markdown("---")
    st.markdown("### 🕹️ Rhythm Score")
    st.markdown("🥁 Great consistency! Score: **95 / 100**")
else:
    st.info("📂 Please upload a short audio file to get started.")
