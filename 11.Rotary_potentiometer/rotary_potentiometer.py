#Terminal prints the analog value read by adjustable potentiometer. The LEd brightness will vary with the the rotary of potentiometer

import smbus
import time
address = 0x48 #default address of PCF8591
bus=smbus.SMBus(1) #Create an instance of smbus

cmd=0x40 #command
# A0 = 0x40 ##A0 ----> port address
# A1 = 0x41
# A2 = 0x42
# A3 = 0x43
def analogRead(chn): #read ADC value,chn:0,1,2,3
    value = bus.read_byte_data(address,cmd+chn)
    return value

def analogWrite(value):#write DAC value
    bus.write_byte_data(address,cmd,value)


def loop():
   while True:
        value = analogRead(0) #read the ADC value ofchannel 0
        analogWrite(value) #write the DAC value
        voltage = value / 255.0 * 3.3 #calculate the voltage value
        print ('ADC Value : %d, Voltage : %.2f'%(value,voltage))
        time.sleep(0.01)

def destroy():
    bus.close()


if __name__ == '__main__':
    print ('Program is starting ... ')

    try:
        loop()
    except KeyboardInterrupt:
        destroy()


#Smbus is based on iic communication. We treat it as iic communication library.

#     bus.read_byte_data(address,cmd+chn)      ---->>>>> Read the corresponding modules with iic address，
# address is the address of pcf8591 module，cmd+chn correspond to the address 
# of analog port pcf8591: A0 = 0x40，A1 = 0x41，A2 = 0x42，A3 = 0x43


#    bus.write_byte_data(address,cmd,value)    ------->>>>>    D/A analog value outputs, address is address of pcf8591 module，
#      cmd outputs the address of pins，value: output value

#  Smbus library file ------>>>>    https://pypi.org/project/smbus2/0.1.2/

