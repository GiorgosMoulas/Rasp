import RPi.GPIO as GPIO
import time

# Set the GPIO mode and pins
GPIO.setmode(GPIO.BCM)
pv_pin = 17
pd_pin = 18
buzzer_pin = 22  # Change this to the GPIO pin connected to the buzzer signal (S)

# Setup GPIO pins
GPIO.setup(pv_pin, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(pd_pin, GPIO.IN,GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)

def activate_buzzer():
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(0.5)  # Buzzer on for 0.5 seconds
    GPIO.output(buzzer_pin, GPIO.LOW)

try:
    while True:
        # Check the state of the self-locking switch
        pv_state = GPIO.input(pv_pin)
        pd_state = GPIO.input(pd_pin)

        if pv_state == GPIO.HIGH:
            print("Switch is not pressed (pv is HIGH)")
            # Your code for the action when the switch is not pressed
            

        if pd_state == GPIO.HIGH:
            print("Switch is  pressed (pd is HIGH)")
            # Your code for the action when the switch is  pressed
            activate_buzzer()

        time.sleep(0.1)  # Add a small delay to avoid rapid state changes

except KeyboardInterrupt:
    print("Program terminated by user")
finally:
    GPIO.cleanup()  # Clean up GPIO on exit






