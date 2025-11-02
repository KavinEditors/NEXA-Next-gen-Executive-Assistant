from modules.voice import listen_command, speak

def wait_for_hotword():
    speak("Say 'Hey Nexa' to activate me.")
    while True:
        command = listen_command()
        if "hey nexa" in command:
            speak("Yes, I'm listening.")
            break
