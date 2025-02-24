import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
dac = [8, 11, 7, 1, 0, 5, 12, 6 ]
GPIO.setup(dac, GPIO.OUT)

def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]

try:
    flag = True
    while(True):
        value = input()
        if(value == 'q'):
            break
        elif(not isinstance(value, str)):
            print("not a number")
            break

        elif(int(value) < 0):
            print("a negative number")
            break
        elif(int(value) > 255):
            print("number out of range")
            break

        else:
            value = int(value)
            GPIO.output(dac, decimal2binary(value))
            print(3.3*value/256, "V")
    







finally:
    GPIO.output(dac, 0)
