import utime, time

def convertToMPH(rawknots):
    try:
        rawknotsfloat = float(rawknots)
        return rawknotsfloat*1.15078
    except:
        return -1.0

def convertToDegree(RawDegrees):

    RawAsFloat = float(RawDegrees)
    firstdigits = int(RawAsFloat/100) 
    nexttwodigits = RawAsFloat - float(firstdigits*100) 
    
    Converted = float(firstdigits + nexttwodigits/60.0)
    Converted = '{0:.6f}'.format(Converted) 
    return str(Converted)

def update_oled():
    global latitude, longitude, satellites, GPStime, speed_mph, maxspeed
    oled.fill(0)
    oled.text("Lat: "+latitude, 0, 0)
    oled.text("Lng: "+longitude, 0, 10)
    oled.text("Satellites: "+satellites, 0, 20)
    oled.text("Time: "+GPStime, 0, 30)
    oled.text("CurSpeed: "+str(speed_mph), 0, 40)
    oled.text("MaxSpeed: "+str(maxspeed), 0, 50)
    oled.show()    

gpsModule = UART(1, baudrate=9600)
maxspeed = 0
latitude = ""
longitude = ""
satellites = ""
GPStime = ""
print(gpsModule)

while True:
    x=gpsModule.readline()
    parts = str(x).split(',')
    if parts[0]=="b'$GPRMC":
        speed_mph = convertToMPH(parts[7])
        if maxspeed < speed_mph:
            maxspeed = speed_mph
        update_oled()
        #print('\nSpeed in mph: {}\n'.format(speed_mph))
        
    if (parts[0] == "b'$GPGGA" and len(parts) == 15):
        if(parts[1] and parts[2] and parts[3] and parts[4] and parts[5] and parts[6] and parts[7]):            
            latitude = convertToDegree(parts[2])
            if (parts[3] == 'S'):
                latitude = "-" + latitude
            longitude = convertToDegree(parts[4])
            if (parts[5] == 'W'):
                longitude = "-"+longitude
            satellites = parts[7]
            GPStime = parts[1][0:2] + ":" + parts[1][2:4] + ":" + parts[1][4:6]
            
            update_oled()

    utime.sleep_ms(500)
