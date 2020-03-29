from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)
pir = Pin(18, Pin.IN)

# Semaphore Block
block = False
# Run Signal
run = False

# Interrupt Handler 
def handle_interrupt(v):
    global block
    global run
    if not block:
        block = True
        run = not run
        led.value(0)
        print("INTERRUPT PERFORMED")

# Main loop
def rutime():
    global block
    global run
    while True:
        led.value(run)
        sleep(1)
        led.value(0)
        sleep(1)
        block = False

# call interrupt an main loop
pir.irq(trigger=pir.IRQ_RISING, handler=handle_interrupt)
rutime()
