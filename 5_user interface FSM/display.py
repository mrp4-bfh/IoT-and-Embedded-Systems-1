__author__      = "Patrik Marti"
__copyright__   = "Copyright 2020, Berner Fachhochschule BFH, IoT anb Embedded Systems"
__license__     = "GPL"
__version__     = "0.1"
__maintainer__  = "Patrik Marti"
__email__       = "patrik.marti@bfh.ch"
__status__      = "testing"

from machine import Pin
from time import sleep, sleep_ms

# Multiplex toggle
class display:
    """
    This module controls a 7 segment display, type LN5101BS  with two digits in total.
    The printValue() and menu() functions must be called in 10 milliseconds intervals, otherwise the display flickers. 
    The point in the display cannot be controlled individually.
    """
    def __init__(self, Pdig1, Pdig2, PsegA, PsegB, PsegC, PsegD, PsegE, PsegF, PsegG, PsegDot):
        #Digit Vin In
        self.digit1 = Pin(Pdig1, Pin.OUT, 0)
        self.digit2 = Pin(Pdig2, Pin.OUT, 1)

        #Segment Gnd
        self.segA = Pin(PsegA, Pin.OPEN_DRAIN, 1)
        self.segB = Pin(PsegB, Pin.OPEN_DRAIN, 1)
        self.segC = Pin(PsegC, Pin.OPEN_DRAIN, 1)
        self.segD = Pin(PsegD, Pin.OPEN_DRAIN, 1)
        self.segE = Pin(PsegE, Pin.OPEN_DRAIN, 1)
        self.segF = Pin(PsegF, Pin.OPEN_DRAIN, 1)
        self.segG = Pin(PsegG, Pin.OPEN_DRAIN, 1)
        self.Dot  = Pin(PsegDot, Pin.OPEN_DRAIN, 1)

        #Update rate digit t(ms)
        self.delay = 12

    #Toggle Digit
    def toggle(self):
        """
        Toggle digit a to b or b to c
        """
        self.digit1.value(not self.digit1.value())
        self.digit2.value(not self.digit1.value())

    def init(self):
        """
        Init digit order
        """
        self.digit1.value(1)
        self.digit2.value(0)        

    def number(self, i):
        """
        Set a number
        """
        self.segA.value(1)
        self.segB.value(1)
        self.segC.value(1)
        self.segD.value(1)
        self.segE.value(1)
        self.segF.value(1)
        self.segG.value(1)
        if(i == 1):
            self.segB.value(0)
            self.segC.value(0)
        elif(i == 2):
            self.segA.value(0)
            self.segB.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segG.value(0)
        elif(i == 3):
            self.segA.value(0)
            self.segB.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segG.value(0)
        elif(i == 4):
            self.segB.value(0)
            self.segC.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(i == 5):
            self.segA.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(i == 6):
            self.segA.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(i == 7):
            self.segA.value(0)
            self.segB.value(0)
            self.segC.value(0)
        elif(i == 8):
            self.segA.value(0)
            self.segB.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(i == 9):
            self.segA.value(0)
            self.segB.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(i == 0):
            self.segA.value(0)
            self.segB.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segF.value(0)

    def char(self, c):
        """
        Set char
        """
        self.segA.value(1)
        self.segB.value(1)
        self.segC.value(1)
        self.segD.value(1)
        self.segE.value(1)
        self.segF.value(1)
        self.segG.value(1)
        if(c == 'r'):
            self.segE.value(0)
            self.segG.value(0)
        elif(c == 'c'):
            self.segA.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segF.value(0)
        elif(c == 'd'):
            self.segB.value(0)
            self.segC.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segG.value(0)
        elif(c == 'e'):
            self.segA.value(0)
            self.segD.value(0)
            self.segE.value(0)
            self.segF.value(0)
            self.segG.value(0)
        elif(c == 'i'):
            self.segC.value(0)
        elif(c == 't'):
            self.segB.value(0)
            self.segC.value(0)
            self.segG.value(0)
    
    def dot(self, s):
        """
        Enable dot with 1 or disable with 0
        """
        if(s == 1):
            self.Dot.value(0)
        else:
            self.Dot.value(1)
    
    #Print Value
    def printValue(self, v=12):
        """
        Display a Value from 0 to 99
        """
        self.number(v//10)
        sleep_ms(self.delay)
        self.toggle()
        self.number(v%10)
        sleep_ms(self.delay)
        self.toggle()

    #Menu
    def menu(self, m='t', c=0):
        """
        Chose a char for the first digit (r, c, d, e, i, t) and a 
        Chose an index number for the second digit (0..9)
        """
        self.char(m)
        sleep_ms(self.delay)
        self.toggle()
        self.number(c)
        sleep_ms(self.delay)
        self.toggle()
   
    #Test Loop
    """
    Segment test, shows each segment from a to g
    """
    def test(self):
        self.digit1.value(1)
        self.digit2.value(1)
        self.segA.value(0)
        sleep(0.2)
        self.segA.value(1)
        self.segB.value(0)
        sleep(0.2)
        self.segB.value(1)
        self.segC.value(0)
        sleep(0.2)
        self.segC.value(1)
        self.segD.value(0)
        sleep(0.2)
        self.segD.value(1)
        self.segE.value(0)
        sleep(0.2)
        self.segE.value(1)
        self.segF.value(0)
        sleep(0.2)
        self.segF.value(1)
        self.segG.value(0)
        sleep(0.2)
        self.segG.value(1)
        self.digit1.value(0)
        self.digit2.value(0)