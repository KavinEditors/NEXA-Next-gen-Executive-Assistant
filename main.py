import sys
import os
import threading
import webbrowser
import pyttsx3
import speech_recognition as sr
import pyautogui
from dotenv import load_dotenv
from groq import Groq
from PyQt5 import QtWidgets, QtGui, QtCore
import pygame

# ======================================================
# NEXA — Next-gen Executive Assistant
# ======================================================

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
recognizer = sr.Recognizer()

# ======================================================
# UTILITIES
# ======================================================
def speak(text):
    print(f"NEXA: {text}")
    engine.say(text)
    engine.runAndWait()

def listen(timeout=5, phrase_limit=6):
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source, duration=0.3)
        try:
            print("Listening...")
            audio = recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_limit)
            return recognizer.recognize_google(audio, language="en-in").lower()
        except Exception:
            return ""

def play_startup_sound():
    try:
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sound.mp3")
        pygame.mixer.music.play()
    except Exception as e:
        print("Startup sound error:", e)

def ask_groq(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": question}]
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Sorry, I couldn’t reach Groq API. {e}"

# ======================================================
# COMMAND EXECUTION
# ======================================================
def execute_command(query):
    if not query:
        return

    # SEARCH
    if "srch" in query or "search" in query:
        speak("What would you like me to search for?")
        term = listen(timeout=6, phrase_limit=6)
        if term:
            speak(f"Searching {term} on Chrome.")
            chrome_path = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
            webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open(f"https://www.google.com/search?q={term}")
        else:
            speak("I didn’t catch that. Please repeat.")

    # OPEN APPS
    elif "open" in query:
        app_name = query.replace("open", "").strip()
        paths = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "notepad": "notepad.exe",
            "calculator": "calc.exe",
            "explorer": "explorer.exe",
            "cmd": "cmd.exe",
            "vscode": r"C:\Users\%USERNAME%\AppData\Local\Programs\Microsoft VS Code\Code.exe"
        }

        # Common websites
        websites = {
            "youtube": "https://www.youtube.com",
            "gmail": "https://mail.google.com",
            "google": "https://www.google.com",
            "github": "https://github.com",
            "whatsapp": "https://web.whatsapp.com",
            "spotify": "https://open.spotify.com",
            "facebook": "https://www.facebook.com",
            "twitter": "https://twitter.com",
            "x": "https://x.com",
            "instagram": "https://www.instagram.com",
            "reddit": "https://www.reddit.com",
            "chatgpt": "https://chat.openai.com"
        }

        # Match and open
        if app_name in paths:
            speak(f"Opening {app_name}")
            os.startfile(os.path.expandvars(paths[app_name]))
        elif app_name in websites:
            speak(f"Opening {app_name}")
            webbrowser.open(websites[app_name])
        else:
            speak(f"Opening {app_name} on the web.")
            webbrowser.open(f"https://www.google.com/search?q={app_name}")

    # SCREENSHOT
    elif "screenshot" in query:
        speak("Capturing your screen.")
        pyautogui.screenshot().save("screenshot.png")
        speak("Screenshot saved successfully.")

    # EXIT
    elif any(word in query for word in ["exit", "quit", "stop"]):
        speak("Goodbye. Shutting down NEXA.")
        QtWidgets.QApplication.quit()

    # AI ANSWERING
    else:
        speak("Analyzing your request.")
        answer = ask_groq(query)
        speak(answer)

# ======================================================
# FLOATING DOT GIF UI
# ======================================================
class FloatingGif(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(
            QtCore.Qt.FramelessWindowHint |
            QtCore.Qt.WindowStaysOnTopHint |
            QtCore.Qt.Tool
        )
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setFixedSize(120, 120)

        label = QtWidgets.QLabel(self)
        movie = QtGui.QMovie("assets/dot.gif")
        label.setMovie(movie)
        label.setScaledContents(True)
        movie.start()

        screen = QtWidgets.QApplication.primaryScreen().geometry()
        x = screen.width() - self.width() - 30
        y = screen.height() - self.height() - 70
        self.move(x, y)

    def mousePressEvent(self, event):
        pass  # Non-draggable

# ======================================================
# HOTWORD: “Hey NEXA”
# ======================================================
def hotword_listener():
    speak("NEXA is online. Say 'Hey NEXA' to activate.")
    while True:
        text = listen(timeout=4, phrase_limit=4)
        if "hey nexa" in text or "nexa" in text:
            speak("Hello, how can I help you?")
            command = listen(timeout=8, phrase_limit=8)
            execute_command(command)

# ======================================================
# MAIN
# ======================================================
def main():
    play_startup_sound()

    app = QtWidgets.QApplication(sys.argv)
    gif_window = FloatingGif()
    gif_window.show()

    listener = threading.Thread(target=hotword_listener, daemon=True)
    listener.start()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
