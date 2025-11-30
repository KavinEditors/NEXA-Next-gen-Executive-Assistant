import os
import threading
from playsound3 import playsound
from modules.voice import speak, listen_command
from modules.hotword import wait_for_hotword
from modules.actions import perform_action
from modules.groq_api import ask_groq
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QSize
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
    movie.setScaledSize(QSize(50, 50))  # smaller GIF
    label.setMovie(movie)
    movie.start()

    screen = app.primaryScreen().availableGeometry()
    margin_right = 50
    margin_bottom = 50
    w, h = 50, 50
    label.setFixedSize(w, h)
    label.move(screen.width() - margin_right - w, screen.height() - margin_bottom - h)
    label.show()
    sys.exit(app.exec_())

def main():
    # Start floating GIF
    threading.Thread(target=show_indicator, daemon=True).start()

    # Startup greeting
    playsound("assets/startup.mp3")
    speak("Hello, I'm Nexa. How can I help you today?")

    # Hotword loop
    while True:
        wait_for_hotword()  # Blocks until "Hey Nexa" is said

        # Command listening loop after hotword
        speak("Yes, I'm listening.")
        while True:
            query = listen_command()
            if not query:
                continue
            query = query.lower()

            # Exit inner loop if user says stop
            if "stop listening" in query or "thank you" in query:
                speak("Going back to standby.")
                break

            # Perform action
            response = perform_action(query)
            if response:
                speak(response)
            else:
                playsound("assets/sound.mp3")
                answer = ask_groq(query)
                speak(answer)

if __name__ == "__main__":
    main()
