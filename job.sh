
#!/bin/sh

echo "Server Up and running"
su pi -c 'node  /home/pi/Desktop/Python/helloworld.js < /dev/null &' &

#echo "Now running Sensor monitor"
#(watch -n 60  sudo python /home/pi/Desktop/Python/InterfaceKit-TempHumi.py)&
#sleep 10
#query after a fixed time 
#(watch -n 80  sudo python /home/pi/Desktop/Python/file.py)&
#sleep 10 
echo 'Done'

