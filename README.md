# NEXA — Next-gen Executive Assistant

NEXA (**Next-gen Executive Assistant**) is an advanced voice-based AI assistant designed to simplify workflow and perform real-time automation intelligently.  
It combines **Groq LLM intelligence**, **speech recognition**, **voice responses**, and **Windows system automation** — powered by a floating UI indicator.

---

## ✨ Features

| Category | Feature | Description |
|----------|---------|-------------|
| 🗣️ Voice Control | Wake Word “Hey Nexa” | Activates the assistant using voice only |
| 💬 AI Chat | Groq API (LLaMA-3) | Raw clean responses without markdown or emojis |
| 🌐 Web Automation | Search & Open websites | Opens YouTube, GitHub, Discord, WhatsApp Web, etc. |
| 📦 App Launcher | Desktop software execution | Opens VS Code, Notepad, Explorer, VLC, Chrome, etc. |
| 📢 System Control | Volume, Brightness, Shutdown | Shutdown, Restart, Sleep, Lock, Volume, Brightness |
| 🔤 Raw Text Speech | TTS clean output | Reads text without emojis or formatting |
| 🔊 Audio Feedback | Custom sounds | `startup.mp3` when starting and `sound.mp3` before response |
| 💫 UI Indicator | Floating `dot.gif` | Forever-loop breathing glowing animation |

---

## 📂 Project Structure

```plaintext
NEXA-Next-gen-Executive-Assistant/
│── main.py
│── groq_api.py
│── hotword.py
│── speak.py
│── actions.py
│── requirements.txt
│── groq_apimodels_check.py
│
├── assets/
│   ├── dot.gif
│   ├── startup.mp3
│   └── sound.mp3
```

---

## ⚙️ Installation

1️⃣ Clone the Repo  
```bash
git clone https://github.com/KavinEditors/NEXA-Next-gen-Executive-Assistant.git
cd NEXA-Next-gen-Executive-Assistant
```

2️⃣ Install Requirements  
```bash
pip install -r requirements.txt
```

3️⃣ Add API Key  

Create `.env` in the root folder:

```env
GROQ_API_KEY=your_groq_api_key
```

💡 Get your API key from: https://console.groq.com/

4️⃣ Add NirCmd to System PATH (Required for volume & brightness)

📌 Download NirCmd: https://www.nirsoft.net/utils/nircmd.zip  

📌 How to add NirCmd to PATH (Video Tutorial):  
https://youtu.be/tYdQ8G2nRVs?si=Ofvdo6gF6CSJnfIn  

Place `nircmd.exe` inside `C:\Windows\System32` or add its folder to PATH

---

▶️ Running NEXA  
```bash
python main.py
```

Start Experience:

- Plays boot sound
- Shows glowing floating dot
- Speaks: “Hello, I’m Nexa. How can I help you today?”
- Waits for: "Hey Nexa"

---

## 🗣 Example Commands

| Command | Result |
|---------|--------|
| "Hey Nexa, open YouTube" | Opens YouTube |
| "Hey Nexa, search weather Chennai" | Google search |
| "Increase volume" | Adjusts system volume |
| "Turn off Wi-Fi" | Toggles Wi-Fi |
| "Restart / Shutdown / Lock / Sleep" | Controls power |

---

📌 Available Groq Models  

Run the included checker file to list supported models:

```bash
python groq_apimodels_check.py
```

---

📦 `requirements.txt`

```
groq
python-dotenv
requests
pyttsx3
SpeechRecognition
pydub
pyaudio
pygame
```

---

📜 License

MIT License — Free to use, modify & distribute.

💖 Contributing

Pull requests are welcome.

⭐ Support the Project

If this helped you, leave a star 🌟 on GitHub to support future development:  
https://github.com/KavinEditors/NEXA-Next-gen-Executive-Assistant
