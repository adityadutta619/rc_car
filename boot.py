# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
import uos, machine
#uos.dupterm(None, 1) # disable REPL on UART(0)
import gc
import webrepl
webrepl.start()
gc.collect()

try:
    import helpers
except:
    pass

import network
wlan = network.WLAN(network.STA_IF)

txts = []
if wlan.active():
    txts.append('Network connected')
    ipaddress = wlan.ifconfig()[0]
    txts.append('webrepl active at: ')
    txts.append(ipaddress)
    
    txts.append('Connect RC CAR')
    txts.append('By ADRK!!')

helpers.dev_disp(txts)