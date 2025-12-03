import os
import threading
import sys
import time
from playsound3 import playsound
from modules.voice import speak, listen_command
from modules.hotword import wait_for_hotword
from modules.actions import perform_action
from modules.groq_api import ask_groq
from PyQt5.QtWidgets import QApplication, QLabel
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie

# Floating GIF Indicator
def show_indicator():
    app = QApplication(sys.argv)
    label = QLabel()
    label.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.Tool)
    label.setAttribute(Qt.WA_TranslucentBackground, True)
    label.setAttribute(Qt.WA_TransparentForMouseEvents, True)

    movie = QMovie("assets/dot.gif")
    movie.setScaledSize(QSize(120, 105))
    label.setMovie(movie)
    movie.start()

    screen = app.primaryScreen().availableGeometry()
    w, h = 120, 105
    label.setFixedSize(w, h)
    label.move(screen.width() - 50 - w, screen.height() - 50 - h)
    label.show()

    app.exec_()

def voice_engine():
    playsound("assets/startup.mp3")
    speak("Hello, I'm Nexa. Say 'Hey Nexa' to activate me.")

    while True:
        inline_cmd = wait_for_hotword()
        print("Hotword detected, inline command:", inline_cmd)

        if inline_cmd:
            response = perform_action(inline_cmd)
            if response:
                speak(response)
            else:
                playsound("assets/sound.mp3")
                answer = ask_groq(inline_cmd)
                speak(answer)

            # ---------- Continuous Listening Mode ----------
            while True:
                start_time = time.time()
                speak("I'm listening...")

                while time.time() - start_time < 4:
                    query = listen_command()
                    if query:
                        if "stop listening" in query or "standby" in query:
                            speak("Entering standby hotword mode.")
                            break

                        response = perform_action(query)
                        if response:
                            speak(response)
                        else:
                            playsound("assets/sound.mp3")
                            answer = ask_groq(query)
                            speak(answer)

                        start_time = time.time()
                    time.sleep(0.1)

                break  # End continuous mode and return to hotword mode


def main():
    threading.Thread(target=show_indicator, daemon=True).start()
    voice_engine()


if __name__ == "__main__":
    main()
