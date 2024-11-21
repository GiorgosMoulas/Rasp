import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the Reed switch and the buzzer module
reed_pin = 17  # Replace with the actual GPIO pin number for the Reed switch
buzzer_pin = 18  # Replace with the actual GPIO pin number for the buzzer module

# Initialize the GPIO pins
GPIO.setup(reed_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        if GPIO.input(reed_pin) == GPIO.HIGH:
            print("Reed switch is closed. Buzzer activated.")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
        else:
            print("Reed switch is open. Buzzer deactivated.")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer
        time.sleep(1)

except KeyboardInterrupt:
    pass

# Clean up GPIO on script exit
GPIO.cleanup()
