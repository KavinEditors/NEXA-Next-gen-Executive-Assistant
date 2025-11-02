import pywhatkit
from modules.voice import speak

def perform_action(command):
    try:
        if "search" in command:
            query = command.replace("search", "").strip()
            speak(f"Searching for {query}")
            pywhatkit.search(query)
        else:
            speak("I couldn’t identify your command.")
    except Exception as e:
        speak(f"Error performing action: {str(e)}")
