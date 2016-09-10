#!/bin/bash
#This project is running on Ubuntu Mate for Raspberry pi, but will be written in 
#python and php, so it should be easy to setup on different environments, and even different units, 
#like intel based computers, and running parts on arduino, etc.
#A must-have is of course a GPIO, so if you want to setup your computer with this, 
#please buy https://www.adafruit.com/product/2264 or similar.
#The following setup is a work in progress, and SHOULD NOT BE CONSIDERED SAFE NOR GOOD PRACTICE. (Especially the symlink parts) 
#Your computer/Raspberry Pi will most likely be very easy to hack.

#Set standard directory, and create directories
cd ~/
mkdir workspace
cd workspace
mkdir chempi
cd chempi

#Standard install without Big Algae
sudo apt-get install apache2 php mariadb-server git python-pip 
sudo pip install picamera
git clone --recursive https://github.com/TobiasFP/ChemPi.git

#Create symlink to html folder
sudo rm -R /var/www/html
sudo ln -s ~/workspace/chempi/chempi/html/ /var/www/html

#setup permissions, but please keep in mind that this is not written to be secure just yet.
sudo chmod u=rwX,g=srX,o=rX -R /var/www/
sudo chmod u=rwX,g=srX,o=rX -R ~/workspace/chempi/chempi/html/

#Big Algae dependencies and installation
echo "Do you want Big Algae?, (y/n) + [ENTER]:"

read  answer
if ( [ "$answer" =  'y' ]  ||  ["$answer" = 'Y' ]); then
	{
    sudo apt-get install python-opencv libcv-dev python-matplotlib python-scipy python-numpy
    sudo pip install piexif GPy  
    git clone --recursive https://github.com/Big-Algae-Open-Experiment/computational_writeup.git
    git clone --recursive https://github.com/Big-Algae-Open-Experiment/bigalgae.git
    echo "Installer finished, installing Big Algae"
	}
	else
		{
			echo "Installer finished, without installing Big Algae"
		}
	fi
