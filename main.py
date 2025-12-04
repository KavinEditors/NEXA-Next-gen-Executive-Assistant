import sys
import threading
import time
import subprocess
from playsound3 import playsound
from pywinauto.application import Application
from pywinauto import keyboard
from pywinauto.findwindows import find_windows, WindowNotFoundError
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie

from modules.voice import speak
from modules.hotword import wait_for_hotword
from modules.actions import perform_action, apps
from modules.groq_api import ask_groq


# -------------------- Typing Functions --------------------
def type_in_notepad(text):
    """Always open a new Notepad and type text."""
    try:
        app = Application().start(r"C:\Windows\System32\notepad.exe")
        time.sleep(0.8)
        notepad = app.window(title_re=".*Notepad.*")
        notepad.set_focus()
        threading.Thread(target=lambda: keyboard.send_keys(text, with_spaces=True, pause=0.02), daemon=True).start()
    except Exception as e:
        print("Typing in Notepad failed:", e)


def type_in_app(app_path, text, app_title=None):
    """Open/focus an app and type text in it."""
    try:
        if app_title:
            hwnds = find_windows(title_re=f".*{app_title}.*", visible_only=True)
            if hwnds:
                app = Application().connect(handle=hwnds[0])
                w = app.window(handle=hwnds[0])
                w.set_focus()
            else:
                raise WindowNotFoundError
        else:
            raise WindowNotFoundError
    except WindowNotFoundError:
        # Open app if not found
        app = Application().start(app_path)
        time.sleep(1)
        w = app.top_window()
        w.set_focus()

    threading.Thread(target=lambda: keyboard.send_keys(text, with_spaces=True, pause=0.02), daemon=True).start()


def speak_and_type(text, target_app_name=None, text_to_type=None):
    """
    Speak text via TTS and type simultaneously.
    target_app_name: None -> Notepad
    text_to_type: If None, type same as text
    """
    if target_app_name and target_app_name.lower() in apps:
        app_path = apps[target_app_name.lower()]
        app_title = target_app_name.capitalize()
        tts_thread = threading.Thread(target=speak, args=(text,))
        tts_thread.start()
        type_in_app(app_path, text_to_type if text_to_type else text, app_title)
        tts_thread.join()
    else:
        # Default -> Notepad
        tts_thread = threading.Thread(target=speak, args=(text,))
        tts_thread.start()
        type_in_notepad(text_to_type if text_to_type else text)
        tts_thread.join()


# -------------------- Voice Engine --------------------
def voice_engine():
    playsound("assets/startup.mp3")
    speak("Hello, I am Nexa. Say Hey Nexa to activate me.")

    while True:
        hotword = wait_for_hotword()
        if hotword:
            # Unpack three values now
            action_result, target_app_name, text_to_type = perform_action(hotword)

            if action_result:
                speak_and_type(action_result, target_app_name, text_to_type)
            else:
                ai_response = ask_groq(hotword)
                speak_and_type(ai_response)

        time.sleep(0.2)


# -------------------- PyQt Indicator --------------------
def create_indicator(label):
    movie = QMovie("assets/dot.gif")
    movie.setScaledSize(QSize(120, 105))
    label.setMovie(movie)
    movie.start()


# -------------------- Main --------------------
def main():
    app = QApplication(sys.argv)

    label = QLabel()
    label.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
    label.setAttribute(Qt.WA_TranslucentBackground, True)
    label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    create_indicator(label)
    screen = app.primaryScreen().availableGeometry()
    w, h = 120, 105
    label.setFixedSize(w, h)
    label.move(screen.width() - 50 - w, screen.height() - 50 - h)
    label.show()

    threading.Thread(target=voice_engine, daemon=True).start()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
