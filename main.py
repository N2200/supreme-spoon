from mqtt.client import MQTTClient
from mqtt.handlers import device_announced
from mqtt import topics
import time

mqtt = MQTTClient()

mqtt.add_handler(
    topics.DISCOVERY,
    device_announced
)

mqtt.connect()

mqtt.subscribe(topics.DISCOVERY)

print("Server running")


try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    mqtt.disconnect()