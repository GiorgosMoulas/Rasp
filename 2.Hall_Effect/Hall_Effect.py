
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the sensor's digital output (DO)
sensor_pin = 17  # Replace with the actual GPIO pin number

# Initialize the sensor pin as an input
GPIO.setup(sensor_pin, GPIO.IN)

try:
    while True:
        sensor_state = GPIO.input(sensor_pin)

        if sensor_state == GPIO.HIGH:
            print("No Magnetic Field !!!")
        else:
            print("A Magnetic Field detected !!!")

        time.sleep(0.1)  # Delay between readings

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
