#!/usr/bin/python
#Imports:
import datetime
import time
import os
import glob
import configparser
import picamera
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
CamLocation = '/home/chempi/workspace/chempi/ChemPi/html/Pictures'
camera = picamera.PiCamera()
#Read config file

config = configparser.ConfigParser()
config.read('html/config.txt')
ConfTemperature = config['Config']['Temperature']
ConfTempGPIO = config['Config']['TempGPIO']
ConfLight = config['Config']['Light']
ConfLightGPIO = config['Config']['LightGPIO']

ConfpH = config['Config']['pH']
ConfpHGPIO = config['Config']['pHGPIO']
ConfCarbonDioxide = config['Config']['CarbonDioxide']
ConfCarbonDioxideGPIO = config['Config']['CarbonDioxideGPIO']
ConfOxygen = config['Config']['Oxygen']
ConfOxygenGPIO = config['Config']['OxygenGPIO']
ConfPiCam = config['Config']['PiCam']
ConfInterval = config['Config']['Interval']
print(ConfLightGPIO)

	#HTML location:
HTMLLocation = "/var/www/html/"

#Temperature
	#Temperature File name:
TempeFN="csv/Temperature.csv"


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
	MeasureTime = time.time()	
	Temp_Return = str(MeasureTime) + ", " + str(read_temp()) + ",\n"
	return Temp_Return

#pH
	#pH File name:
pHFN="csv/pH.csv"

def pHMeasure():
	MeasureTime = time.time()	
	pH_Return = str(MeasureTime) + ", Test - pH is measured, \n"
	return pH_Return

#Oxygen
	#Oxygen File name:
OxygenFN="csv/Oxygen.csv"

def OMeasure():
	MeasureTime = time.time()	
	O_Return = str(MeasureTime) + ", Test - O is measured, \n"
	return O_Return


#Carbon Dioxide
	#CO2 File name:
COTwoFN="csv/COTwo.csv"


def COTwoMeasure():
	MeasureTime = time.time()	
	COTwo_Return = str(MeasureTime) + ", Test - CO2 is measured, \n"
	return COTwo_Return

#Light measure
        #Light File name:
LightFN="csv/Light.csv"

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
	MeasureTime = time.time()	
	Light_Return = str(MeasureTime) + ", " + str(RCtime(3)) + ",\n"
	return Light_Return


def TakePic():
	MeasureTime = time.time()	
	camera.capture("%s%s.jpg" % (CamLocation, MeasureTime))
	return 0

lastInterval = 0
while True:
	if lastInterval>CameraInterval:
		TakePic()
		lastInterval=0
	else:
		lastInterval = lastInterval + ReportingInterval
		

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
