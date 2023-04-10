
__author__ = "Fabian Astudillo"
__copyright__ = "Copyleft 2023"
__credits__ = ["Fabian Astudillo"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Fabian Astudillo"
__email__ = "fabian.astudillos@ucuenca.edu.ec"
__status__ = "test"

import paho.mqtt.client as mqtt

MQTT_BROKER = "mosquitto"
MQTT_FORWARDER_TOPIC = "forwarded/topic"
MQTT_REMOTE_BROKER = "10.0.2.83"
MQTT_REMOTE_PORT = 1883

def on_connect(client, userdata, flags, rc):
    print("Conectado al broker MQTT local")
    client.subscribe(MQTT_FORWARDER_TOPIC)

def on_message(client, userdata, message):
    print(f"Recibido mensaje en el topic {message.topic}")
    forwarder_client = mqtt.Client()
    forwarder_client.connect(MQTT_REMOTE_BROKER, MQTT_REMOTE_PORT)
    forwarder_client.publish(message.topic, payload=message.payload)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(MQTT_BROKER)

client.loop_forever()
