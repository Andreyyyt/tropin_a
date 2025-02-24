import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setup(24, GPIO.OUT)
p = GPIO.PWM(24, 50)
p.start(0)
try:
    while(True):
        dtc = int(input())
        p.ChangeDutyCycle(dtc)
        print(dtc*3.3/100)
    
finally:
    p.stop()
    GPIO.cleanup()