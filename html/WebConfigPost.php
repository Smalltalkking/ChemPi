<html>
<head>
<title>
WebConfig
</title>
</head>
<body>
<h1> Webconfig  </h1>
<?php
$Temperature = $_POST["Temperature"];
$Light = $_POST["Light"];
$Interval = $_POST["Interval"];


// Open the file 
$file = 'config.txt';
$configText = 
"Temperature = " . $_POST["Temperature"] . "\n TempGPIO = " . $_POST["TempGPIO"] .
"\n" . "Light = " . $_POST["Light"] . "\n" . "LightGPIO = " . $_POST["LightGPIO"] . 
"\n" . "pH = " . $_POST["pH"] . "\n" . "pHGPIO = " . $_POST["pHGPIO"] . 
"\n" . "CarbonDioxide = " . $_POST["CarbonDioxide"] . "\n" . "CarbonDioxideGPIO = " . $_POST["CarbonDioxideGPIO"] . 
"\n" . "Oxygen = " . $_POST["Oxygen"] . "\n" . "OxygenGPIO = " . $_POST["OxygenGPIO"] . 
"\n" . "PiCam = " . $_POST["PiCam"] . "\n" . "CamRepInterval = " . $_POST["CamRepInterval"] . 
"\n" . "Interval = " . $_POST["Interval"] . 
"\n" . "";
// Write the contents back to the file
file_put_contents($file, $configText);

echo $configText;
?>



</body>
</html>
