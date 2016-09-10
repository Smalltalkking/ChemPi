#!/usr/bin/python
#Imports:
import configparser

config = configparser.ConfigParser()
config.read('html/config.txt')
print(config['Config']['Temperature'])
print(config['Config']['TempGPIO'])
print(config['Config']['PiCam'])
