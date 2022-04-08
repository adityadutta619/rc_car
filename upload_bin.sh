#!/bin/bash

# Download the binary file

if [ -f esp_8266.bin  ]
then
	echo "File exists not downloading again"
else
	wget -O esp_8266.bin https://micropython.org/resources/firmware/esp8266-20220117-v1.18.bin
fi

# Check if the esp is connected

cnt=$(lsusb | grep "UART" | wc -l)
if [ $cnt -gt 0 ]
then
	for sysdevpath in $(find /sys/bus/usb/devices/usb*/ -name dev); do
	    (
		syspath="${sysdevpath%/dev}"
		devname="$(udevadm info -q name -p $syspath)"
		[[ "$devname" == "bus/"* ]] && exit
		eval "$(udevadm info -q property --export -p $syspath)"
		[[ -z "$ID_SERIAL" ]] && exit
		device="/dev/$devname - $ID_SERIAL"
		device_port=$(echo $device | awk -F' -' '{print $1}')
		

		if [ $(echo $device | grep "UART" | wc -l) -gt 0 ]
		then
			echo "Detected UART esp"
			echo $device
			echo $device_port
		#	usb_path=$("$device" | awk -F' -' '{print $1}')

			# Copy downloaded file to device
			# Make sure you have esptool installed

			sudo chmod -R 777 $device_port

			echo "Erasing flash on esp"
			esptool.py --port $device_port erase_flash

			wait $!

			echo "Uploading new firmware"
			esptool.py --port $device_port --baud 115200 write_flash --flash_size=detect 0 esp_8266.bin

			wait $!

		

		fi
	    )

	done

else
	echo "ESP not detected. Are you using the right cable?"
fi

