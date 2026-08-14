import json

from mqtt.client import MQTTClient
from games.phasmophobia import topics


class Device:

    def __init__(self, name):
        self.name = name
        self.mqtt = MQTTClient()

        # Register our MQTT message handler.
        self.mqtt.add_handler(self._on_mqtt_message)

    def connect(self):
        self.mqtt.connect()

        # Subscribe to messages sent from the server.
        for topic in topics.DEVICE_SUBSCRIPTIONS:
            self.mqtt.subscribe(topic)

        self.announce(f"{self.name} connected")

    def disconnect(self):
        self.announce(f"{self.name} disconnecting")
        self.mqtt.disconnect()

    # ------------------------------------------------------------------
    # Server -> Device
    # ------------------------------------------------------------------

    def _on_mqtt_message(self, topic, payload):
        """
        Handle any MQTT message received by this device.
        """

        self.parse_server_message(topic, payload)

    def parse_server_message(self, topic, payload):
        print(f"Received {topic}: {payload}")
        """
        Parse the actual message sent from the server.

        TODO: Implement the server message format later.
        """
        pass

    # ------------------------------------------------------------------
    # Device -> Server
    # ------------------------------------------------------------------

    def announce(self, message):
        self._send_device_message(
            topics.DEVICE_ANNOUNCE,
            message
        )

    def heartbeat(self, message):
        self._send_device_message(
            topics.DEVICE_HEARTBEAT,
            message
        )

    def event(self, message):
        self._send_device_message(
            topics.DEVICE_EVENTS,
            message
        )

    def _send_device_message(self, topic, message):
        payload = json.dumps({
            "device": self.name,
            "message": message
        })

        self.mqtt.publish(
            self.name,
            topic,
            payload
        )