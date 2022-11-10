import paho.mqtt.client as paho

def on_connect(client, userdata, flags, rc):
    print('CONNACK received with code %d.' % (rc))

client = paho.Client()
client.on_connect = on_connect
client.connect('broker.mqttdashboard.com', 1883)

import paho.mqtt.client as paho
import time

def on_publish(client, userdata, mid):
    print("mid: "+str(mid))
 
client = paho.Client()
client.on_publish = on_publish
client.connect('broker.mqttdashboard.com', 1883)
client.loop_start()

while True:
    temperature = ('GG')
    (rc, mid) = client.publish('encyclopedia/temperature', str(temperature), qos=1)
    time.sleep(30)
