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

from time import sleep
sleep(3)

for i in range(10):
    txts = [i for i in wlan.ifconfig()]
    txts.append('      ')
    txts.append('  By ADRK!!')
    sleep(0.5)
    helpers.dev_disp(txts)