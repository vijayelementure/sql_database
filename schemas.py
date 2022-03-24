from pydantic import BaseModel
import paho.mqtt.client as paho
import time

'''class UserBase(BaseModel):
    username = "vijay"
    email = "vijaybhaskarmyv@gmail.com"
    password = "vaishu"'''


def recieving(client, userdata, msg):
        print("topics :" + msg.topic + " , " +  " payload :"  + msg.payload.decode())
        var = UserBase(msg)
        print(var.pub_topic)
        print(var.topic_payload)


client = paho.Client("python")
client.on_message = recieving

if client.connect("fueb.elementure.live",1883,60) != 0:
    print("not connected to MQTT broker")

client.loop_start()

client.subscribe("lock/status")

class UserBase(BaseModel):
    def __init__(self,mes):
        self.pub_topic = mes.topic
        self.topic_payload = mes.payload.decode()


time.sleep(30)
client.loop_stop()

client.disconnect() 
print("disconnected")



  