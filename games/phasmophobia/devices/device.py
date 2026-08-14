import time

from games.phasmophobia.device_logic import Device


device = Device("ghost-meter")

device.connect()
print(f"{device.name} online")

heartbeat_message = {
  "type": "heartbeat",
  "device_id": "ghost-meter-01",
  "room": "hallway"
}

try:
    while True:
         time.sleep(5)
         device.heartbeat(heartbeat_message)

except KeyboardInterrupt:
    device.disconnect()