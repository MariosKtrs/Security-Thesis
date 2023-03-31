
<!DOCTYPE html>
<html>
	<head>
		<link rel="stylesheet" href="./styles.css">
	</head>
	<body>
		<div class="app">
			<div class="main">
				<h1>Ready to test your directory traversal skills?</h1>
				<p>I bet you can't read my flag at /home/secret/flag/flag.txt !</p>
				<img src="./bg.jpg">
			</div>
			<div class="info">
				<?php

						if (isset($_GET['file']) && (!is_numeric(strpos($_GET['file'],'/')))){
						echo '<br>';
						$filename = $_GET['file'];
						include urldecode($filename);
						echo '<br>';
						echo '<br>';

						echo 'filename: '.$filename;

					}
					else{
						echo 'Illegal characters found!';
						echo '<br>';
						echo $_GET['file'];
					}
				?>
			</div>
		</div>	
	</body>
</html>
