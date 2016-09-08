#!/bin/bash
#This project is running on Ubuntu Mate for Raspberry pi, but will be written in 
#python and php, so it should be easy to setup on different environments, and even different units, 
#like intel based computers, and running parts on arduino, etc.
cd ~/
mkdir workspace
cd workspace
mkdir chempi
cd chempi
#Standard install without Big Algae
sudo apt-get install apache2 php mariadb-server git 

#Big Algae dependencies
sudo apt-get install python-opencv libcv-dev python-matplotlib python-scipy python-numpy python-pip
sudo pip install piexif GPy  
git clone --recursive https://github.com/Big-Algae-Open-Experiment/computational_writeup.git
git clone --recursive https://github.com/Big-Algae-Open-Experiment/bigalgae.git
git clone --recursive https://github.com/TobiasFP/ChemPi.git
