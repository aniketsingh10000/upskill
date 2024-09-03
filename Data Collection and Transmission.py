# data_collector.py
import paho.mqtt.client as mqtt
import json
import random
import time

# MQTT settings
MQTT_BROKER = 'broker.hivemq.com'
MQTT_PORT = 1883
MQTT_TOPIC = 'water_monitoring/sensor_data'

# Connect to MQTT broker
client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

def collect_data():
    return {
        'flow_rate': random.uniform(0.0, 10.0),
        'leak_detected': random.choice([True, False])
    }

while True:
    data = collect_data()
    client.publish(MQTT_TOPIC, json.dumps(data))
    print("Data sent:", data)
    time.sleep(10)  # Send data every 10 seconds
