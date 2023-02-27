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
        <link rel="stylesheet" href="styles.css">
        <style><?php include "styles.css" ?></style>
    </head>
    <body>
        <?php include_once "nav.php" ?>
        <h1>Welcome to your Super Secure Account <?php echo $user_data['user_name']?>!</h1>
        <p class="flag"> HTB{Y0u_4r3_An_SQL_1nj3ct10n_M4st3r} </p>
    </body>
</html>
<script src="./index.js"></script>
