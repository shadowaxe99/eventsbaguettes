```python
import datetime
from src.event_management import eventData

def scheduleEvent(event_id, start_time, end_time):
    """
    Function to schedule an event.
    """
    if not isinstance(start_time, datetime.datetime) or not isinstance(end_time, datetime.datetime):
        raise ValueError("Start time and end time must be datetime objects")

    if start_time >= end_time:
        raise ValueError("Start time must be before end time")

    if event_id not in eventData:
        raise ValueError("Event ID not found")

    eventData[event_id]['start_time'] = start_time
    eventData[event_id]['end_time'] = end_time

    return eventData[event_id]

def getEventSchedule(event_id):
    """
    Function to get the schedule of an event.
    """
    if event_id not in eventData:
        raise ValueError("Event ID not found")

    return eventData[event_id]['start_time'], eventData[event_id]['end_time']

def rescheduleEvent(event_id, new_start_time, new_end_time):
    """
    Function to reschedule an event.
    """
    if not isinstance(new_start_time, datetime.datetime) or not isinstance(new_end_time, datetime.datetime):
        raise ValueError("New start time and new end time must be datetime objects")

    if new_start_time >= new_end_time:
        raise ValueError("New start time must be before new end time")

    if event_id not in eventData:
        raise ValueError("Event ID not found")

    eventData[event_id]['start_time'] = new_start_time
    eventData[event_id]['end_time'] = new_end_time

    return eventData[event_id]
```