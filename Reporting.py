#!/usr/bin/python
#Imports:
import datetime
import time

#Config:
	#Reporting interval
ReportingInterval = 300

	#HTML location:
HTMLLocation = "/home/tobias/workspace/ChemPi/"

	#Temperature File name:
TempeFN="Temperature.csv"

def TemperatureMeasure():
	MeasureTime = datetime.datetime.now()	
	Temp_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - Temperature is measured, \n"
	return Temp_Return


	#pH File name:
pHFN="pH.csv"

def pHMeasure():
	MeasureTime = datetime.datetime.now()	
	pH_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - pH is measured, \n"
	return pH_Return

	#Oxygen File name:
OxygenFN="Oxygen.csv"

def OMeasure():
	MeasureTime = datetime.datetime.now()	
	O_Return = MeasureTime.strftime('%H:%M:%S::%m/%d %Y') + ", Test - O is measured, \n"
	return O_Return

	#CO2 File name:
COTwoFN="COTwo.csv"

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
