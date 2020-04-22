#################################################################
#
# Code by P. Marti BFH 21.04.2019
# Ecercise MQTT FS 2019
#
#################################################################
import time
from umqttsimple import MQTTClient
from machine import Pin, I2C, reset
import BME280 
import esp
import gc

gc.collect()

# MQTT Server Information 
SERVER ='m24.cloudmqtt.com' #TODO
CLIENT_ID='ESP32'           #TODO
PORT=14362                  #TODO
TOPIC_PUB=b'temp_humidity'  #aka tag publish
TOPIC_SUB=b'led1'           #aka tag subscribe
# User login if needed
USERNAME = 'YOUR_USER_NAME' #TODO
PASSWORD = 'YOUR_PASSWORD'  #TODO

# Update parameter
last_sensor_reading = 0
readings_interval = 5

# Create library object using our bus I2C port
i2c1 = I2C(scl=Pin(22), sda=Pin(23), freq=10000)
#1 Create led object using pin class
led=Pin(13,Pin.OUT)

#Read data from BME280 sensor
def read_ds_sensor():
  try:
    bme = BME280.BME280(i2c=i2c1)
    t = float(bme.read_temperature()) / 100
    p = float(bme.read_pressure()) / 100
    h = float(bme.read_humidity()) / 1024
    if isinstance(t, float) and isinstance(p, float) and isinstance(t, float):
      msg = (b'{0:3.1f},{1:3.1f},{2:3.1f}'.format(t,h,p))
      print(msg)
      return msg
    else:
      print('invalid sensor value')
  except OSError:
    print ('failed to read sensor')
    reset()

#Read LED state    
def sub_cb(topic, msg):
  print((topic, msg))
  if msg == b'on':
    led.value(1)
  elif msg == b'off':
    led.value(0)

# try to connect to the MQTT Broker    
def connect_and_subscribe():
  global CLIENT_ID, SERVER, PORT, USERNAME, PASSWORD, TOPIC_PUB
  client=MQTTClient(CLIENT_ID, SERVER,PORT , USERNAME, PASSWORD)
  client.set_callback(sub_cb)
  client.connect()
  client.subscribe(TOPIC_SUB)
  print('Connected to %s MQTT broker, subscribed to %s topic' % (SERVER, TOPIC_SUB))
  return client

# Restart the Conecction
def restart_and_reconnect():
  print('Failed to connect to MQTT broker. Reconnecting...')
  time.sleep(5)
  reset()
  
# Try to connect to the MQTT Sercer
try:
  client = connect_and_subscribe()
except OSError as e:
  restart_and_reconnect()

# Main Routine
while True:
  try:
    #TODO
    # 2nd step, wait for msg
    #client.wait_msg()
    if (time.time() - last_sensor_reading) > readings_interval:
      msg = read_ds_sensor()
      client.publish(TOPIC_PUB, msg)
      last_sensor_reading = time.time()
  except OSError as e:
    restart_and_reconnect()

