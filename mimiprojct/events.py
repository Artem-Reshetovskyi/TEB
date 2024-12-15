from enum import Enum

class EventType(Enum):
    BUG_FIX = "Bug Fix"
    ABSENCE = "Absence"
    SYSTEM_CRASH = "System Crash"

class Event:
    def __init__(self, event_type: EventType, impact: str):
        self.event_type = event_type
        self.impact = impact

    def apply_event(self):
        print(f"Event triggered: {self.event_type.value}. Impact: {self.impact}")