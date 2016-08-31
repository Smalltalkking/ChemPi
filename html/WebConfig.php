<html>
<head>
<title>
WebConfig
</title>
</head>
<body>
<h1> Webconfig  </h1>

<form action="WebConfigPost.php" method="post">
  <input type="checkbox" name="Temperature" value="Temperature"> Temperature 
  <input type="number" name="TempGPIO" min="0" max="50" step="1" value="3"> GPIO number  <br />
  <input type="checkbox" name="Light" value="Light"> Light 
  <input type="number" name="LightGPIO" min="0" max="50" step="1" value="21"> GPIO number <br />
  <input type="checkbox" name="pH" value="pH"> pH 
  <input type="number" name="pHGPIO" min="0" max="50" step="1" value="27"> GPIO number <br />
  <input type="checkbox" name="CarbonDioxide" value="CarbonDioxide"> CarbonDioxide 
  <input type="number" name="CarbonDioxideGPIO" min="0" max="50" step="1" value="3"> GPIO number <br />
  <input type="checkbox" name="Oxygen" value="Oxygen"> Oxygen 
  <input type="number" name="OxygenGPIO" min="0" max="50" step="1" value="3"> GPIO number <br />
  
  
  <input type="number" name="Interval" min="0" max="100000" step="10" value="3"> Update interval [sec] <br />

<input type="submit">
</form>


</body>
</html>
