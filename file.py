
#!/usr/bin/env python

#from pymongo import MongoClient
import time
from  datetime import date
import os
import smtplib
import os.path
import json
import fileinput


toda=date.today()
triggerfilename=str(toda)+"Trigger.txt"
filename=str(toda)+"Data.txt"
json_file="Text.json"
print(filename)

PATH="/home/pi/Desktop/Python/"+filename
PATH1="/home/pi/Desktop/Python/"+json_file
PWP=200
def mean(list):
    sum=0
    totalnos=len(list)
    for each_item in list:
        sum=sum + int(each_item)
    avg=sum/int(totalnos)
    return avg
#connection=MongoClient('10.24.192.4', 27017)

#db=connection.plants
#mycollection=db.happyplants
#for each_item in mycollection.find():
#    print(each_item['temperature'])

if os.path.isfile(PATH):
    file_object=open('/home/pi/Desktop/Python/'+filename, "r")
else:
    print("Unable to open Data.txt, Something must have gone horribly wrong")
    exit(1)

file_html=open("/home/pi/Desktop/Python/HelloPlant.html", "w")
count=0
jsonDic=[]
list=[]
tempival=[]
humiival=[]
soilmois=[]

#Creating Trigger file


for each_line in file_object.readlines():

    count=count+1
    split_line=each_line.split(':', 2)
    temptotal=split_line[0]
    humiditytotal=split_line[1]
    soilmoistotal=split_line[2]
    humi=humiditytotal.split(' ',1)
    humilabel=humi[0]
    humival=humi[1]
    soil=soilmoistotal.split(' ',1)
    soillabel=soil[0]
    soilvaltotal=soil[1].split(' ', 1)
    soilvaltotallabel=soilvaltotal[0]
    soilvaltotalval=soilvaltotal[1]
    soillabelfi=soillabel+" "+soilvaltotallabel
    templabel=temptotal.split(' ', 1)[0]
    tempval=temptotal.split(' ',1)[1]
    print(templabel + tempval + humilabel + humival + soillabel + soilvaltotalval)
    tempival.append(tempval)
    humiival.append(humival)
    soilmois.append(soilvaltotalval)
    list.append(templabel + ": " + tempval + "    " + humilabel + ": " + humival+"     "+soillabelfi+": "+soilvaltotalval)


avg_temp=mean(tempival)
avg_humi=mean(humiival)
avg_soilmois=mean(soilmois)

#Build the Json Object

file_object1=open("/home/pi/Desktop/Python/"+json_file,"w")

count=0

for eachtemp in soilmois:
    moisdic={}
    count=count+1
    #json.dump({'Moisture':eachtemp, 'Time':count},outfile,indent=4)
    moisdic['Moisture']=int(eachtemp)
    moisdic['Sample Time']=int(count)
    jsonDic.append(moisdic)

with file_object1 as outfile:
    json.dump(jsonDic,outfile,indent=4)


#Sandy loam
F_c= 18/100 * 50
PWP=8/100 * 50
Plant_available=F_c-PWP

print(Plant_available)
print(avg_soilmois)

#logic for displaying alert button
#The soil moisture sensor refernece :
#Dry Soil- 300 and less
#Wet Soil(Ideal) - 300 to 700
#Flooded - > 700
StrPredic=""
img=""
if avg_soilmois>=700 and avg_soilmois<= 800:
    StrPredic="<h3>I will be thirsty tomorrow. Good idea to water me now!!</h3>"
    img="<center><img src='sad.png'></img></center> "
elif avg_soilmois>=900:
     StrPredic="<h3>I am super thirsty.</h3>"
     img="<center><img src='sad.png'></img></center> "
else:
    StrPredic="<h3>I am okay now.</h3>"
    img="<center><img src='happy.png'></img>"

if avg_soilmois >= 900:
        strDisplay="<center> <p id='status' style='color: #ffffff; background-color: #ff0000'> Attention!! plant needs help</p></center>"
        # logic for sending mails
        '''
        #server=smtplib.SMTP('smtp.gmail.com', 587);

        #server.ehlo()
        #server.starttls()
        #server.ehlo()
        #server.login("happy.plantv2.0@gmail.com", "happyplant2")

        #msg="Subject: Plant alert \n\n Plant 007 needs help"
        #server.sendmail("happy.plantv2.0@gmail.com","satabdi.ganguly89@gmail.com",msg)
        #server.quit()
        '''

        if os.path.isfile(PATH):
            trigger_file=open('/home/pi/Desktop/Python/'+triggerfilename, "w")
        trigger_file.write("Yes")
        trigger_file.close()
else:
        strDisplay="<center><p style='color:blue' id='status'>Status okay!</p></center>"
        if os.path.isfile(PATH):
            trigger_file=open('/home/pi/Desktop/Python/'+triggerfilename, "r+")

        for line in trigger_file.readlines():
            print(line)
            if line.strip() == "Yes":
                trigger_file.close()
                os.remove(triggerfilename)
                trigger_file=open('/home/pi/Desktop/Python/'+triggerfilename, "w")
                trigger_file.write("No")
                trigger_file.close()




    #mycollection.insert({templabel.lower():int(tempval), humilabel.lower():int(humival)})

inserted_list='<br>'.join(['*' + x for x in list])

file_html.write("""

	<html><!DOCTYPE html>
    <html lang="en">
	<link href='https://fonts.googleapis.com/css?family=Open+Sans:400,300,700' rel='stylesheet' type='text/css'>
    <link href='https://fonts.googleapis.com/css?family=PT+Serif:400,700,400italic' rel='stylesheet' type='text/css'>
    <link href='https://netdna.bootstrapcdn.com/font-awesome/4.2.0/css/font-awesome.css' rel='stylesheet' type='text/css'>
    <link href='https://maxcdn.bootstrapcdn.com/bootstrap/3.2.0/css/bootstrap.min.css' rel='stylesheet' type='text/css'>

    <link href='metricsgraphics.css' rel='stylesheet' type='text/css'>


    <script src='https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js'></script>
    <script src="d3.js" charset="utf-8"></script>
    <script src='metricsgraphics.min.js'></script>



	<title> Happy Plants</title><META HTTP-EQUIV="refresh" CONTENT="200"></head> <body> <center> <h2> %s </h2> </center> """ %toda)
file_html.write(""""

%s

""" %strDisplay)

file_html.write(""""

%s

""" %img)


file_html.write(""""

<center>Plant feelings: %s </center>

""" %StrPredic)


file_html.write("""
<center>
<div id="small"></div>
</center>
""")

file_html.write("""

%s


""" %inserted_list)


file_html.write("""
<script>
 d3.json('Text.json', function(data) {
    MG.data_graphic({
        title: "Peace Lily",
        description: "Timely Moisture ratings for the plant - Peace Lily",
        data: data,
        width: 650,
        height: 150,
        target: '#small',
        x_accessor: 'Sample Time',
        y_accessor: 'Moisture'
    })
})


 </script>

</body>
</html>

"""  )
