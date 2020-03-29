__author__      = "Patrik Marti"
__copyright__   = "Copyright 2020, Berner Fachhochschule BFH, IoT anb Embedded Systems"
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Patrik Marti"
__email__       = "patrik.marti@bfh.ch"
__status__      = "testing"

from machine import Pin, I2C
from time import sleep, sleep_ms
import BME280
import display 

#Debug
sleep(2)

#Button
blue    = Pin(35, Pin.IN)
yellow  = Pin(34, Pin.IN)

#7 Segment
disp = display.display(Pdig1=15,Pdig2=4,PsegA=32,PsegB=33,PsegC=18,PsegD=19,PsegE=23,PsegF=25,PsegG=26,PsegDot=5)

#I2C
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# Scan for your BME280 with the i2c.scan() function
try:
    bme = BME280.BME280(i2c=i2c)
except OSError as e:
    print('Failed to read/publish sensor readings.')

#*************** local variables *******************

block = False
run = True
state = 0
refresh_rate = 1
btc1 = 0
btc2 = 0
show = 0
indentation = 0

#*************** helper fuction *******************

def getSensorData():
    temp = int(bme.read_temperature()/100)
    humy = int(bme.read_humidity()/1000)    
    return [temp, humy]

#********************* MAIN ************************
print('start programm')
sensor_data = getSensorData()
disp.init()

c = 0
while True:
    #routine
    if(state==0):
        c += 1
        #show sensor data
        disp.printValue(sensor_data[show])      #show value on 7 segment display
        if (c > refresh_rate*50):
            sensor_data = getSensorData()       #refresh
            if indentation and show==1:         #indentation on or off
                show=0
            elif indentation and show==0:
                show=1
            disp.dot(show)                    #show temp or humidit
            c = 0

    #Menu
    if yellow.value() or not state==0:
        btc1 += 1
        if btc1 > 100:
            state==1
        
            #1 refresh rate ********************
            if state == 1:
                disp.menu('t',refresh_rate)
                if blue.value() and not block:
                    block = True
                    refresh_rate += 1
                elif(refresh_rate>9):
                    refresh_rate = 1

            #2 temp or humy ********************
            if state == 2:
                disp.menu('d',show)
                if blue.value() and not block:
                    block = True
                    show += 1
                elif(show>1):
                    show = 0
                disp.dot(show)

            #3 iteration temp humy **************
            if state == 3:
                disp.menu('i',indentation)
                if blue.value() and not block:
                    block = True
                    indentation += 1
                elif(indentation>1):
                    indentation = 0
           
            #4 return  **************************
            if state == 4:
                disp.menu('r',12)
                if blue.value():
                    btc1 = 0
                    block = False
                    disp.init()
                    disp.dot(0)
                    state=0

            #5 exit menu  ********************
            if state == 5:
                disp.menu('e',12)
                if blue.value():
                    btc2 += 1
                    if(btc2 > 100): 
                        disp.test()
                        break

            #Menu Handler ********************    
            if yellow.value() and not block:
                block = True
                state +=1
            elif state > 5:
                state = 1

            #4 rise trigger ********************
            if not blue.value() and not yellow.value() and block:
                block = False  
                disp.init()
                disp.dot(show)         
                btc1 = 0
                btc2 = 0