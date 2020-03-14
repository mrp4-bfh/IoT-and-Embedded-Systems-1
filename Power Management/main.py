from machine import Pin, I2C, idle
from time import sleep
import BME280

# ESP32 - Pin assignement
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignement
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)

try:
    bme = BME280.BME280(i2c=i2c)
except OSError as e:
    print('Failed to read/publish sensor readings.')

i = 0

while i < 10:
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    sensor_readings = {'value1':temp, 'value2':hum, 'value3':pres}
    print(sensor_readings)
    sleep(1)
    i += 1
