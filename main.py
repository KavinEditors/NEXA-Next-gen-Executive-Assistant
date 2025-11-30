import os
import threading
from playsound3 import playsound
from modules.voice import speak, listen_command
from modules.hotword import wait_for_hotword
from modules.actions import perform_action
from modules.groq_api import ask_groq
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie
import sys

# Floating GIF Indicator
def show_indicator():
    app = QApplication(sys.argv)
    label = QLabel()
    label.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
    label.setAttribute(Qt.WA_TranslucentBackground, True)
    label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    movie = QMovie("assets/dot.gif")
    label.setMovie(movie)
    movie.start()

    screen = app.primaryScreen().availableGeometry()
    label.move(screen.width() - 130, screen.height() - 130)  # bottom-right corner
    label.show()
    sys.exit(app.exec_())

def main():
    threading.Thread(target=show_indicator, daemon=True).start()
    playsound("assets/startup.mp3")
    speak("Hello, I'm Nexa. How can I help you today?")
    wait_for_hotword()

    while True:
        query = listen_command()
        if not query:
            continue

        if "search" in query:
            perform_action(query)
        else:
            playsound("assets/sound.mp3")
            answer = ask_groq(query)
            speak(answer)

if __name__ == "__main__":
    main()
