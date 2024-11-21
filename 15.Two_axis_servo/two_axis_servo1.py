import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for PWM1 and PWM2
pwm1_pin = 17  # Replace with the actual GPIO pin number for PWM1
pwm2_pin = 18  # Replace with the actual GPIO pin number for PWM2

# Initialize the GPIO pins
GPIO.setup(pwm1_pin, GPIO.OUT)
GPIO.setup(pwm2_pin, GPIO.OUT)

# Create PWM instances for both servos
pwm1 = GPIO.PWM(pwm1_pin, 50)  # 50Hz frequency
pwm2 = GPIO.PWM(pwm2_pin, 50)

# Start the PWM signals
pwm1.start(7.5)  # Adjust the duty cycle for servo position
pwm2.start(7.5)

try:
    while True:
        # Move the servos to predefined positions
        pwm1.ChangeDutyCycle(12.5)  # Adjust these values as needed
        pwm2.ChangeDutyCycle(2.5)
        time.sleep(2)
        
        pwm1.ChangeDutyCycle(2.5)
        pwm2.ChangeDutyCycle(12.5)
        time.sleep(2)

except KeyboardInterrupt:
    pass

# Clean up GPIO on script exit
pwm1.stop()
pwm2.stop()
GPIO.cleanup()
