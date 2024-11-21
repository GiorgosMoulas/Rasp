import smbus
import time

address = 0x48  # Default address of PCF8591
bus = smbus.SMBus(1)  # Create an instance of smbus

cmd = 0x40  # Command

def analogRead(chn):  # Read ADC value, chn: 0, 1, 2, 3
    value = bus.read_byte_data(address, cmd + chn)
    return value

def analogWrite(value):  # Write DAC value
    bus.write_byte_data(address, cmd, value)

def loop():
    while True:
        value1 = analogRead(0)  # Read the ADC value of channel 0
        value2 = analogRead(1)  # Read the ADC value of channel 1

        voltage1 = value1 / 255.0 * 3.3  # Calculate the voltage value for channel 0
        voltage2 = value2 / 255.0 * 3.3  # Calculate the voltage value for channel 1

        print(f'ADC Value (Channel 0): {value1}, Voltage: {voltage1:.2f}V')
        print(f'ADC Value (Channel 1): {value2}, Voltage: {voltage2:.2f}V')

        time.sleep(0.01)

def destroy():
    bus.close()

if __name__ == '__main__':
    print('Program is starting ... ')

    try:
        loop()
    except KeyboardInterrupt:
        destroy()
