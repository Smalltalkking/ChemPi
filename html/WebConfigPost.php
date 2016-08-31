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
$configText = "Temperature = " . $Temperature . "\n" . "Light = " . $Light . "\n" . "Interval = " . $Interval . "\n";
// Write the contents back to the file
file_put_contents($file, $configText);

echo $configText;
?>



</body>
</html>
