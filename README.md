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


