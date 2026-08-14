ROOT = "phasmophobia"

# Topics published by devices (device -> server)
DEVICE_ANNOUNCE = f"{ROOT}/device/announce"
DEVICE_HEARTBEAT = f"{ROOT}/device/heartbeat"
DEVICE_EVENTS = f"{ROOT}/device/events"

# Topics the server subscribes to (device -> server)
SUBSCRIPTIONS = [
    DEVICE_ANNOUNCE,
    DEVICE_HEARTBEAT,
    DEVICE_EVENTS,
]

# Topics published by server (server -> device)
SERVER_COMMANDS = f"{ROOT}/server/+/commands"
SERVER_ANNOUNCE = f"{ROOT}/server/+/announce"
# Topics devices should subscribe to (server -> device)
DEVICE_SUBSCRIPTIONS = [
    SERVER_COMMANDS,
    SERVER_ANNOUNCE,
]
