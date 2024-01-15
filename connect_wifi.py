import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('RedPanda_2.4', 'merryweather246')

print(wlan.ifconfig())