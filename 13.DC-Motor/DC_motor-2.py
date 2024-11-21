

import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for DIR and SIG
dir_pin = 17  # Replace with the actual GPIO pin number for DIR
sig_pin = 18  # Replace with the actual GPIO pin number for SIG

# Initialize the GPIO pins
GPIO.setup(dir_pin, GPIO.OUT)
GPIO.setup(sig_pin, GPIO.OUT)

try:
    while True:
        user_input = input("Enter action (f: forward, b: backward, s: stop, q: quit): ").lower()

        if user_input == 'f':
            # Move motor forward
            GPIO.output(dir_pin, GPIO.HIGH)
            GPIO.output(sig_pin, GPIO.HIGH)
            time.sleep(10)
        elif user_input == 'b':
            # Move motor backward
            GPIO.output(dir_pin, GPIO.LOW)
            GPIO.output(sig_pin, GPIO.HIGH)
            time.sleep(10)
        elif user_input == 's':
            # Stop the motor
            GPIO.output(sig_pin, GPIO.LOW)
        elif user_input == 'q':
            break

except KeyboardInterrupt:
    pass

# Stop the motor
GPIO.output(sig_pin, GPIO.LOW)

# Clean up GPIO on script exit
GPIO.cleanup()
