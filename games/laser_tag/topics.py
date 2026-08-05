ROOT = "room"

def announce(device):
    return f"{ROOT}/device/{device}/announce"

def heartbeat(device):
    return f"{ROOT}/device/{device}/heartbeat"

def config(device):
    return f"{ROOT}/device/{device}/config"

def commands(device):
    return f"{ROOT}/device/{device}/commands"

def events(device):
    return f"{ROOT}/device/{device}/events"

DISCOVERY = f"{ROOT}/device/+/announce"
HEARTBEAT = f"{ROOT}/device/+/heartbeat"
EVENTS = f"{ROOT}/device/+/events"

SUBSCRIPTIONS = [
    DISCOVERY,
    HEARTBEAT,
    EVENTS,
]