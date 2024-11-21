import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the Reed switch
reed_pin = 17  # Replace with the actual GPIO pin number

# Initialize the GPIO pin
GPIO.setup(reed_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(reed_pin) == GPIO.HIGH:
            print("Reed switch is closed .")
        else:
            print("Reed switch is open .")
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO on script exit
GPIO.cleanup()
