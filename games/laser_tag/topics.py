ROOT = "room"

DISCOVERY = f"{ROOT}/device/+/announce"
HEARTBEAT = f"{ROOT}/device/+/heartbeat"
EVENTS = f"{ROOT}/device/+/events"

SUBSCRIPTIONS = [
    DISCOVERY,
    HEARTBEAT,
    EVENTS,
]