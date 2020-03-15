from machine import Pin

bit1 = Pin(25, Pin.OUT)
bit2 = Pin(33, Pin.OUT)
bit3 = Pin(15, Pin.OUT)
bit4 = Pin(21, Pin.OUT)
bit5 = Pin(14, Pin.OUT)
bit6 = Pin(32, Pin.OUT)
bit7 = Pin(27, Pin.OUT)
bit8 = Pin(12, Pin.OUT)
bit = [bit1, bit2, bit3, bit4, bit5, bit6, bit7, bit8]

#****************** funtions *****************

#test loop
def test():
    for i in range(8):
        print(bit[i].value())

#****************** rutine *******************

x = int(input("enter a value: "))
y = "{0:08b}".format(x)
length = int(len(y))-1

for i in range(8):
    bit[i].value(int(y[(length-i)])) #turn direction (lowest bit = LED 1)
