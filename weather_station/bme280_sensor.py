import bme280
import smbus2

port = 1 #port on smbus
address = 0x76 # address for bme sensor
bus = smbus2.SMBus(port) #make a bus to go to sensor

bme280.load_calibration_params(bus,address)

def read_all():
    bme_data = bme280.sample(bus, address)
    return bme_data.temperature, bme_data.pressure, bme_data.humidity
    
