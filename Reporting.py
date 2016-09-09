#!/usr/bin/python
#Imports:
import datetime
import time
import os
import glob
import time
import ConfigParser
import RPi.GPIO as GPIO
GPIO.setwarnings(False)

DEBUG = 1
GPIO.setmode(GPIO.BCM)

#initialize the thermometer 
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'


#Config:
	#Reporting interval
ReportingInterval = 3
	#Camera interval (3600=1 hour)
CameraInterval = 3600

#Read config file

config = ConfigParser.ConfigParser()
config.read("html/config.txt")
var_a = config.get("GPIOConfig", "var_a")
var_b = config.get("GPIOConfig", "var_b")
var_c = config.get("GPIOConfig", "var_c")

	#HTML location:
HTMLLocation = "/var/www/html/"

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
	Temp_Return = MeasureTime.strftime('%Y%m%d%H%M%S') + ", " + str(read_temp()) + ",\n"
	return Temp_Return

#pH
	#pH File name:
pHFN="pH.csv"

def pHMeasure():
	MeasureTime = datetime.datetime.now()	
	pH_Return = MeasureTime.strftime('%Y%m%d%H%M%S') + ", Test - pH is measured, \n"
	return pH_Return

#Oxygen
	#Oxygen File name:
OxygenFN="Oxygen.csv"

def OMeasure():
	MeasureTime = datetime.datetime.now()	
	O_Return = MeasureTime.strftime('%Y%m%d%H%M%S') + ", Test - O is measured, \n"
	return O_Return


#Carbon Dioxide
	#CO2 File name:
COTwoFN="COTwo.csv"


def COTwoMeasure():
	MeasureTime = datetime.datetime.now()	
	COTwo_Return = MeasureTime.strftime('%Y%m%d%H%M%S') + ", Test - CO2 is measured, \n"
	return COTwo_Return

#Light measure
        #Light File name:
LightFN="Light.csv"

def RCtime (RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(.1)
 
        GPIO.setup(RCpin, GPIO.IN)
        # This takes about 1 millisecond per loop cycle
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading

def LightMeasure():
	MeasureTime = datetime.datetime.now()	
	Light_Return = MeasureTime.strftime('%Y%m%d%H%M%S') + ", " + str(RCtime(3)) + ",\n"
	return Light_Return


while True:
	with open(HTMLLocation+TempeFN, "a") as myfile:
    		myfile.write(TemperatureMeasure())

	with open(HTMLLocation+pHFN, "a") as myfile:
    		myfile.write(pHMeasure())

	with open(HTMLLocation+OxygenFN, "a") as myfile:
    		myfile.write(OMeasure())

	with open(HTMLLocation+COTwoFN, "a") as myfile:
    		myfile.write(COTwoMeasure())

        with open(HTMLLocation+LightFN, "a") as myfile:
                myfile.write(LightMeasure())


        time.sleep(ReportingInterval)
