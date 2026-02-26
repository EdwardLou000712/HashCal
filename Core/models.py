from dataclasses import dataclass, asdict
from datetime import datetime
import uuid
import hashlib
import os

@dataclass
class SessionEvent:
    session_id: str
    parent_id: str | None
    timestamp: str
    file_hash: str
    description: str

    @staticmethod
    def create(file_path: str, parent_id=None, description=""):
        return SessionEvent(
            session_id=str(uuid.uuid4()),
            parent_id=parent_id,
            timestamp=datetime.utcnow().isoformat(),
            file_hash=SessionEvent.hash_file(file_path),
            description=description
        )

    @staticmethod
    def hash_file(path):
        sha = hashlib.sha256()
        with open(path, "rb") as f:
            while chunk := f.read(4096):
                sha.update(chunk)
        return sha.hexdigest()

    def to_dict(self):
        return asdict(self)
