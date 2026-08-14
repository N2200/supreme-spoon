from games.phasmophobia import topics
import json

class GameServer:

    def __init__(self, mqtt):
        self.mqtt = mqtt

        self.routes = {
            "announce": self.device_announced,
            "heartbeat": self.device_heartbeat,
            "events": self.device_event,
        }

    def on_message(self, topic, payload):

        last = topic.split("/")[-1]

        if last in self.routes:
            self.routes[last](topic, payload)
# ---------------------------------------------------------
    # Device -> Server
    # ---------------------------------------------------------

    def device_announced(self, topic, payload):
        print("Device announced:", topic, payload)

    def device_heartbeat(self, topic, payload):
        print("Heartbeat:", topic, payload)

    def device_event(self, topic, payload):
        print("Event:", topic, payload)

    # ---------------------------------------------------------
    # Server -> Device
    # ---------------------------------------------------------

    def send_command(self, device_name, message):
        payload = json.dumps({
            "message": message
        })

        topic = topics.SERVER_COMMANDS.replace("+", device_name)

        self.mqtt.publish(topic, payload)



    def send_announcement(self, message):
        payload = json.dumps({
            "message": message
        })

        self.mqtt.publish(
            topics.SERVER_ANNOUNCE,
            payload
        )