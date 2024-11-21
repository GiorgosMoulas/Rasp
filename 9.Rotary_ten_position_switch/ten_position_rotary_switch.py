import RPi.GPIO as GPIO

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pins for the switch and initialize them
switch_common_pin = 17
output_pins = [18, 19, 20, 21]

GPIO.setup(switch_common_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

for pin in output_pins:
    GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# Function to calculate the position
def calculate_position():
    position = 0
    for i, pin in enumerate(output_pins):
        if GPIO.input(pin) == GPIO.LOW:
            position += 2 ** i
    return position

try:
    while True:
        position = calculate_position()
        print(f"Switch is in position {position}")
        GPIO.wait_for_edge(switch_common_pin, GPIO.BOTH)
except KeyboardInterrupt:
    GPIO.cleanup()  # Clean up GPIO on Ctrl+C

finally:
    GPIO.cleanup()  # Clean up GPIO on script exit

