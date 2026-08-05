import time

from mqtt.client import MQTTClient
from games.laser_tag import topics
from games.laser_tag.game_server import GameServer

mqtt = MQTTClient()
game = GameServer(mqtt)
mqtt.add_handler(game.on_message)

mqtt.connect()


for topic in topics.SUBSCRIPTIONS:
    mqtt.subscribe(topic)

print("Server running")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    mqtt.disconnect()