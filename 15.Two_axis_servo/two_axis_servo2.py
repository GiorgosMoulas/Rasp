import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define GPIO pins for servo PWM control
pwm1_pin = 17  # Replace with the actual GPIO pin number for servo1
pwm2_pin = 18  # Replace with the actual GPIO pin number for servo2

# Define GPIO pins for tact switches
s0_pin = 22
s1_pin = 23
s2_pin = 24
s3_pin = 25
s4_pin = 26

# Initialize GPIO pins
GPIO.setup(pwm1_pin, GPIO.OUT)
GPIO.setup(pwm2_pin, GPIO.OUT)
GPIO.setup(s0_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s1_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s2_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s3_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(s4_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Create PWM instances for servo control
pwm1 = GPIO.PWM(pwm1_pin, 50)  # 50Hz frequency
pwm2 = GPIO.PWM(pwm2_pin, 50)

# Define servo positions (adjust duty cycles as needed)
initial_position = 7.5
servo1_position = initial_position
servo2_position = initial_position

# Start the PWM signals
pwm1.start(servo1_position)
pwm2.start(servo2_position)

def reset_servos():
    global servo1_position, servo2_position
    servo1_position = initial_position
    servo2_position = initial_position
    pwm1.ChangeDutyCycle(servo1_position)
    pwm2.ChangeDutyCycle(servo2_position)

try:
    while True:
        if not GPIO.input(s0_pin):
            servo2_position = initial_position + 2.5  # Clockwise 50%
            pwm2.ChangeDutyCycle(servo2_position)
        if not GPIO.input(s4_pin):
            servo2_position = initial_position - 2.5  # Anti-clockwise 50%
            pwm2.ChangeDutyCycle(servo2_position)
        if not GPIO.input(s3_pin):
            servo1_position = initial_position + 2.5  # Clockwise 50%
            pwm1.ChangeDutyCycle(servo1_position)
        if not GPIO.input(s1_pin):
            servo1_position = initial_position - 2.5  # Anti-clockwise 50%
            pwm1.ChangeDutyCycle(servo1_position)
        if not GPIO.input(s2_pin):
            reset_servos()

except KeyboardInterrupt:
    pass

# Clean up GPIO on script exit
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
