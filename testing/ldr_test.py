from machine import ADC
import time
adc = ADC(28) 
while 1:
    time.sleep(0.3)     
    print(adc.read_u16())

