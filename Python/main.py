from machine import Pin

led1 = Pin(2, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(15, Pin.OUT)
led4 = Pin(16, Pin.OUT)
leds = [led1, led2, led3, led4] 

x = int(input("enter a value: "))
y = "{0:b}".format(x)
length = int(len(y)) - 1

for i in range(4):
    if(i < int(length)):
        leds[i].value(int(y[(length-i)]))
    else:
        leds[i].value(0)