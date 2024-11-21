import RPi.GPIO as GPIO
import time

buzzPin = 13  # Define the buzzer pin

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(buzzPin, GPIO.OUT)  # Set the buzzer pin as an output
    print("Buzzer pin setup complete")

def loop():
    try:
        while True:
            GPIO.output(buzzPin, GPIO.HIGH)  # Output high level signal
            time.sleep(1)  # Delay for 1 second
            GPIO.output(buzzPin, GPIO.LOW)  # Output low level signal
            time.sleep(1)  # Delay for 1 second
    except KeyboardInterrupt:
        GPIO.cleanup()  # Clean up GPIO on Ctrl+C exit

if __name__ == '__main__':
    setup()
    loop()
