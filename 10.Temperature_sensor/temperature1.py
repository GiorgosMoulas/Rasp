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

# Define the ADC channel for the temperature sensor
temperature_channel = 0

# Function to convert ADC value to temperature (replace with your specific conversion formula)
def convert_to_temperature(adc_value):
    # Replace this with your actual conversion formula
    temperature = adc_value /10.0
    return temperature

try:
    while True:
        # Read analog value from the temperature sensor
        analog_value = read_adc(temperature_channel)

        # Convert ADC value to temperature
        temperature = convert_to_temperature(analog_value)

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
