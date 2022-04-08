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
    <h2>ESP MicroPython Web Server</h2>
    <p>LED state: <strong>""" + led_state + """</strong></p>
    <h3> Accelerometer readings</h3>
 <table style="border:1px solid black;margin-left:auto;margin-right:auto;">
  <tr>
     <th>Entity</th>
     <th>Value</th>
  <tr>
    <td>GyZ</td>
    <td>""" + str(accel['GyZ']) +"""</td>
  </tr>
  <tr>
    <td>GyX</td>
    <td>""" + str(accel['GyX']) +"""</td>
  </tr>
  <tr>
    <td>GyY</td>
    <td>""" + str(accel['GyY']) +"""</td>
  </tr>
  <tr>
    <td>Tmp</td>
    <td>""" + str(accel['Tmp']) +"""</td>
  </tr>
  <tr>
    <td>AcZ</td>
    <td>""" + str(accel['AcZ']) +"""</td>
  </tr>
  <tr>
    <td>AcX</td>
    <td>""" + str(accel['AcX']) +"""</td>
  </tr>
  <tr>
    <td>AcY</td>
    <td>""" + str(accel['AcY']) +"""</td>
  </tr>
</table> 
    <p>
        <i class="fas fa-lightbulb fa-3x" style="color:#c81919;"></i>
        <a href=\"?led_2_on\"><button class="button">LED ON</button></a>
    </p>
    <p>
        <i class="far fa-lightbulb fa-3x" style="color:#000000;"></i>
        <a href=\"?led_2_off\"><button class="button button1">LED OFF</button></a>
    </p>
</body>

</html>"""
    return html


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

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
        time.sleep(0.3)
        accel = accelerometer.get_values()
        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()
    except OSError as e:
        conn.close()
        print('Connection closed')

