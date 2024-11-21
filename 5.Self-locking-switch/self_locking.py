import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pins
GPIO.setmode(GPIO.BCM)
pv_pin = 17
pd_pin = 18

# Setup GPIO pins
GPIO.setup(pv_pin, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(pd_pin, GPIO.IN,GPIO.PUD_DOWN)

try:
    while True:
        # Check the state of the self-locking switch
        pv_state = GPIO.input(pv_pin)
        pd_state = GPIO.input(pd_pin)

        if pv_state == GPIO.HIGH:
            print("Switch is not pressed (pv is HIGH)")
            # Your code for the action when the switch is pressed

        if pd_state == GPIO.HIGH:
            print("Switch is  pressed (pd is HIGH)")
            # Your code for the action when the switch is not pressed

        time.sleep(0.1)  # Add a small delay to avoid rapid state changes

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit

