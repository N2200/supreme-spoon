import paho.mqtt.client as mqtt
from . import config

class MQTTClient:

    def __init__(self, broker=config.MQTT_BROKER, port=config.MQTT_PORT):
        self.handlers = []

        self.client = mqtt.Client()

        self.client.on_message = self._message_received

        self.broker = broker
        self.port = port


    def connect(self):
        print("Connecting to MQTT broker...")

        self.client.connect(
            self.broker,
            self.port
        )

        self.client.loop_start()


    def disconnect(self):
        self.client.loop_stop()
        self.client.disconnect()


    def subscribe(self, topic):
        print("Subscribing:", topic)
        self.client.subscribe(topic)


    def publish(self,device_name, topic, payload):
        topic = topic.replace("+", device_name)
        self.client.publish(topic, payload)
    
    


    def add_handler(self, handler):
        self.handlers.append(handler)


    def _message_received(self, client, userdata, msg):

        topic = msg.topic
        payload = msg.payload.decode()

        self.on_message(
            topic,
            payload
        )


    def on_message(self, topic, payload):

        for handler in self.handlers:
            handler(topic, payload)