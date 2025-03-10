import matplotlib.pyplot as plt
import RPi.GPIO as gpio
import sys
import time

gpio.setmode(gpio.BCM)
dac=[8, 11, 7, 1, 0, 5, 12, 6]
leds = [2, 3, 4, 17, 27, 22, 10, 9]
comp=14
troyka=13
gpio.setup(dac, gpio.OUT)
gpio.setup(troyka,gpio.OUT, initial=gpio.HIGH)
gpio.setup(comp, gpio.IN)


def decimal2binary(a):
    return [int(elem) for elem in bin(a)[2:].zfill(8)]
    
def binary2decimal(ar):
    ans = 0
    pw = 128
    for i in range(8):
        ans += ar[i]*pw
        pw //= 2
    return ans

def adc_sar():
    ar = [0]*8
    for i in range(8):
        ar[i] = 1
        gpio.output(dac,ar)
        time.sleep(0.01)
        if gpio.input(comp) == 1:
            ar[i] = 0
    return ar

measured_data = []

try:
    time_start = time.time()
    datas = 0
    gpio.output(troyka, 1)
    while(datas < 200):
        datas = binary2decimal(adc_sar())
        measured_data.append(datas)
    gpio.output(troyka, 0)
    while(datas > 100):
        datas = binary2decimal(adc_sar())
        measured_data.append(datas)      

    time_end = time.time()
     
    measured_data_str = [str(item) for item in measured_data]
    print(measured_data_str)
    with open('data.txt', 'w') as outfile:
        outfile.write("\n".join(measured_data_str))
    with open('settings.txt', 'w') as outfile_1:
        outfile_1.write(" ".join(["step quanting: ",str(3.3/256), "frequency:", str(12.5)]))


    print(time_end - time_start, 0.08, 12.5, 3.3/256)  
    plt.plot(measured_data)
    plt.show()

finally:
    gpio.cleanup()

#plt.plot(measured_data)
#plt.show()