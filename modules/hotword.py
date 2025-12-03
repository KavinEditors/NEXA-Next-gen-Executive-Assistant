from modules.voice import listen_command, speak

def wait_for_hotword():
    speak("Say 'Hey Nexa' to activate me.")
    while True:
        command = listen_command()
        if not command:
            continue

        if "hey nexa" in command or "hey alexa" in command:
            # Extract additional text after hotword
            cleaned = command.replace("hey nexa", "").replace("hey alexa", "").strip()

            speak("Yes, I'm listening.")

            return cleaned