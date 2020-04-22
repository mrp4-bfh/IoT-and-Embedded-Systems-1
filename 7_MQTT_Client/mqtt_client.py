#################################################################
#
# Code by P. Marti BFH 21.04.2019
# Ecercise MQTT FS 2019
# 
# Run on your Raspberry Pi, PC or Mac
#   
#################################################################
import paho.mqtt.client as mqtt
# MQTT Server Information 
SERVER = "m24.cloudmqtt.com"
PORT = 14362
# User login if needed
USER ='USER'
PW ='PW'
# MQTT broker topic (subscribe)
TOPIC='TOPIC'

def on_connect(client,userdata,flags,rc):
    print('connected with result code {0}'.format(rc))
    client.subscribe(TOPIC)
    
def on_message(client,userdata,msg):
    t,h,p=[float(x) for x in msg.payload.decode("utf-8").split(',')]
    print('{0}C     {1}%      {2}mPa'.format(t,h,p))
    
client=mqtt.Client()
client.username_pw_set(USER, PW)
client.connect(SERVER,port=PORT,keepalive=60,bind_address='0.0.0.0')
client.on_connect=on_connect
client.on_message=on_message

#client.subscribe("")
client.loop_start()
input("Press enter to terminate")
