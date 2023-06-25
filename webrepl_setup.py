import webrepl_setup

import network
ap = network.WLAN(network.AP_IF)
print(ap.config('essid'))
# Done
