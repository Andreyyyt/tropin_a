import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc():
    for value in range(256):
        GPIO.output(dac,decimal2binary(value))
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            return value
    return value


try:
    while(True):
        value = adc()
        voltage = value*3.3/256
        print(value, voltage)
        time.sleep(0.01)



finally:
    GPIO.output(dac, 0)