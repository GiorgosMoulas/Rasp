
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the PIR sensor's output
pir_sensor_pin = 17  # Replace with the actual GPIO pin number

# Define the GPIO pin for the buzzer module's signal input
buzzer_pin = 18  # Replace with the actual GPIO pin number

# Initialize the sensor pin as an input
GPIO.setup(pir_sensor_pin, GPIO.IN)

# Initialize the buzzer pin as an output
GPIO.setup(buzzer_pin, GPIO.OUT)
GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer initially

try:
    while True:
        sensor_state = GPIO.input(pir_sensor_pin)

        if sensor_state == GPIO.HIGH:
            print("Motion detected")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Turn on the buzzer
        else:
            print("No motion")
            GPIO.output(buzzer_pin, GPIO.LOW)  # Turn off the buzzer

        time.sleep(0.1)  # Delay between readings

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
