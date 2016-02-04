#!/bin/sh
echo "Now running Sensor monitor"
sudo python /home/pi/Desktop/Python/InterfaceKit-TempHumi.py
sleep 10

#query after a fixed time 
sudo python /home/pi/Desktop/Python/file.py
sleep 10  

echo 'Done'

