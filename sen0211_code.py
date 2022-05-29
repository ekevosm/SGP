#from machine import Pin
import machine
from time import sleep
from util.octopus import disp7_init



def readACCurrentValue():
    
    ACTectionRange = 20
    VREF = 3.3
    ACCurrtntValue = 0
    peakVoltage = 0 
    voltageVirtualValue = 0
    for i in range(5):
        peakVoltage += sen0211.read()
        sleep(1)
  
    peakVoltage = peakVoltage / 5
    print('peak', peakVoltage)
    voltageVirtualValue = peakVoltage * 0.707   

    voltageVirtualValue = (voltageVirtualValue / 1024 * VREF ) / 2  

    ACCurrtntValue = voltageVirtualValue * ACTectionRange

    return ACCurrtntValue


led = machine.Pin(2, machine.Pin.OUT)
disp7 = disp7_init()
sen0211= machine.ADC(machine.Pin(39))
sen0211.atten(machine.ADC.ATTN_11DB)


while True:
    sen0211_value= sen0211.read()  #readACCurrentValue()
    print(sen0211_value)
    disp7.show(sen0211_value)
    sleep(1)
