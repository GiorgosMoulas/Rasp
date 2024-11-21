import RPi.GPIO as GPIO
import time

# Define GPIO pins for toggle switches
S0_PIN = 17
S1_PIN = 12
S2_PIN = 27
S3_PIN = 22
S4_PIN = 23
S5_PIN = 24

# Set the GPIO mode and setup the pins as inputs
GPIO.setmode(GPIO.BCM)
GPIO.setup([S0_PIN, S1_PIN, S2_PIN, S3_PIN, S4_PIN, S5_PIN], GPIO.IN,GPIO.PUD_DOWN)

try:
    while True:
        # Read the state of each toggle switch
        state_s0 = GPIO.input(S0_PIN)
        state_s1 = GPIO.input(S1_PIN)
        state_s2 = GPIO.input(S2_PIN)
        state_s3 = GPIO.input(S3_PIN)
        state_s4 = GPIO.input(S4_PIN)
        state_s5 = GPIO.input(S5_PIN)

        # Print the state of each toggle switch
        print(f"S0-S1: {state_s0}-{state_s1}, S2-S3: {state_s2}-{state_s3}, S4-S5: {state_s4}-{state_s5}")

        # Add your code here to perform actions based on the switch states
        # For example, you can check each switch's state and take appropriate actions

        # Wait for a short duration to avoid continuous printing
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Exiting program")
finally:
    # Cleanup GPIO settings on program exit
    GPIO.cleanup()

