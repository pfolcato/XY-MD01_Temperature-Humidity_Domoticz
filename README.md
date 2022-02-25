# XY-MD01_Temperature-Humidity_Domoticz
Script that reads the temperature from a ModBus Temperature sensor connected on /dev/ttyUSB0 on a unix like device via a USB to RS485 converter.

The pymodbus library already return the temperature in an integer in Celcius and Humidity for this specific sensor model.

The sensor is a "XY-MD01" model. based on SHT20 sensor

Change IDX number and Domoticz Settings(ip, create dummy device Temp+Humidity
change 

Compatible with Python 3.7

Install dependencies:
    pip3 install pymodbus
    
   copy XY-MD01.py in /home/pi/domoticz/scripts/
   
Create a LUA script and copy the content of file Reader_XY-MD01.lua, modyfy the name of your dummy device in the script
