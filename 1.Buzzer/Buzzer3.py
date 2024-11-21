import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin for the buzzer and initialize it
buzzer_pin = 13
GPIO.setup(buzzer_pin, GPIO.OUT)

# Define a simple melody
melody = [261.63, 293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]

# Function to play a note
def play_note(frequency, duration):
    if frequency == 0:
        time.sleep(duration)
    else:
        period = 1.0 / frequency
        half_period = period / 2
        cycles = int(duration * frequency)
        for _ in range(cycles):
            GPIO.output(buzzer_pin, GPIO.HIGH)
            time.sleep(half_period)
            GPIO.output(buzzer_pin, GPIO.LOW)
            time.sleep(half_period)

try:
    for note in melody:
        play_note(note, 0.5)  # Play each note for 0.5 seconds

except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit
