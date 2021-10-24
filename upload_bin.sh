download_dir="/home/aditya/Downloads"

# Download the binary file to Downloads directory
wget -P $download_dir -O esp_8266.bin https://micropython.org/resources/firmware/esp8266-20210902-v1.17.bin

# Check if the esp is connected
#!/bin/bash

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
			echo $chk
		#	usb_path=$("$device" | awk -F' -' '{print $1}')

			# Copy downloaded file to device
			# Make sure you have esptool installed

			echo "Erasing flash on esp"
			esptool.py --port $device_port erase_flash

			wait $!

			echo "Uploading new firmware"
			esptool.py --port $device_port --baud 460800 write_flash --flash_size=detect 0 "$download_dir/esp_8266.bin"

		

		fi
	    )

	done

else
	echo "ESP not detected. Are you using the right cable?"
fi

