<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>ChemPi Overview</title>
<meta http-equiv="Content-Language" content="English" />
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
<link rel="stylesheet" type="text/css" href="style.css" media="screen" />
<script type="text/javascript"
  src="dygraph-combined.js"></script>
</head>
<body>
<div id="wrap">

<div id="top"></div>

<div id="content">

<div class="header">
<h1><a href="#">ChemPi</a></h1>
<h2>Free chemical analysis</h2>
</div>

<div class="breadcrumbs">
<a href="#">Home</a> &middot; You are here
</div>

<div class="middle">
			
<h2>Overview of sensors</h2> <br/>
<h3> Sensors active: </h3>	<br />
<ul>
<li> Temperature </li>
<li> Light </li>
<li> PiCamera </li>
<li> pH Orb </li>
<li>  </li>
</ul>		
<br /><br /><br />
<!--Defines for graphs-->
<script type="text/javascript">
var Temperature = "csv/Temperature.csv";
var Light = "csv/Light.csv";
var pH = "csv/pH.csv";
var Oxygen = "csv/Oxygen.csv";
var Oxygen = "csv/COTwo.csv";
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
<div>
<?php
include 'WebConfig.php';
?>
</div>
 		
</div>
		
<div class="right">
		
<h2>Navigation</h2>

<ul>
<li><a href="">Home</a></li>
<li><a href="">WebConfig</a></li>
<li><a href="/csv/">Export data</a></li>
<li><a href="http://bigalgae.com/about">BigAlgae</a></li>
<li><a href="/Pictures/">Pictures</a></li>
</ul>
		
</div>

<div id="clear"></div>

</div>

<div id="bottom"></div>

</div>

<div id="footer">
Design by <a href="http://www.minimalistic-design.net">Minimalistic Design</a>
</div>

</body>
</html>
