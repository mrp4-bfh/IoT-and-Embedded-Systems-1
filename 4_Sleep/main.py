#Task 4.2 Wake up!

import esp32
from machine import Pin, deepsleep, DEEPSLEEP_RESET, reset_cause
from time import sleep

led=Pin(13, Pin.OUT)
button = Pin(14, Pin.IN)

#Note: with this wake up source, you can only use pins that are RTC GPIOs
#take a look at our ESP32 GPIO reference guide. 
#level parameter can be: esp32.WAKEUP_ANY_HIGH or esp32.WAKEUP_ALL_LOW
esp32.wake_on_ext0(pin = button, level = esp32.WAKEUP_ANY_HIGH)

# check if the device woke from a deep sleep
if reset_cause() == DEEPSLEEP_RESET:
    print('woke from a deep sleep')

print('start work')
led.value(1)
sleep(5)
print('Going to sleep')
led.value(0)
#put the device to deepsleep
deepsleep()
