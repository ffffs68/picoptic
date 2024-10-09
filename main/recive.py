import machine
import time

adc = machine.ADC(28)
period = 0.05

print("looking...")

while 1:
    while adc.read_u16() > 18000:
        time.sleep(0.01)
    time.sleep((period//2)*3)
    luggage = ""
    for i in range(8):
        if adc.read_u16() > 18000:
            luggage += "1"
        else:
            luggage += "0"
        time.sleep(period)
    if luggage == "00001010":
        print("")
    else:
        print(chr(int(luggage,2)),end="")
