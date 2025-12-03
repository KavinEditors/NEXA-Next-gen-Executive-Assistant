import subprocess
import webbrowser
import os

apps = {
    "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "goodle": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\NEW\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "vsc": r"C:\Users\NEW\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "visual studio code": r"C:\Users\NEW\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "notepad": r"C:\Windows\System32\notepad.exe",
    "explorer": r"C:\Windows\explorer.exe",
    "cmd": r"C:\WINDOWS\system32\cmd.exe",
    "magnifier": r"C:\WINDOWS\system32\Magnify.exe",
    "vlc": r"C:\Program Files (x86)\VideoLAN\VLC\vlc.exe"
}

websites = {
    "github": "https://github.com",
    "youtube": "https://youtube.com",
    "discord": "https://discord.com/app",
    "whatsapp web": "https://web.whatsapp.com",
    "canva": "https://www.canva.com",
    "instagram": "https://instagram.com",
    "twitter": "https://x.com",
    "x": "https://x.com",
    "spotify": "https://open.spotify.com",
    "stackoverflow": "https://stackoverflow.com",
    "chatgpt": "https://chat.openai.com",
    "netflix": "https://netflix.com",
    "prime video": "https://primevideo.com"
}

def open_app(name):
    for key, path in apps.items():
        if name in key:
            subprocess.Popen([path])
            return f"Opening {key.capitalize()}."
    return None


def control_system(cmd):
    # Power Control
    if "shutdown" in cmd:
        os.system("shutdown /s /t 3")
        return "Shutting down system."

    if "restart" in cmd:
        os.system("shutdown /r /t 3")
        return "Restarting system."

    if "logout" in cmd or "sign out" in cmd:
        os.system("shutdown /l")
        return "Logging out."

    if "sleep" in cmd:
        os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
        return "Putting system to sleep."

    if "lock" in cmd:
        os.system("rundll32.exe user32.dll,LockWorkStation")
        return "Locking system."

    # Volume
    if "mute" in cmd:
        os.system("nircmd.exe mutesysvolume 1")
        return "Muted system volume."

    if "unmute" in cmd:
        os.system("nircmd.exe mutesysvolume 0")
        return "Unmuted system volume."

    if "increase volume" in cmd or "volume up" in cmd:
        os.system("nircmd.exe changesysvolume 5000")
        return "Increasing volume."

    if "decrease volume" in cmd or "volume down" in cmd:
        os.system("nircmd.exe changesysvolume -5000")
        return "Decreasing volume."

    # Brightness
    if "increase brightness" in cmd:
        os.system("nircmd.exe setbrightness +10")
        return "Increasing brightness."

    if "decrease brightness" in cmd:
        os.system("nircmd.exe setbrightness -10")
        return "Decreasing brightness."

    # WiFi
    if "turn on wifi" in cmd or "wifi on" in cmd:
        os.system('netsh interface set interface "Wi-Fi" admin=enabled')
        return "Turning on WiFi."

    if "turn off wifi" in cmd or "wifi off" in cmd:
        os.system('netsh interface set interface "Wi-Fi" admin=disabled')
        return "Turning off WiFi."

    # Hotspot
    if "hotspot on" in cmd or "turn on hotspot" in cmd:
        os.system("netsh wlan start hostednetwork")
        return "Turning on Hotspot."

    if "hotspot off" in cmd or "turn off hotspot" in cmd:
        os.system("netsh wlan stop hostednetwork")
        return "Turning off Hotspot."

    # Bluetooth
    if "bluetooth on" in cmd:
        os.system('powershell -command "Start-Service bthserv"')
        return "Turning on Bluetooth."

    if "bluetooth off" in cmd:
        os.system('powershell -command "Stop-Service bthserv"')
        return "Turning off Bluetooth."

    # Battery Saver
    if "battery saver on" in cmd:
        os.system('powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 98')
        os.system('powercfg /s SCHEME_CURRENT')
        return "Enabling battery saver."

    if "battery saver off" in cmd:
        os.system('powercfg /setdcvalueindex SCHEME_CURRENT SUB_ENERGYSAVER ESBATTTHRESHOLD 0')
        os.system('powercfg /s SCHEME_CURRENT')
        return "Disabling battery saver."

    return None

def perform_action(query: str):
    query = query.lower()
    commands = [c.strip() for c in query.replace(" and ", ",").split(",")]
    responses = []

    for cmd in commands:

        # ---------------- System Controls ----------------
        sys_result = control_system(cmd)
        if sys_result:
            responses.append(sys_result)
            continue

        # ---------------- Website Opening ----------------
        if cmd in websites:   # Direct match e.g. "youtube"
            webbrowser.open(websites[cmd])
            responses.append(f"Opening {cmd}.")
            continue

        # If command starts with "open" followed by website/app name
        if cmd.startswith("open"):
            name = cmd.replace("open", "").strip()

            # Check website list
            for site in websites:
                if name == site or name.replace(" ", "") == site.replace(" ", ""):
                    webbrowser.open(websites[site])
                    responses.append(f"Opening {site}.")
                    break
            else:
                # Try app opening
                r = open_app(name)
                if r:
                    responses.append(r)
                else:
                    webbrowser.open(f"https://www.google.com/search?q={name}")
                    responses.append(f"Searching for {name}.")
            continue

        # ---------------- Search Internet ----------------
        if cmd.startswith("search"):
            term = cmd.replace("search", "").strip()
            if term:
                webbrowser.open(f"https://www.google.com/search?q={term}")
                responses.append(f"Searching {term}.")
            continue

    return " | ".join(responses) if responses else None