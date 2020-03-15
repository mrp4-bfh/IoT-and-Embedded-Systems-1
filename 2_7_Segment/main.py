from machine import Pin
from time import sleep, sleep_ms

digit1 = Pin(26, Pin.OUT)
digit2 = Pin(25, Pin.OUT)

segA = Pin(33, Pin.OPEN_DRAIN, 1)
segB = Pin(15, Pin.OPEN_DRAIN, 1)
segC = Pin(21, Pin.OPEN_DRAIN, 1)
segD = Pin(14, Pin.OPEN_DRAIN, 1)
segE = Pin(32, Pin.OPEN_DRAIN, 1)
segF = Pin(27, Pin.OPEN_DRAIN, 1)
segG = Pin(12, Pin.OPEN_DRAIN, 1)

#*************** 7 segment *******************

# Multiplex toggle
def toggle():
    digit1.value(not digit1.value())
    digit2.value(not digit1.value())

# Set 1
def number(i):
    if(i == 1):
        segA.value(1)
        segB.value(0)
        segC.value(0)
        segD.value(1)
        segE.value(1)
        segF.value(1)
        segG.value(1)
    elif(i == 2):
        segA.value(0)
        segB.value(0)
        segC.value(1)
        segD.value(0)
        segE.value(0)
        segF.value(1)
        segG.value(0)
    elif(i == 3):
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(0)
        segE.value(1)
        segF.value(1)
        segG.value(0)
    elif(i == 4):
        segA.value(1)
        segB.value(0)
        segC.value(0)
        segD.value(1)
        segE.value(1)
        segF.value(0)
        segG.value(0)
    elif(i == 5):
        segA.value(0)
        segB.value(1)
        segC.value(0)
        segD.value(0)
        segE.value(1)
        segF.value(0)
        segG.value(0)
    elif(i == 6):
        segA.value(0)
        segB.value(1)
        segC.value(0)
        segD.value(0)
        segE.value(0)
        segF.value(0)
        segG.value(0)
    elif(i == 7):
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(1)
        segE.value(1)
        segF.value(1)
        segG.value(1)
    elif(i == 8):
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(0)
        segE.value(0)
        segF.value(0)
        segG.value(0)
    elif(i == 9):
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(0)
        segE.value(1)
        segF.value(0)
        segG.value(0)
    elif(i == 0):
        segA.value(0)
        segB.value(0)
        segC.value(0)
        segD.value(0)
        segE.value(0)
        segF.value(0)
        segG.value(1)

#Test Loop
def test():
    digit1.value(1)
    digit2.value(1)
    segA.value(0)
    sleep(0.2)
    segA.value(1)
    segB.value(0)
    sleep(0.2)
    segB.value(1)
    segC.value(0)
    sleep(0.2)
    segC.value(1)
    segD.value(0)
    sleep(0.2)
    segD.value(1)
    segE.value(0)
    sleep(0.2)
    segE.value(1)
    segF.value(0)
    sleep(0.2)
    segF.value(1)
    segG.value(0)
    sleep(0.2)
    segG.value(1)
    digit1.value(0)
    digit2.value(0)

def TestLoop():
    for i in range(100000):
        digit2.value(not digit1.value())


#********************* MAIN **************************

runtime = 25 # sec
hp = 1 #ms

digit1.value(0)
digit2.value(1)
c = (runtime*1000)//(hp*2)

num = 0

while c > 0:
    c -= 1
    number(num//10)
    toggle()
    sleep_ms(hp)
    number(num%10)
    toggle()
    sleep_ms(hp)
    if(c %(1000//(2*hp)) == 0):
        num += 1

#RESET Display
test()