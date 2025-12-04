import speech_recognition as sr
import pyttsx3
import threading

engine = pyttsx3.init()
engine.setProperty("rate", 175)
voices = engine.getProperty("voices")

# Keep your original voice intact
engine.setProperty("voice", voices[1].id)

# A flag to stop TTS instantly
stop_flag = False

def speak(text):
    global stop_flag
    stop_flag = False

    print(f"NEXA: {text}")

    def run_tts():
        global stop_flag
        engine.say(text)
        engine.runAndWait()

    t = threading.Thread(target=run_tts)
    t.start()
    t.join()

def stop_speaking():
    """Instantly stops ongoing TTS (called when popup X is pressed)."""
    global stop_flag
    stop_flag = True
    engine.stop()

def listen_command():
    r = sr.Recognizer()
    r.pause_threshold = 1.2
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.7)
        audio = r.listen(source, timeout=None, phrase_time_limit=None)
    try:
        command = r.recognize_google(audio).lower()
        print(f"You said: {command}")
        return command
    except:
        return ""

