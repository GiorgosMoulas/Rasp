
import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the Hall Effect sensor's digital output (DO)
hall_sensor_pin = 17

# Define the GPIO pin for the active buzzer's signal input (S)
buzzer_pin = 18

# Initialize the sensor pin as an input
GPIO.setup(hall_sensor_pin, GPIO.IN)

# Initialize the buzzer pin as an output
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    while True:
        sensor_state = GPIO.input(hall_sensor_pin)

        if sensor_state == GPIO.HIGH:
            print("Closed window  !!")
            # Activate the buzzer when a magnetic field is detected
            GPIO.output(buzzer_pin, GPIO.HIGH)
        else:
            print("Open window  !!")
            # Deactivate the buzzer when no magnetic field is detected
            GPIO.output(buzzer_pin, GPIO.LOW)

        time.sleep(0.1)  # Delay between readings

except KeyboardInterrupt:
    pass

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
