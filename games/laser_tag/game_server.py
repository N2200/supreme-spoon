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

    def device_announced(self, topic, payload):
        print("Device announced:", topic, payload)

    def device_heartbeat(self, topic, payload):
        print("Heartbeat:", topic, payload)

    def device_event(self, topic, payload):
        print("Event:", topic, payload)

        # Example:
        # self.mqtt.publish("room/device/light/commands", "on")