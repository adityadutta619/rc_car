import network

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect('Conv', 'merryweather246')

wlan.ifconfig()