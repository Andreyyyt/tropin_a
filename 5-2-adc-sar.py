import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
def binary2decimal(ar):
    ans = 0
    pw = 128
    for i in range(8):
        ans += ar[i]*pw
        pw //= 2
    return ans

dac = [8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp = 14
troyka = 13
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def adc_sar():
    ar = [0]*8
    for i in range(8):
        ar[i] = 1
        GPIO.output(dac,ar)
        time.sleep(0.001)
        if GPIO.input(comp) == 1:
            ar[i] = 0
    return ar

           
    


try:
    while(True):
        ar = adc_sar()
        value = binary2decimal(ar)
        n = (value+1)//32
        led_bin = [0]*8
        for i in range(n):
            led_bin[7-i] = 1
        
        voltage = value*3.3/256
        print(n, voltage)
        GPIO.output(leds, led_bin)
        time.sleep(0.01)



finally:
    GPIO.output(dac, 0)