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
 
           deltatime = timedifference(otherdevices_lastupdate['Sensore_RS485'])--Change The device name accordig to name of Dummy sensor that you have create in domoticz

           print('deltatime_RS485='..deltatime) ---read the sensor every 10 seconds, change this value if you want.


             
        if deltatime > 10 then
            os.execute ('/usr/bin/python3 /home/pi/domoticz/scripts/XY-MD01.py >/dev/null 2>&1')
        end
        
return commandArray