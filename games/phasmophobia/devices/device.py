import time

from mqtt.client import MQTTClient
from games.phasmophobia import topics
from games.phasmophobia.game_server import GameServer

name = "ghost-meter"
mqtt = MQTTClient()
game = GameServer(mqtt)
mqtt.add_handler(game.on_message)

mqtt.connect()


for topic in topics.SUBSCRIPTIONS:
    mqtt.subscribe(topic)

print("Device running")

try:
    while True:
        time.sleep(1)
        mqtt.publish(name,topics.SUBSCRIPTIONS[0],"Hello World")

except KeyboardInterrupt:
    mqtt.disconnect()