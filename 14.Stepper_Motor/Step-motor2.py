

import RPi.GPIO as GPIO
import time

STEPPER_PIN1 = 6
STEPPER_PIN2 = 13
STEPPER_PIN3 = 19
STEPPER_PIN4 = 26

STEPS_PER_ROTOR_REV = 32
GEAR_REDUCTION = 64
STEPS_PER_OUT_REV = STEPS_PER_ROTOR_REV * GEAR_REDUCTION

StepsRequired = 0

GPIO.setmode(GPIO.BCM)
GPIO.setup(STEPPER_PIN1, GPIO.OUT)
GPIO.setup(STEPPER_PIN2, GPIO.OUT)
GPIO.setup(STEPPER_PIN3, GPIO.OUT)
GPIO.setup(STEPPER_PIN4, GPIO.OUT)

def set_step(w1, w2, w3, w4):
    GPIO.output(STEPPER_PIN1, w1)
    GPIO.output(STEPPER_PIN2, w2)
    GPIO.output(STEPPER_PIN3, w3)
    GPIO.output(STEPPER_PIN4, w4)

def forward(delay, steps):
    for _ in range(steps):
        set_step(1, 0, 0, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 0)
        time.sleep(delay)
        set_step(0, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 0, 0, 1)
        time.sleep(delay)

def backward(delay, steps):
    for _ in range(steps):
        set_step(0, 0, 0, 1)
        time.sleep(delay)
        set_step(0, 0, 1, 0)
        time.sleep(delay)
        set_step(0, 1, 0, 0)
        time.sleep(delay)
        set_step(1, 0, 0, 0)
        time.sleep(delay)

try:
    while True:
        # rotate very slowly for 4 steps to observe the change of LED light on the module
        StepsRequired = 4
        forward(0.01, StepsRequired)
        time.sleep(1)

        # clockwise rotation slowly
        StepsRequired = STEPS_PER_OUT_REV
        forward(0.01, StepsRequired)
        time.sleep(1)

        # counterclockwise rotation quickly
        StepsRequired = STEPS_PER_OUT_REV
        backward(0.01, StepsRequired)
        time.sleep(1)

except KeyboardInterrupt:
    pass

GPIO.cleanup()
