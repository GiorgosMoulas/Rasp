
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the PIR sensor's output
pir_sensor_pin = 17  # Replace with the actual GPIO pin number

# Initialize the sensor pin as an input
GPIO.setup(pir_sensor_pin, GPIO.IN)

try:
    while True:
        sensor_state = GPIO.input(pir_sensor_pin)

        if sensor_state == GPIO.HIGH:
            print("Motion detected")
        else:
            print("No motion")

        time.sleep(0.1)  # Delay between readings

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
