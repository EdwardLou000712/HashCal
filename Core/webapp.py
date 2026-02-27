import os
import json
import uuid
import hashlib
from datetime import datetime
from flask import Flask, request, jsonify, send_file
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Force the storage file to live in the same folder as this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STORAGE_FILE = os.path.join(BASE_DIR, "sessions.json")

def get_ledger():
    """Helper to safely load the JSON ledger."""
    if not os.path.exists(STORAGE_FILE):
        return []
    try:
        with open(STORAGE_FILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_ledger(data):
    """Helper to safely write the JSON ledger."""
    with open(STORAGE_FILE, "w") as f:
        json.dump(data, f, indent=4)

@app.route('/sessions', methods=['GET'])
def get_sessions():
    return jsonify(get_ledger())

@app.route('/track', methods=['POST'])
def track_session():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    parent_id = request.form.get('parent_id')
    description = request.form.get('description', "")

    # Hash calculation (Original logic)
    sha = hashlib.sha256()
    while chunk := file.read(4096):
        sha.update(chunk)
    file_hash = sha.hexdigest()

    event = {
        "session_id": str(uuid.uuid4()),
        "parent_id": parent_id if parent_id and parent_id != "null" else None,
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "file_hash": file_hash,
        "description": description,
        "file_name": file.filename
    }

    # Atomic update
    ledger = get_ledger()
    ledger.append(event)
    save_ledger(ledger)

    return jsonify(event)

if __name__ == '__main__':
    # Initialize file on startup
    if not os.path.exists(STORAGE_FILE):
        save_ledger([])
    app.run(port=5000, debug=True)