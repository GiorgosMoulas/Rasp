import RPi.GPIO as GPIO
import time

# Define GPIO pins for IN1, IN2, IN3, IN4 on the ULN2803
IN1 = 17
IN2 = 18
IN3 = 27
IN4 = 22

# Set up GPIO mode and pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Full Step Sequence
FULL_STEP_SEQUENCE = [
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 1, 1]
]

# Function to set the motor coils based on the step
def set_step(step_sequence):
    GPIO.output(IN1, step_sequence[0])
    GPIO.output(IN2, step_sequence[1])
    GPIO.output(IN3, step_sequence[2])
    GPIO.output(IN4, step_sequence[3])

# Main function to rotate the stepper motor
def rotate_stepper_motor(steps, delay):
    for _ in range(steps):
        for step_sequence in FULL_STEP_SEQUENCE:
            set_step(step_sequence)
            time.sleep(delay)

# Rotate the stepper motor 200 steps with a delay of 0.005 seconds between steps
rotate_stepper_motor(200, 0.005)

# Clean up GPIO on program exit
GPIO.cleanup()
