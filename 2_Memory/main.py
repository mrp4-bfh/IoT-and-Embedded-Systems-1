import boot
import os
from time import sleep

#*************** functions *******************

# Write file
def writeFile(value):
    f=open("myfile.txt","w")
    f.write(str(value))
    f.close()

# Read File
def readFile():
    f=open("myfile.txt","r")
    myfile = f.read()
    f.close()
    return myfile

#*************** main loop *******************

# Restore cycle
i = int(readFile())

while i < 20:
    i += 1
    sleep(1)
    writeFile(i)
    print(i)

if i >= 20:
    writeFile(0)
    print("Done!!!!!!")