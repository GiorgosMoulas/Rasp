
import RPi.GPIO as GPIO
import time

addCount = 8
addPins = [4, 17, 27, 22, 18, 23, 24, 25]  # Define the dip switch pins

GPIO.setmode(GPIO.BCM)

for add in range(addCount):
    GPIO.setup(addPins[add], GPIO.IN)

try:
    while True:
        dat = 0
        for i in range(8):
            dat <<= 1
            if not GPIO.input(addPins[i]):
                dat |= 0x01

        print("DEC:", dat)
        print("BIN:", bin(dat))
        time.sleep(0.5)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
