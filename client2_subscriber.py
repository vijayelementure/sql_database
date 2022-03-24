import paho.mqtt.client as paho
import time

def recieving(client, userdata, msg):
    print(msg.topic + " : " + msg.payload.decode()) 

client = paho.Client("python")
client.on_message = recieving

if client.connect("fueb.elementure.live",1883,60) != 0:
    print("not connected to MQTT broker")

client.loop_start()

client.subscribe("lock/status")
time.sleep(30)
client.loop_stop()

client.disconnect() 
print("disconnected")