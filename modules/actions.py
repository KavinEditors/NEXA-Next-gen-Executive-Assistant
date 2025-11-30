import subprocess
import pywhatkit
import os

# Paths to applications
apps = {
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\NEW\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
}

def perform_action(query):
    query = query.lower()

    # Open applications
    for app_name, path in apps.items():
        if f"open {app_name}" in query or query.strip() == app_name:
            try:
                subprocess.Popen([path])
                return f"Opening {app_name.capitalize()}..."
            except Exception as e:
                return f"Failed to open {app_name}: {e}"

    # Search in Chrome/Edge using pywhatkit
    if "search" in query:
        try:
            # Extract search term
            search_term = query.split("search", 1)[1].strip()
            if not search_term:
                return "Please say what you want to search."
            
            # Open Chrome or Edge directly and search
            browser_path = apps.get("chrome")  # Change to 'edge' if needed
            pywhatkit.search(search_term, browser=browser_path)
            return f"Searching for '{search_term}'..."
        except Exception as e:
            return f"Failed to search: {e}"

    return "Sorry, I can't perform that action."
