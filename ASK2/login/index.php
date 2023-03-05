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
        <form class="index-box" method="post">
            <p>Enter an id and check your emails from that person!</p>
            <input class="sender-id" name="sender" type="text">
            <input class="submit" type="submit" name="submit" value="Search"> 
           <?php 
                if(isset($_POST['submit'])){ 
                    $name = $_POST['sender'];  
                    echo $name;
                }
            ?>
        </form>
    </body>
</html>
<script src="./index.js"></script>
