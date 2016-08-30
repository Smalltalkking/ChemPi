#!/usr/bin/python
#Imports:
import datetime
import time
import os
import glob
import time
#initialize the device 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
#Config:
	#Reporting interval
ReportingInterval = 300

	#HTML location:
HTMLLocation = "/home/tobias/workspace/ChemPi/"

#Temperature
	#Temperature File name:
TempeFN="Temperature.csv"


def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        return temp_c

def TemperatureMeasure():
	MeasureTime = datetime.datetime.now()	
	Temp_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", " + read_temp() + "\n"
	return Temp_Return

#pH
	#pH File name:
pHFN="pH.csv"

def pHMeasure():
	MeasureTime = datetime.datetime.now()	
	pH_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - pH is measured, \n"
	return pH_Return

#Oxygen
	#Oxygen File name:
OxygenFN="Oxygen.csv"

def OMeasure():
	MeasureTime = datetime.datetime.now()	
	O_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - O is measured, \n"
	return O_Return

	#CO2 File name:
COTwoFN="COTwo.csv"

#Carbon Dioxide
def COTwoMeasure():
	MeasureTime = datetime.datetime.now()	
	COTwo_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - CO2 is measured, \n"
	return COTwo_Return

while True:
	with open(HTMLLocation+TempeFN, "a") as myfile:
    		myfile.write(TemperatureMeasure())

	with open(HTMLLocation+pHFN, "a") as myfile:
    		myfile.write(pHMeasure())

	with open(HTMLLocation+OxygenFN, "a") as myfile:
    		myfile.write(OMeasure())

	with open(HTMLLocation+COTwoFN, "a") as myfile:
    		myfile.write(COTwoMeasure())
	time.sleep(ReportingInterval)
