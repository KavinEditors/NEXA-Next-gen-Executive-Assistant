# 🤖 NEXA — Next-gen Executive Assistant

NEXA (**Next-gen Executive Assistant**) is an advanced voice-based AI assistant designed to simplify your workflow.  
It combines **Groq LLM intelligence**, **speech recognition**, **voice responses**, and **system automation** —  
all wrapped in a minimal floating interface with a glowing status indicator.

---

## 🧠 Features Overview

| Category | Feature | Description |
|-----------|----------|-------------|
| 🗣️ Voice Control | Wake Word “Hey Nexa” | Instantly activates the assistant via voice. |
| 💬 AI Chat | Groq API Integration | Answers any question using the LLaMA-3 model. |
| 🌐 Web Automation | Smart Chrome Search | Recognizes “search” commands and opens Chrome automatically. |
| 🔊 Audio Feedback | Startup & Response Sounds | Plays customizable `startup.mp3` and `sound.mp3` cues. |
| 💫 Visual Indicator | Floating `dot.gif` | Non-draggable glowing animation in the bottom-right corner above the taskbar. |
| 🧩 Modular Design | Clean Code Architecture | Organized modules for scalability and easy updates. |
| 🪶 Lightweight | Minimal Dependencies | Runs efficiently on most Windows systems. |

---

## 🏗️ Project Structure

NEXA/
├── main.py
├── .env
├── requirements.txt
│
├── assets/
│   ├── dot.gif
│   ├── startup.mp3
│   └── sound.mp3
│
├── modules/
│   ├── voice.py
│   ├── groq_api.py
│   ├── actions.py
│   └── hotword.py
│
└── utils/
    └── __init__.py

---

## ⚙️ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/KavinEditors/NEXA-Next-gen-Executive-Assistant.git
cd NEXA-Next-gen-Executive-Assistant
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
# source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Set Up Environment Variables
Create a file named `.env` in the project root and add your Groq API key:
```env
GROQ_API_KEY=your_groq_api_key_here
```
🔑 Get your free Groq API key from: [https://console.groq.com](https://console.groq.com)

> ⚠️ **Important:** Never upload your `.env` file to GitHub — keep it private.

---

### 5. Add Assets
Ensure the following files exist under the `assets/` folder:

- `dot.gif` → Floating assistant indicator (transparent background)
- `startup.mp3` → Plays at startup
- `sound.mp3` → Plays before responses

---

## ▶️ Running NEXA

```bash
python main.py
```

Once launched:

- Plays **startup sound**
- Displays the floating **dot.gif** indicator (bottom-right corner above taskbar)
- Greets: “Hello, I’m Nexa. How can I help you today?”
- Waits for the hotword **“Hey Nexa”**

---

## 🗣️ Example Commands

| Command | Action |
|----------|--------|
| “Hey Nexa, search weather in Chennai” | Opens Chrome with search results |
| “Hey Nexa, what’s 5 multiplied by 8?” | Answers using Groq LLM |
| “Hey Nexa, open YouTube” | Opens YouTube instantly |
| “Hey Nexa, tell me a fun fact” | Responds with a random fun fact |

---

## 💡 Future Enhancements

- Continuous background listening with noise filtering  
- Multi-language recognition and voice selection  
- GUI control dashboard for preferences and API setup  
- Auto-start on Windows login (background service)  
- Smart home / IoT integrations  

---

## 👨‍💻 Author

**Kavin**  
Student · Programmer · Developer  
GitHub: [https://github.com/KavinEditors](https://github.com/KavinEditors)

---

## 🧾 License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute with proper attribution.

---

> ⚡ **NEXA — Intelligence meets Execution.**
