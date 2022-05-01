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
speed_mph = 0
latitude = ""
longitude = ""
satellites = ""
GPStime = ""
print(gpsModule)

# For more details and step by step guide visit: Microcontrollerslab.com
led_state = "ON"
def web_page():
    html = """<html>

<head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="refresh" content="1">
    <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.7.2/css/all.css"
     integrity="sha384-fnmOCqbTlWIlj8LyTjo7mOUStjsKC4pOpQbqyi7RrhN7udi9RwhKkMHpvLbHG9Sr" crossorigin="anonymous">
    <style>
        html {
            font-family: Arial;
            display: inline-block;
            margin: 0px auto;
            text-align: center;
        }

        .button {
            background-color: #ce1b0e;
            border: none;
            color: white;
            padding: 16px 40px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }

        .button1 {
            background-color: #000000;
        }
    </style>
</head>

<body>
    <h2>ESP ADRK Web Server</h2>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <h3> GPS readings</h3>
 <table style="border:1px solid black;margin-left:auto;margin-right:auto;">
  <tr>
     <th>Entity</th>
     <th>Value</th>
  <tr>
    <td>Latitude</td>
    <td>""" + str(latitude) +"""</td>
  </tr>
  <tr>
    <td>Longitude</td>
    <td>""" + str(longitude) +"""</td>
  </tr>
  <tr>
    <td>Satelllites</td>
    <td>""" + str(satellites) +"""</td>
  </tr>
  <tr>
    <td>GPSTime</td>
    <td>""" + str(GPStime) +"""</td>
  </tr>
  <tr>
    <td>Current Speed</td>
    <td>""" + str(speed_mph) +"""</td>
  </tr>
  <tr>
    <td>Max Speed</td>
    <td>""" + str(maxspeed) +"""</td>
  </tr>
</table> 
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"?led_2_on\"><button class="button">LED OFF</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"?led_2_off\"><button class="button button1">LED ON</button></a>
    </p>
</body>

</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

def get_vals():
    global gpsModule, latitude, longitude, satellites, GPStime, speed_mph, maxspeed
    x=gpsModule.readline()
    parts = str(x).split(',')
    if parts[0]=="b'$GPRMC" and len(parts)==13:
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

while True:
    try:
        if gc.mem_free() < 102000:
            gc.collect()
        conn, addr = s.accept()
        conn.settimeout(3.0)
        print('Received HTTP GET connection request from %s' % str(addr))
        request = conn.recv(1024)
        conn.settimeout(None)
        request = str(request)
        print('GET Rquest Content = %s' % request)
        led_on = request.find('/?led_2_on')
        led_off = request.find('/?led_2_off')
        if led_on == 6:
            print('LED OFF -> GPIO2')
            led_state = "ON"
            led.off()
        if led_off == 6:
            print('LED -> GPIO2')
            led_state = "OFF"
            led.on()
        _ = get_vals()
        time.sleep(0.2)
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')
