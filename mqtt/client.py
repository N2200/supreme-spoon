import json
import paho.mqtt.client as mqtt

from . import config


class MQTTClient:

    def __init__(self):

        self.client = mqtt.Client(
            mqtt.CallbackAPIVersion.VERSION2,
            client_id=config.CLIENT_ID
        )

        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_disconnect = self.on_disconnect

        self.handlers = {}

    def connect(self):

        self.client.connect(
            config.MQTT_BROKER,
            config.MQTT_PORT,
            config.KEEPALIVE
        )

        self.client.loop_start()

    def disconnect(self):

        self.client.loop_stop()
        self.client.disconnect()

    def subscribe(self, topic):

        self.client.subscribe(topic)

    def publish(self, topic, payload, retain=False, qos=0):

        self.client.publish(
            topic,
            json.dumps(payload),
            qos=qos,
            retain=retain
        )

    def add_handler(self, topic, callback):

        self.handlers[topic] = callback

    def on_connect(self, client, userdata, flags, reason_code, properties):

        print("Connected")

    def on_disconnect(self, client, userdata, flags, reason_code, properties):

        print("Disconnected")

    def on_message(self, client, userdata, msg):

        payload = json.loads(msg.payload.decode())

        print(msg.topic)
        print(payload)

        if msg.topic in self.handlers:
            self.handlers[msg.topic](payload)
