<html>
<head>
<title>
WebConfig
</title>
</head>
<body>
<h1> Webconfig  </h1>
<?php


// Open the file 
$file = "config.txt";
$configText = 
"[Config] \nTemperature = " . $_POST["Temperature"] . "\n" . "TempGPIO = " . $_POST["TempGPIO"] .
"\n" . "Light = " . $_POST["Light"] . "\n" . "LightGPIO = " . $_POST["LightGPIO"] . 
"\n" . "pH = " . $_POST["pH"] . "\n" . "pHGPIO = " . $_POST["pHGPIO"] . 
"\n" . "CarbonDioxide = " . $_POST["CarbonDioxide"] . "\n" . "CarbonDioxideGPIO = " . $_POST["CarbonDioxideGPIO"] . 
"\n" . "Oxygen = " . $_POST["Oxygen"] . "\n" . "OxygenGPIO = " . $_POST["OxygenGPIO"] . 
"\n" . "PiCam = " . $_POST["PiCam"] . "\n" . "CamRepInterval = " . $_POST["CamRepInterval"] . 
"\n" . "Interval = " . $_POST["Interval"] . 
"\n" . "";
// Write the contents back to the file
file_put_contents($file, $configText);

include 'index.php'; 

echo "File written (Not a verification)";
?>




</body>
</html>
