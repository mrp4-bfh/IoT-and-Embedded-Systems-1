from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
pir = Pin(15, Pin.IN)

# Semaphore Block
block = False

# Interrupt Handler 
def handle_interrupt(v):
    global block
    if not block:
        block = True
        led.value(0)
        print("INTERRUPT PERFORMED")
        sleep(3)

# Wait method with short sleep to avoid daemon threads
def wait(msec=1):
    global block
    for i in range(msec):
        sleep(0.1)
        if block:
            break

# Main loop
def rutine():
    global block
    while True:
        led.value(1)
        wait(5)
        led.value(0)
        wait(5)
        block = False

# call interrupt an main loop
pir.irq(trigger=pir.IRQ_RISING, handler=handle_interrupt)
rutine()
