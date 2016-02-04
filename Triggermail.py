#!/usr/bin/env python

#Mail sending Script

import os
import fileinput
import smtplib
from  datetime import date

toda=date.today()
triggerfilename=str(toda)+"Trigger.txt"


trigger_file=open('/home/pi/Desktop/Python/'+triggerfilename,'r')
for line in trigger_file.readlines():
    if line == "Yes":

        server=smtplib.SMTP('smtp.gmail.com', 587);

        server.ehlo()
        server.starttls()
        #server.ehlo()
        server.login("happy.plantv2.0@gmail.com", "happyplant2")

        msg="Subject: Plant alert \n\n Plant Peace Lily  needs help"
        server.sendmail("happy.plantv2.0@gmail.com","satabdi.ganguly89@gmail.com",msg)
        server.quit()
	trigger_file.close()


