<?php 
session_start();

	include("connection.php");
	include("functions.php");

	$user_data = check_login($con);

?>

<!DOCTYPE html>
<html>
    <head>
        <title>Welcome!</title>
        <link rel="stylesheet" href="./styles.css">
    </head>
    <body>
        <h1>Welcome to my Super Secure Website!</h1>
        <p>Hello <?php echo $user_data['user_name']; ?>
        <?php include_once 'nav.php'; ?>
    </body>
</html>
<script src="./index.js"></script>
