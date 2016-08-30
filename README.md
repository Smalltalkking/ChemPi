# ChemPi
Software (and hardware explanation) for realtime monitoring of chemical attributes in experiments, such as pH, CO2 levels, O levels,  Temperature, etc. using sensors attached to the Raspberry Pi (2+3)

The ChemPi will consist of a Raspberry Pi (1, 2, 3 or newer), which will monitor whatever you need to monitor. Input will be read from the GPIO via a breadboard.


The web server will be run directly from the Pi, but will only display csv files rendered by javascript, so as to make sure the Pi will not get too stressed. 

The GPIO will be read via Python, and CSV files will be created with date as one parameter, and the levels as the other, and served directly to the webserver (Apache + html or PHP). The ChemPi will also be able to send out emails, if a limit is reached. This will be monitored via Python, but may be configured from the webserver via PHP.
