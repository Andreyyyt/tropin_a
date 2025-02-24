import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6 ]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
try:
    t = float(input())/256
    level = 0
    flag = True
    while(True):
        GPIO.output(dac, decimal2binary(level))
        time.sleep(t)
        if(flag):
            level += 1
        if(not flag):
            level -= 1
        if(level == 250):
            flag = False
            level -= 1
        if(level == 2):
            flag = True
            level += 1
            
            




finally:
    GPIO.output(dac, 0)
