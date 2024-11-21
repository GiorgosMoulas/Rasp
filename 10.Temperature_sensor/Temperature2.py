import smbus
import time

# Define the I2C bus and address
bus = smbus.SMBus(1)  # Use bus number 1 for Raspberry Pi 3 and later
pcf8591_address = 0x48  # PCF8591 default I2C address

# Function to read ADC channel
def read_adc(channel):
    # PCF8591 has 4 analog input channels (Ain0 to Ain3)
    command = 0x40 | (channel & 0x03)
    bus.write_byte(pcf8591_address, command)
    time.sleep(0.01)  # Allow some time for the conversion to complete
    adc_value = bus.read_byte(pcf8591_address)
    return adc_value

# Define the ADC channel for the LM35 temperature sensor
lm35_channel = 0

try:
    while True:
        # Read analog value from the LM35 temperature sensor
        analog_value = read_adc(lm35_channel)

        # Calculate the temperature in degrees Celsius
        temperature = (analog_value ) / 10.24

        # Print the temperature to the console
        print(f"Temperature: {temperature:.2f} degrees Celsius")

        # Sleep for a short time to avoid printing too quickly
        time.sleep(0.1)

except KeyboardInterrupt:
    # Clean up on Ctrl+C
    pass

finally:
    # Clean up on normal program exit
    print("Cleaning up...")
    bus.close()

