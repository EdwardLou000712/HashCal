import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(BASE_DIR, "sessions.json")

def load_sessions():
    if not os.path.exists(STORAGE_FILE):
        return []
    with open(STORAGE_FILE, "r") as f:
        return json.load(f)

def save_session(event):
    sessions = load_sessions()
    sessions.append(event.to_dict())
    with open(STORAGE_FILE, "w") as f:
        json.dump(sessions, f, indent=4)