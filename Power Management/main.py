from machine import Pin, I2C, idle, RTC, freq
from time import sleep
import BME280
import os

rtc = RTC()
rtc.datetime((2020, 3, 17, 0, 6, 0, 0, 0))

# ESP32 - Pin assignement
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)

# Scan for your BME280 with the i2c.scan() function
try:
    bme = BME280.BME280(i2c=i2c)
except OSError as e:
    print('Failed to read/publish sensor readings.')

i = 0

while i < 20:
    # Get data from BME280
    temp = bme.temperature
    hum = bme.humidity
    pres = bme.pressure
    time = str(rtc.datetime())

    # Build a String
    sensor_readings = {'temp: '+temp+' humy: '+hum+' presure: '+pres+' log: '+time}
    print(sensor_readings)


    # Write so in file
    f = open('data.txt', 'a')
    f.write(str(sensor_readings)+'\n')
    f.close()

    sleep(0.5)
    i += 1