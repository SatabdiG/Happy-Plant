#!/usr/bin/env python

"""Copyright 2010 Phidgets Inc.
This work is licensed under the Creative Commons Attribution 2.5 Canada License. 
To view a copy of this license, visit http://creativecommons.org/licenses/by/2.5/ca/
"""

__author__ = 'Satabdi Ganguly'
__version__ = '1.0'
__date__ = 'August 30th 2015'

#Basic imports
from ctypes import *
import sys
import random
#Phidget specific imports
from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Events.Events import AttachEventArgs, DetachEventArgs, ErrorEventArgs, InputChangeEventArgs, OutputChangeEventArgs, SensorChangeEventArgs
from Phidgets.Devices.InterfaceKit import InterfaceKit
from Phidgets.Phidget import PhidgetLogLevel
import os
import os.path


#Create an interfacekit object
try:
    interfaceKit = InterfaceKit()
except RuntimeError as e:
    print("Runtime Exception: %s" % e.details)
    print("Exiting....")
    exit(1)

#global variables

#data= stores the sensor vales
data={}
#stores data values fetched periodically from the sensor values
PATH="./Data.txt"

#Information Display Function
def displayDeviceInfo():
    print("|------------|----------------------------------|--------------|------------|")
    print("|- Attached -|-              Type              -|- Serial No. -|-  Version -|")
    print("|------------|----------------------------------|--------------|------------|")
    print("|- %8s -|- %30s -|- %10d -|- %8d -|" % (interfaceKit.isAttached(), interfaceKit.getDeviceName(), interfaceKit.getSerialNum(), interfaceKit.getDeviceVersion()))
    print("|------------|----------------------------------|--------------|------------|")
    print("Number of Digital Inputs: %i" % (interfaceKit.getInputCount()))
    print("Number of Digital Outputs: %i" % (interfaceKit.getOutputCount()))
    print("Number of Sensor Inputs: %i" % (interfaceKit.getSensorCount()))

#Event Handler Callback Functions
def interfaceKitAttached(e):
    attached = e.device
    print("InterfaceKit %i Attached!" % (attached.getSerialNum()))

def interfaceKitDetached(e):
    detached = e.device
    print("InterfaceKit %i Detached!" % (detached.getSerialNum()))

def interfaceKitError(e):
    try:
        source = e.device
        print("InterfaceKit %i: Phidget Error %i: %s" % (source.getSerialNum(), e.eCode, e.description))
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))

def interfaceKitInputChanged(e):
    source = e.device
    print("InterfaceKit %i: Input %i: %s" % (source.getSerialNum(), e.index, e.state))

def interfaceKitSensorChanged(e):
    source = e.device
    if e.value != 0:
        data[e.index]=e.value
    print("InterfaceKit %i: Sensor %i: %i" % (source.getSerialNum(), e.index, e.value))

def interfaceKitOutputChanged(e):
    source = e.device
    print("InterfaceKit %i: Output %i: %s" % (source.getSerialNum(), e.index, e.state))

def filewrite(datavalues):

    #file handler code
    if os.path.isfile(PATH):
        file_object=open("Data.txt", "a")
    else:
        file_object=open("Data.txt", "w")
    for i in datavalues.items():
        if i[0]== 0:
            file_object.write("Temperature "+ str(i[1])+ ":")
        else:
            file_object.write("Humidity "+ str(i[1]) +"\n")

#Main Program Code
try:
	#logging example, uncomment to generate a log file
    #interfaceKit.enableLogging(PhidgetLogLevel.PHIDGET_LOG_VERBOSE, "phidgetlog.log")
	
    interfaceKit.setOnAttachHandler(interfaceKitAttached)
    interfaceKit.setOnDetachHandler(interfaceKitDetached)
    interfaceKit.setOnErrorhandler(interfaceKitError)
    interfaceKit.setOnInputChangeHandler(interfaceKitInputChanged)
    interfaceKit.setOnOutputChangeHandler(interfaceKitOutputChanged)
    interfaceKit.setOnSensorChangeHandler(interfaceKitSensorChanged)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Opening phidget object....")

try:
    interfaceKit.openPhidget()
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    print("Exiting....")
    exit(1)

print("Waiting for attach....")

try:
    interfaceKit.waitForAttach(10000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))
    try:
        interfaceKit.closePhidget()
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
        print("Exiting....")
        exit(1)
    print("Exiting....")
    exit(1)
else:
    displayDeviceInfo()

print("Setting the data rate for each sensor index to 4ms....")
for i in range(interfaceKit.getSensorCount()):
    try:
        
        interfaceKit.setDataRate(i, 4)
    except PhidgetException as e:
        print("Phidget Exception %i: %s" % (e.code, e.details))
#Call to filewriter
filewrite(data)
print(data)

#close the ports
print("Done.")
exit(0)
