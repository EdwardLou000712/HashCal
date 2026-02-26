from models import SessionEvent
from storage import save_session

def create_new_session(file_path, parent_id=None, description=""):
    event = SessionEvent.create(
        file_path=file_path,
        parent_id=parent_id,
        description=description
    )
    save_session(event)
    print(f"Created session {event.session_id}")
    return event.session_id
