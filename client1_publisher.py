import paho.mqtt.client as paho
import time

client = paho.Client()

if client.connect("fueb.elementure.live")!=0:
    print("not connected to MQTT broker")

client.loop_start()

client.publish("lock/status", "publishing lock status",0)

time.sleep(30)
client.loop_stop()
client.disconnect()
print("disconnected")