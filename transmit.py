from machine import Pin
import time

laser = Pin(16,Pin.OUT)
period = 0.05

print("pointing...")

while 1:
    laser.value(1)
    inpdata = input("<--")
    for i in inpdata:
        x = bin(ord(i))[2:]
        if len(x) < 8:
            x = ((8 - len(x)) * "0") + x
        for i in x:
            if i == "1":
                laser.value(1)
            else:
                laser.value(0)
            time.sleep(period)
    bsn = "00001010"
    for i in bsn:
        if i == "1":
            laser.value(1)
        else:
            laser.value(0)
        time.sleep(period)
