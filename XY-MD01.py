#!/usr/local/lib/python3.7
"""
Script that reads the temperature from a ModBus Temperature sensor connected on /dev/ttyUSB0 on a unix like device via a USB to RS485 converter.

The pymodbus library already return the temperature in an integer in Celcius and Humidity for this specific sensor model.

The sensor is a "XY-MD01" model.

Change IDX number and Domoticz Settings, create dummy device Temp+Humidity


Compatible with Python 3.7

Install dependencies:
    pip3 install pymodbus

Run:
   Enable this script to run at a regular interval (1 min):

sudo crontab -e

Create a LUA script and write this:
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
function timedifference (s)
            year = string.sub(s, 1, 4)
           month = string.sub(s, 6, 7)
            day = string.sub(s, 9, 10)
             hour = string.sub(s, 12, 13)
            minutes = string.sub(s, 15, 16)
             seconds = string.sub(s, 18, 19)
             tempo1 = os.time()
             tempo2 = os.time{year=year, month=month, day=day, hour=hour, min=minutes, sec=seconds}
            difference = os.difftime (tempo1, tempo2)
           return difference
         end

 commandArray = {}
 
--debug = 0
           deltatime = timedifference(otherdevices_lastupdate['Sensore_RS485']) --Change The device name accordig to name of Dummy sensor that you have create in domoticz

           print('deltatime_RS485='..deltatime)


             
        if deltatime > 10 then ---read the sensor every 10 seconds, change this value if you want.
            os.execute ('/usr/bin/python3 /home/pi/domoticz/scripts/XY-MD01.py >/dev/null 2>&1')
        end
        
return commandArray
---------------------------------------------------------------------------------------------------------------------------------------------------------------------





"""
#!/usr/bin/env python
import urllib.request
import base64
import time
import pymodbus
from pymodbus.client.sync import ModbusSerialClient as ModbusClient


# Settings for the domoticz server



domoticzserver   = "10.0.0.10:8080" # change according your domoticz settings
domoticzusername = ""
domoticzpassword = ""
# Sensor IDs
idx_temp = "278"  # insert the correct IDX number of Temperature and Humidity dummy device created on Domoticz

base64string = base64.encodestring(('%s:%s' % (domoticzusername, domoticzpassword)).encode()).decode().replace('\n', '')



# Create virtual sensors in dummy hardware
# type temperature & humidity
 
client = ModbusClient(method="rtu", port="/dev/ttyUSB0", stopbits=1, bytesize=8, parity="N", baudrate=9600, timeout=1, retries=2)
client.connect()
data = client.read_input_registers(1, 2, unit=1) # FUNCTION 04 - READ register (start=1, length=2, unitid=12)
client.close()
Temperatura = data.registers[0] / 10
Umidit = data.registers[1] / 10

def domoticzrequest (url):
  print(url)
  request = urllib.request.Request(url)
  request.add_header("Authorization", "Basic %s" % base64string)
  response = urllib.request.urlopen(request)
  return response.read()

#global domoticzserver

val_temp = str(Temperatura)
val_hum = str(Umidit)
val_comfort = "0"
if float(val_hum) < 40:
        val_comfort = "2"
elif float(val_hum) <= 70:
        val_comfort = "1"
elif float(val_hum) > 70:
        val_comfort = "3"
        
domoticzrequest("http://" + domoticzserver + "/json.htm?type=command&param=udevice&idx=" + idx_temp + "&nvalue=0&svalue=" + val_temp + ";" + val_hum + ";"+ val_comfort )   
        
    

