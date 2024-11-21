
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

# Function to move the motor forward
def move_forward():
    GPIO.output(dir_pin, GPIO.HIGH)
    GPIO.output(sig_pin, GPIO.HIGH)

# Function to move the motor backward
def move_backward():
    GPIO.output(dir_pin, GPIO.LOW)
    GPIO.output(sig_pin, GPIO.HIGH)

# Function to stop the motor
def stop_motor():
    GPIO.output(sig_pin, GPIO.LOW)

try:
    while True:
        user_input = input("Enter action (f: forward, b: backward, s: stop, q: quit): ").lower()
        
        if user_input == 'f':
            move_forward()
            time.sleep(10)  # Move forward for 10 seconds
        elif user_input == 'b':
            move_backward()
            time.sleep(10)  # Move backward for 10 seconds
        elif user_input == 's':
            stop_motor()
        elif user_input == 'q':
            break

except KeyboardInterrupt:
    pass

# Stop the motor
stop_motor()

# Clean up GPIO on script exit
GPIO.cleanup()

