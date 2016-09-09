<html>
 <head>
 <title>
 WebConfig
 </title>
     <style type="text/css">
	form  { display: table;      }
	p     { display: table-row;  }
	label { display: table-cell; }
	input { display: table-cell; }
    </style>
 </head>
 <body>
 <h1> Webconfig  </h1>
 
 <form action="WebConfigPost.php" method="post">
   <fieldset>
   <p> <label for="Temperature" >Temperature: </label> <input type="checkbox" name="Temperature" value="Temperature" id="Temperature">  </p>
   <p> <label for="TempGPIO" > GPIO number: </label><input type="number" name="TempGPIO" id="TempGPIO" min="0" max="50" step="1" value="3">   <br /> </p>
   <p> <label for="Light" > Light: </label><input type="checkbox" name="Light" id="Light" value="Light">  </p>
   <p> <label for="LightGPIO" > GPIO number: </label><input type="number" name="LightGPIO" id="LightGPIO" min="0" max="50" step="1" value="21">  <br /></p>
   <p> <label for="pH" >pH: </label><input type="checkbox" name="pH" id="pH" value="pH"> </p>
   <p> <label for="pHGPIO" >GPIO number: </label><input type="number" name="pHGPIO" id="pHGPIO" min="0" max="50" step="1" value="27"> <br /></p>
   <p> <label for="CarbonDioxide" >CarbonDioxide: </label><input type="checkbox" name="CarbonDioxide"id="CarbonDioxide" value="CarbonDioxide">  </p>
   <p> <label for="CarbonDioxideGPIO" >GPIO number: </label><input type="number" name="CarbonDioxideGPIO"id="CarbonDioxideGPIO" min="0" max="50" step="1" value="3"> <br /> </p>
   <p> <label for="Oxygen" >Oxygen: </label><input type="checkbox" name="Oxygen" id="Oxygen" value="Oxygen">  </p>
   <p> <label for="OxygenGPIO" >GPIO number: </label><input type="number" name="OxygenGPIO" id ="OxygenGPIO"  min="0" max="50" step="1" value="3">  <br /></p>

   <p> <label for="Interval" >Update interval [sec]: </label><input type="number" name="Interval" id="Interval" min="0" max="100000" step="10" value="3"> <br /> <br /></p>

   <p> <label for="PiCam" >Pi Camera: </label><input type="checkbox" name="PiCam" id="PiCam" value="PiCam"> </p>

   <p><label for="CamRepInterval" > Camera capture interval [sec]: </label><input type="number" name="CamRepInterval" id="CamRepInterval" min="0" max="100000" step="1" value="3600"> </p><br />
   </fieldset>
   </form>
   </body>
   </html>
   


</body>
</html>
