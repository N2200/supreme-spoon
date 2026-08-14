import time

from mqtt.client import MQTTClient
from games.phasmophobia import topics
from games.phasmophobia.game_server import GameServer

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
        game.send_announcement("TEST")

except KeyboardInterrupt:
    mqtt.disconnect()