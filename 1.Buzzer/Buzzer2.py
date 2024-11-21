import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the buzzer and initialize them
buzzer_pin = 13
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    # Activate the buzzer for 1 second
    GPIO.output(buzzer_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(buzzer_pin, GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
