<html>
<head>
<script type="text/javascript"
  src="dygraph-combined.js"></script>
</head>
<body>
<!--Defines for graphs-->
<script type="text/javascript">
var Temperature = "Temperature.csv";
var Light = "Light.csv";
var pH = "pH.csv";
var Oxygen = "Oxygen.csv";
var Oxygen = "COTwo.csv";
</script>
<!--End defines for graphs-->

<br />
Temperature
<br />

<div id="graphdiv2"
  style="width:500px; height:300px;">
</div>
<script type="text/javascript">
  g2 = new Dygraph(
    document.getElementById("graphdiv2"),
    Temperature, // path to CSV file
    {}          // options
  );
</script>
<br />
Light
<br />
<br />

<div id="graphLight"
  style="width:500px; height:300px;">
</div>
<script type="text/javascript">
  g2 = new Dygraph(
    document.getElementById("graphLight"),
    Light, // path to CSV file
    {}          // options
  );
</script>
<?php
include 'WebConfig.php';
?>
</body>
</html>
