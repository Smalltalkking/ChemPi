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
sudo apt-get install pip3 apache2 php mariadb-server git

#Big Algae dependencies
sudo apt-get install OpenCV piexif GPy numpy scipy matplotlib
git clone --recursive https://github.com/Big-Algae-Open-Experiment/computational_writeup.git
git clone --recursive https://github.com/Big-Algae-Open-Experiment/bigalgae.git
git clone --recursive https://github.com/TobiasFP/ChemPi.git
