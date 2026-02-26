import json
import os

STORAGE_FILE = "sessions.json"

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

def find_session(session_id):
    sessions = load_sessions()
    for s in sessions:
        if s["session_id"] == session_id:
            return s
    return None
