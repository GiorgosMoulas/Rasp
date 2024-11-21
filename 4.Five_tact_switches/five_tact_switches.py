import RPi.GPIO as GPIO
import time

# Define GPIO pins
S0 = 17
S1 = 27
S2 = 22
S3 = 5
S4 = 6

# Set GPIO mode and setup
GPIO.setmode(GPIO.BCM)
GPIO.setup([S0, S1, S2, S3, S4], GPIO.IN, pull_up_down=GPIO.PUD_UP)

try:
    while True:
        state_s0 = GPIO.input(S0)
        state_s1 = GPIO.input(S1)
        state_s2 = GPIO.input(S2)
        state_s3 = GPIO.input(S3)
        state_s4 = GPIO.input(S4)

        print(f"S0: {state_s0}, S1: {state_s1}, S2: {state_s2}, S3: {state_s3}, S4: {state_s4}")
        time.sleep(0.1)

except KeyboardInterrupt:
    GPIO.cleanup()
    print("Script terminated by user.")
