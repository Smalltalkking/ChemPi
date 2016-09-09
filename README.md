# ChemPi
Software (and hardware explanation) for realtime monitoring of chemical attributes in experiments, such as pH, CO2 levels, O levels,  Temperature, etc. using sensors attached to the Raspberry Pi (2+3)

The ChemPi will consist of a Raspberry Pi ([1], 2, 3 or newer), which will monitor whatever you need to monitor. Input will be read from the GPIO via a breadboard.

The web server will be run directly from the Pi, but will only display csv files rendered by javascript, so as to make sure the Pi will not get too stressed. 

The GPIO will be read via Python, and CSV files will be created with date as one parameter, and the levels as the other, and served directly to the webserver (Apache + html or PHP). The ChemPi will also be able to send out emails, if a limit is reached. This will be monitored via Python, but may be configured from the webserver via PHP.

A Webconfig will also be created, so as to be able to use the system headless. Here it will be possible to set which periferals are connected, GPIO inputs, data recording intervals, Big Algae processing interval and more.


The great work from Big Algae (https://github.com/Big-Algae-Open-Experiment) will also be implemented into the project. This part will of course be optional. The system will function in a way that a camera will take photos at an interval set by the user (via webconfig). There will be the possibility to either run the Big Algae alghoritms locally or externally. When run locally, the Big Algae python+OpenCV module will be allocated one full CPU Core(Out of the Pi´s 4 cores), and will most likely be set to run every night at 2 o' clock (Webconfig Configurability will be made possible at a later stage).


Announcing BigAlgae+Chempi OS. A raspberry Pi "distro" based on Ubuntu Mate 16.04.
This will be a distro with everything from the Chempi and Big Algae installed, and it will be distributed as ISO/IMG files just like all other Raspberry Pi distros. The Distro will include detailed assembly instructions, Hardware recommendations, basic installation, and hopefully somebody that knows about Software security will help stabilize security issues. 
