import bme280_sensor
import database

db = database.weather_database()
air_temperature, air_pressure, humidity = bme280_sensor.read_all()
while True:
    temp, pressure, humid = bme280_sensor.read_all()
    
    while temp >= air_temperature+0.5 or temp <= air_temperature-0.5:
        air_temperature = temp
        print('Temperature: {}C Pressure: {}atm Humidity: {}%'.format(air_temperature, pressure, humid))
        db.insert(air_temperature, air_pressure, humidity)
    
