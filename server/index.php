<html>
<head>
<title>Get Distance</title>
</head>
<body>
<form action='index.php' method = 'get'>
<?php
if(isset($_GET['distance'])){
	$output = exec('sudo python3 /home/pi/Obstacles-Avoiding-Robot-Using-CNN/ultrasonic.py');
	echo $output."\n";
}
if(isset($_GET['camera'])){
	exec('sudo python3 /home/pi/Obstacles-Avoiding-Robot-Using-CNN/capture.py');
	echo "<img src='image.jpg'>";
}
if(isset($_GET['shutdown'])){
	echo "Raspberry Pi Shutdown !!!";
	exec('sudo shutdown -H now');
}
if(isset($_GET['train'])){
	echo "TRAINING STARTED !!!";
	exec('sudo python3 /home/pi/Obstacles-Avoiding-Robot-Using-CNN/reinforced.py');
	}
if(isset($_GET['autonomous'])){
	echo "STARTED !!!";
	exec('sudo python3 /home/pi/Obstacles-Avoiding-Robot-Using-CNN/predict.py');
	}
if(isset($_GET['reboot'])){
	echo "Raspberry Pi Rebooted !!!";
	exec('sudo reboot');
}
if(isset($_GET['up'])){
	exec('sudo python3 -c "import motor; motor.forward(1)"');
	}
if(isset($_GET['down'])){
	exec('sudo python3 -c "import motor; motor.reverse(1)"');
	}
if(isset($_GET['left'])){
	exec('sudo python3 -c "import motor; motor.left(1.5)"');
	}
if(isset($_GET['right'])){
	exec('sudo python3 -c "import motor; motor.right(1.5)"');
	}
?>
<br><button name = 'distance'>Distance</button>
<button name = 'camera'>Camera</button>
<button name = 'train'>Train</button>
<button name = 'autonomous'>Autonomous</button>
<button name = 'reboot'>Reboot</button>
<button name = 'shutdown'>Shutdown</button>
<br>
<center>
<button name = 'up'>UP</button><br><br>
<button name = 'left'>LEFT</button>
<button name = 'right'>RIGHT</button><br><br>
<button name = 'down'>DOWN</button>
</center>
</form>
</body>
</html>
