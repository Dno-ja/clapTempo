# 🎵 Clap Tempo Dance Game

A fun and interactive rhythm game that lets you upload a **clap or tap audio**, detects the **tempo**, and plays a **matching music loop** (Chill, Pop, or EDM). No music background needed — just clap to create beats!

> Built with Python, [Streamlit](https://streamlit.io/), and [Librosa](https://librosa.org/)

---

## 🚀 Features

- 🎧 Upload an audio file of your clapping or tapping
- 🧠 Detect tempo using onset and beat analysis with Librosa
- 🎶 Classify tempo into:
  - **Chill** (80–100 BPM)
  - **Pop** (100–120 BPM)
  - **EDM** (120–140 BPM)
- 🔁 Automatically play a matching music loop
- ⏱ Customize output duration (5 to 60 seconds)
- 📊 Visual feedback of tempo detection
- 🔥 Designed for fun, learning, and social creativity

---

## 🛠 Tech Stack

- **Python 3**
- **Streamlit** – for building the web interface
- **Librosa** – for audio processing and tempo estimation
- **Soundfile** – for reading/writing `.wav` files
- **NumPy** – for numerical operations

---

## 📁 Folder Structure


## ⚙️ How to Run the App

- Clone the repository
```bash
git clone https://github.com/yourusername/clap-tempo-dance-game.git
cd clap-tempo-dance-game
```

- Install dependencies
`pip install -r requirements.txt`

- Start the app
  `streamlit run app.py`



```bash
clap-tempo-dance-game/
│
├── app.py                   # Main Streamlit app
├── requirements.txt         # List of dependencies
├── README.md                # Project documentation
├── loops/                   # Pre-recorded music loops
│   ├── chill/
│   ├── pop/
│   └── edm/
```


## 📸 Preview

# 💡 Use Cases
- 🎓 Music education & rhythm training
- 🧒 Kids & beginner-friendly music interaction
- 🕺 Party or event activity
- 📱 Social media content creation

## 🌱 Future Enhancements

- 🎙 **Real-time Mic Input (Live Mode)**  
  Detect tempo from live clapping/tapping using the device microphone.

- 🕹 **Challenge Mode with Scoring**  
  Introduce a rhythm matching game mode with accuracy scoring and timed challenges.

- 💾 **Save and Remix Your Beat**  
  Allow users to download or remix their generated beat with tempo and loop customizations.

- 📱 **Mobile Version with Vibration Feedback**  
  Build a mobile app with mic input and haptic feedback for rhythmic response.

- 🧠 **AI-Generated Melodies from Claps**  
  Generate AI-based melodies or loops based on the detected tempo and rhythm.

- 🎛 **Remix Mode**  
  Let users tweak instrument layers, change tempo, or add sound effects to their loop.

- 🎵 **Genre Customization & Sound Packs**  
  Offer various genres like Hip-Hop, Jazz, Classical, or Rock, with downloadable sound packs.



##  📃 License
 This project is licensed under the MIT License.

# 🙌 Acknowledgments
- Librosa
- Streamlit
- Your beats and creativity 🎶





